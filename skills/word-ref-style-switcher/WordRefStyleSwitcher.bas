Attribute VB_Name = "WordRefStyleSwitcher"
Option Explicit

' Word Ref Style Switcher
' Converts numeric citations like [1], [2, 4, 5], [33-37]
' into author-year citations like (Alvin and Murphy, 1988).
'
' Assumptions for this first VBA version:
' 1. The manuscript is a normal Word .docx with plain-text citations.
' 2. The reference section starts with a paragraph whose text is "References",
'    "Reference", "Bibliography", or "参考文献".
' 3. Each reference starts with a numeric label, for example:
'    1. K. L. Alvin, R. J. Murphy, “Title”, Journal 9 no.4 (1988) 353-361.
'
' Run:
'   SwitchNumericReferencesToAuthorYear
'
' The macro saves a copy of the active document, works on the copy, then appends
' a conversion report at the end.

Private Type RefItem
    OldNumber As Long
    RawText As String
    AuthorsPart As String
    SortKey As String
    FirstAuthorSurname As String
    CitationText As String
    YearText As String
    ParseStatus As String
End Type

Private RefItems() As RefItem
Private RefCount As Long
Private Problems As Collection
Private ConvertedCitationCount As Long

Public Sub SwitchNumericReferencesToAuthorYear()
    On Error GoTo FailFast

    Dim srcDoc As Document
    Dim doc As Document
    Dim copyPath As String
    Dim refStartParaIndex As Long
    Dim bodyEndPos As Long

    Set srcDoc = ActiveDocument
    Set Problems = New Collection
    ConvertedCitationCount = 0

    If srcDoc.Path = "" Then
        MsgBox "请先保存当前 Word 文档，再运行宏。", vbExclamation
        Exit Sub
    End If

    copyPath = BuildOutputPath(srcDoc)
    srcDoc.Save
    If Dir(copyPath) <> "" Then Kill copyPath
    srcDoc.SaveCopyAs copyPath
    Set doc = Documents.Open(FileName:=copyPath)

    refStartParaIndex = FindReferencesHeadingParagraph(doc)
    If refStartParaIndex = 0 Then
        MsgBox "没有找到参考文献标题。请确认标题是 References / Reference / Bibliography / 参考文献。", vbExclamation
        Exit Sub
    End If

    ParseReferenceSection doc, refStartParaIndex
    If RefCount = 0 Then
        MsgBox "没有解析到编号参考文献。请确认文末格式类似：1. Author, Title, Journal (2020) pages.", vbExclamation
        Exit Sub
    End If

    bodyEndPos = doc.Paragraphs(refStartParaIndex).Range.Start
    ReplaceInTextRange doc.Range(0, bodyEndPos)
    RewriteReferenceSection doc, refStartParaIndex
    AppendConversionReport doc

    doc.Save
    MsgBox "转换完成，已保存副本：" & vbCrLf & copyPath, vbInformation
    Exit Sub

FailFast:
    MsgBox "宏运行失败：" & Err.Description, vbCritical
End Sub

Private Function BuildOutputPath(ByVal doc As Document) As String
    Dim baseName As String
    Dim extPos As Long

    baseName = doc.Name
    extPos = InStrRev(baseName, ".")
    If extPos > 0 Then baseName = Left$(baseName, extPos - 1)

    BuildOutputPath = doc.Path & Application.PathSeparator & baseName & "_author_year.docx"
End Function

Private Function FindReferencesHeadingParagraph(ByVal doc As Document) As Long
    Dim i As Long
    Dim t As String

    For i = 1 To doc.Paragraphs.Count
        t = NormalizeParagraphText(doc.Paragraphs(i).Range.Text)
        Select Case LCase$(t)
            Case "references", "reference", "bibliography", "works cited"
                FindReferencesHeadingParagraph = i
                Exit Function
            Case "参考文献"
                FindReferencesHeadingParagraph = i
                Exit Function
        End Select
    Next i

    FindReferencesHeadingParagraph = 0
End Function

Private Sub ParseReferenceSection(ByVal doc As Document, ByVal headingParaIndex As Long)
    Dim i As Long
    Dim paraText As String
    Dim currentNumber As Long
    Dim currentText As String
    Dim n As Long
    Dim restText As String

    RefCount = 0
    Erase RefItems

    currentNumber = 0
    currentText = ""

    For i = headingParaIndex + 1 To doc.Paragraphs.Count
        paraText = NormalizeParagraphText(doc.Paragraphs(i).Range.Text)

        If paraText <> "" Then
            If TryParseReferenceStart(paraText, n, restText) Then
                If currentNumber > 0 Then AddReferenceItem currentNumber, currentText
                currentNumber = n
                currentText = restText
            ElseIf currentNumber > 0 Then
                currentText = currentText & " " & paraText
            End If
        End If
    Next i

    If currentNumber > 0 Then AddReferenceItem currentNumber, currentText
End Sub

Private Function TryParseReferenceStart(ByVal textValue As String, ByRef numberValue As Long, ByRef restText As String) As Boolean
    Dim re As Object
    Dim matches As Object

    Set re = CreateObject("VBScript.RegExp")
    re.Pattern = "^\s*(\d+)[\.\)]\s+(.+)$"
    re.Global = False
    re.IgnoreCase = True

    If re.Test(textValue) Then
        Set matches = re.Execute(textValue)
        numberValue = CLng(matches(0).SubMatches(0))
        restText = Trim$(matches(0).SubMatches(1))
        TryParseReferenceStart = True
    Else
        TryParseReferenceStart = False
    End If
End Function

Private Sub AddReferenceItem(ByVal oldNumber As Long, ByVal rawReferenceText As String)
    Dim item As RefItem

    item.OldNumber = oldNumber
    item.RawText = rawReferenceText
    item.YearText = ExtractYear(rawReferenceText)
    item.AuthorsPart = ExtractAuthorsPart(rawReferenceText)
    item.FirstAuthorSurname = ExtractFirstAuthorSurname(item.AuthorsPart)
    item.CitationText = BuildCitationText(item.AuthorsPart, item.YearText)
    item.SortKey = BuildSortKey(item)
    item.ParseStatus = "OK"

    If item.YearText = "" Then
        item.ParseStatus = "Needs review: year not found"
        Problems.Add "Reference [" & oldNumber & "] 缺少年份：" & rawReferenceText
    End If

    If item.FirstAuthorSurname = "" Then
        item.ParseStatus = "Needs review: author not found"
        Problems.Add "Reference [" & oldNumber & "] 作者解析失败：" & rawReferenceText
    End If

    RefCount = RefCount + 1
    ReDim Preserve RefItems(1 To RefCount)
    RefItems(RefCount) = item
End Sub

Private Function ExtractYear(ByVal textValue As String) As String
    Dim re As Object
    Dim matches As Object

    Set re = CreateObject("VBScript.RegExp")
    re.Pattern = "\((18|19|20)\d{2}[a-z]?\)"
    re.Global = False
    re.IgnoreCase = True

    If re.Test(textValue) Then
        Set matches = re.Execute(textValue)
        ExtractYear = Replace(Replace(matches(0).Value, "(", ""), ")", "")
    Else
        re.Pattern = "\b(18|19|20)\d{2}[a-z]?\b"
        If re.Test(textValue) Then
            Set matches = re.Execute(textValue)
            ExtractYear = matches(0).Value
        Else
            ExtractYear = ""
        End If
    End If
End Function

Private Function ExtractAuthorsPart(ByVal rawReferenceText As String) As String
    Dim qPos1 As Long
    Dim qPos2 As Long
    Dim commaQuotePos As Long
    Dim yearPos As Long

    qPos1 = InStr(rawReferenceText, ChrW(&H201C))
    qPos2 = InStr(rawReferenceText, """")

    If qPos1 > 1 Then
        ExtractAuthorsPart = CleanTrailingComma(Left$(rawReferenceText, qPos1 - 1))
        Exit Function
    End If

    If qPos2 > 1 Then
        ExtractAuthorsPart = CleanTrailingComma(Left$(rawReferenceText, qPos2 - 1))
        Exit Function
    End If

    commaQuotePos = InStr(rawReferenceText, ", ")
    yearPos = InStr(rawReferenceText, "(" & ExtractYear(rawReferenceText) & ")")

    If yearPos > 1 Then
        ExtractAuthorsPart = CleanTrailingComma(Left$(rawReferenceText, yearPos - 1))
    ElseIf commaQuotePos > 1 Then
        ExtractAuthorsPart = CleanTrailingComma(Left$(rawReferenceText, commaQuotePos - 1))
    Else
        ExtractAuthorsPart = ""
    End If
End Function

Private Function CleanTrailingComma(ByVal textValue As String) As String
    textValue = Trim$(textValue)
    Do While Len(textValue) > 0 And (Right$(textValue, 1) = "," Or Right$(textValue, 1) = "." Or Right$(textValue, 1) = ";")
        textValue = Trim$(Left$(textValue, Len(textValue) - 1))
    Loop
    CleanTrailingComma = textValue
End Function

Private Function ExtractFirstAuthorSurname(ByVal authorsPart As String) As String
    Dim firstAuthor As String
    Dim tokens() As String

    If Trim$(authorsPart) = "" Then
        ExtractFirstAuthorSurname = ""
        Exit Function
    End If

    firstAuthor = Split(authorsPart, ",")(0)
    firstAuthor = Trim$(firstAuthor)
    tokens = Split(firstAuthor, " ")

    If UBound(tokens) >= 0 Then
        ExtractFirstAuthorSurname = CleanAuthorToken(tokens(UBound(tokens)))
    Else
        ExtractFirstAuthorSurname = ""
    End If
End Function

Private Function BuildCitationText(ByVal authorsPart As String, ByVal yearText As String) As String
    Dim authors() As String
    Dim countAuthors As Long
    Dim firstSurname As String
    Dim secondSurname As String

    If Trim$(authorsPart) = "" Then
        If yearText <> "" Then
            BuildCitationText = "Unknown, " & yearText
        Else
            BuildCitationText = "Unknown, n.d."
        End If
        Exit Function
    End If

    authors = SplitAuthors(authorsPart)
    countAuthors = SafeArrayCount(authors)

    If countAuthors = 0 Or Trim$(authors(0)) = "" Then
        If yearText <> "" Then
            BuildCitationText = "Unknown, " & yearText
        Else
            BuildCitationText = "Unknown, n.d."
        End If
        Exit Function
    End If

    firstSurname = ExtractSurnameFromAuthor(authors(0))

    If countAuthors = 1 Then
        BuildCitationText = firstSurname & ", " & FallbackYear(yearText)
    ElseIf countAuthors = 2 Then
        secondSurname = ExtractSurnameFromAuthor(authors(1))
        BuildCitationText = firstSurname & " and " & secondSurname & ", " & FallbackYear(yearText)
    Else
        BuildCitationText = firstSurname & " et al., " & FallbackYear(yearText)
    End If
End Function

Private Function SplitAuthors(ByVal authorsPart As String) As String()
    Dim normalized As String
    Dim rawParts() As String
    Dim result() As String
    Dim i As Long
    Dim count As Long
    Dim candidate As String

    normalized = Replace(authorsPart, " and ", ", ")
    rawParts = Split(normalized, ",")
    ReDim result(0 To 0)
    count = 0

    i = 0
    Do While i <= UBound(rawParts)
        candidate = Trim$(rawParts(i))

        If candidate <> "" Then
            If LooksLikeInitialsOnly(candidate) And count > 0 Then
                result(count - 1) = Trim$(result(count - 1) & ", " & candidate)
            Else
                If count = 0 Then
                    ReDim result(0 To 0)
                Else
                    ReDim Preserve result(0 To count)
                End If
                result(count) = candidate
                count = count + 1
            End If
        End If

        i = i + 1
    Loop

    If count = 0 Then
        ReDim result(0 To 0)
        result(0) = ""
    End If

    SplitAuthors = result
End Function

Private Function LooksLikeInitialsOnly(ByVal textValue As String) As Boolean
    Dim re As Object
    Set re = CreateObject("VBScript.RegExp")
    re.Pattern = "^([A-Z]\.\s*)+$"
    re.IgnoreCase = False
    LooksLikeInitialsOnly = re.Test(Trim$(textValue))
End Function

Private Function SafeArrayCount(ByRef arr() As String) As Long
    On Error GoTo EmptyArray
    SafeArrayCount = UBound(arr) - LBound(arr) + 1
    Exit Function
EmptyArray:
    SafeArrayCount = 0
End Function

Private Function ExtractSurnameFromAuthor(ByVal authorText As String) As String
    Dim t As String
    Dim tokens() As String

    t = Trim$(authorText)
    If InStr(t, ",") > 0 Then
        ExtractSurnameFromAuthor = CleanAuthorToken(Trim$(Split(t, ",")(0)))
        Exit Function
    End If

    tokens = Split(t, " ")
    If UBound(tokens) >= 0 Then
        ExtractSurnameFromAuthor = CleanAuthorToken(tokens(UBound(tokens)))
    Else
        ExtractSurnameFromAuthor = "Unknown"
    End If
End Function

Private Function CleanAuthorToken(ByVal token As String) As String
    token = Trim$(token)
    token = Replace(token, ".", "")
    token = Replace(token, ",", "")
    token = Replace(token, ";", "")
    CleanAuthorToken = token
End Function

Private Function FallbackYear(ByVal yearText As String) As String
    If yearText = "" Then
        FallbackYear = "n.d."
    Else
        FallbackYear = yearText
    End If
End Function

Private Function BuildSortKey(ByRef item As RefItem) As String
    BuildSortKey = LCase$(item.FirstAuthorSurname & "|" & item.YearText & "|" & item.RawText)
End Function

Private Sub ReplaceInTextRange(ByVal rng As Range)
    Dim re As Object
    Dim matches As Object
    Dim i As Long
    Dim hit As Object
    Dim hitStart As Long
    Dim hitEnd As Long
    Dim replacement As String
    Dim workRange As Range
    Dim sourceText As String

    sourceText = rng.Text
    Set re = CreateObject("VBScript.RegExp")
    re.Pattern = "\[((\s*\d+\s*([\-,–—]\s*\d+\s*)?)(,\s*\d+\s*([\-,–—]\s*\d+\s*)?)*)\]"
    re.Global = True
    re.IgnoreCase = True

    If Not re.Test(sourceText) Then Exit Sub
    Set matches = re.Execute(sourceText)

    For i = matches.Count - 1 To 0 Step -1
        Set hit = matches(i)
        replacement = BuildReplacementForBracketCitation(hit.Value)

        If replacement <> "" Then
            hitStart = rng.Start + hit.FirstIndex
            hitEnd = hitStart + hit.Length
            Set workRange = rng.Document.Range(hitStart, hitEnd)
            workRange.Text = replacement
            ConvertedCitationCount = ConvertedCitationCount + 1
        End If
    Next i
End Sub

Private Function BuildReplacementForBracketCitation(ByVal bracketText As String) As String
    Dim innerText As String
    Dim numbers As Collection
    Dim citations As Collection
    Dim i As Long
    Dim n As Variant
    Dim itemIndex As Long
    Dim result As String

    innerText = Replace(Replace(bracketText, "[", ""), "]", "")
    Set numbers = ExpandCitationNumbers(innerText)
    Set citations = New Collection

    For Each n In numbers
        itemIndex = FindRefItemIndex(CLng(n))
        If itemIndex > 0 Then
            citations.Add RefItems(itemIndex).CitationText
        Else
            Problems.Add "正文引用 [" & CStr(n) & "] 在文末未找到对应参考文献。"
        End If
    Next n

    If citations.Count = 0 Then
        BuildReplacementForBracketCitation = ""
        Exit Function
    End If

    result = ""
    For i = 1 To citations.Count
        If result <> "" Then result = result & "; "
        result = result & citations(i)
    Next i

    BuildReplacementForBracketCitation = "(" & result & ")"
End Function

Private Function ExpandCitationNumbers(ByVal innerText As String) As Collection
    Dim result As New Collection
    Dim parts() As String
    Dim p As Variant
    Dim normalized As String
    Dim bounds() As String
    Dim startN As Long
    Dim endN As Long
    Dim i As Long

    normalized = Replace(innerText, "–", "-")
    normalized = Replace(normalized, "—", "-")
    parts = Split(normalized, ",")

    For Each p In parts
        normalized = Trim$(CStr(p))
        If InStr(normalized, "-") > 0 Then
            bounds = Split(normalized, "-")
            If UBound(bounds) = 1 And IsNumeric(Trim$(bounds(0))) And IsNumeric(Trim$(bounds(1))) Then
                startN = CLng(Trim$(bounds(0)))
                endN = CLng(Trim$(bounds(1)))
                If startN <= endN Then
                    For i = startN To endN
                        result.Add i
                    Next i
                Else
                    For i = startN To endN Step -1
                        result.Add i
                    Next i
                End If
            End If
        ElseIf IsNumeric(normalized) Then
            result.Add CLng(normalized)
        End If
    Next p

    Set ExpandCitationNumbers = result
End Function

Private Function FindRefItemIndex(ByVal oldNumber As Long) As Long
    Dim i As Long
    For i = 1 To RefCount
        If RefItems(i).OldNumber = oldNumber Then
            FindRefItemIndex = i
            Exit Function
        End If
    Next i
    FindRefItemIndex = 0
End Function

Private Sub RewriteReferenceSection(ByVal doc As Document, ByVal headingParaIndex As Long)
    Dim refRange As Range
    Dim i As Long
    Dim outputText As String

    SortReferences

    Set refRange = doc.Range(doc.Paragraphs(headingParaIndex + 1).Range.Start, doc.Content.End)

    outputText = ""
    For i = 1 To RefCount
        outputText = outputText & FormatReferenceForAuthorYear(RefItems(i)) & vbCrLf
    Next i

    refRange.Text = outputText
End Sub

Private Sub SortReferences()
    Dim i As Long
    Dim j As Long
    Dim temp As RefItem

    For i = 1 To RefCount - 1
        For j = i + 1 To RefCount
            If RefItems(j).SortKey < RefItems(i).SortKey Then
                temp = RefItems(i)
                RefItems(i) = RefItems(j)
                RefItems(j) = temp
            End If
        Next j
    Next i
End Sub

Private Function FormatReferenceForAuthorYear(ByRef item As RefItem) As String
    FormatReferenceForAuthorYear = item.RawText
End Function

Private Sub AppendConversionReport(ByVal doc As Document)
    Dim r As Range
    Dim i As Long
    Dim report As String

    report = vbCrLf & "Reference Style Switch Report" & vbCrLf
    report = report & "=============================" & vbCrLf
    report = report & "Parsed references: " & RefCount & vbCrLf
    report = report & "Converted in-text citation groups: " & ConvertedCitationCount & vbCrLf
    report = report & "Problems requiring review: " & Problems.Count & vbCrLf & vbCrLf

    report = report & "Number to author-year map:" & vbCrLf
    For i = 1 To RefCount
        report = report & "[" & RefItems(i).OldNumber & "] -> " & RefItems(i).CitationText & " | " & RefItems(i).ParseStatus & vbCrLf
    Next i

    If Problems.Count > 0 Then
        report = report & vbCrLf & "Problems:" & vbCrLf
        For i = 1 To Problems.Count
            report = report & "- " & Problems(i) & vbCrLf
        Next i
    End If

    Set r = doc.Range(doc.Content.End - 1, doc.Content.End - 1)
    r.InsertAfter vbCrLf & report
End Sub

Private Function NormalizeParagraphText(ByVal textValue As String) As String
    textValue = Replace(textValue, vbCr, "")
    textValue = Replace(textValue, vbLf, "")
    textValue = Replace(textValue, Chr(7), "")
    NormalizeParagraphText = Trim$(textValue)
End Function
