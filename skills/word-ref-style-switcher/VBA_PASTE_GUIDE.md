# Word 编号制引文转作者-年份制 VBA 宏

## 使用方法

1. 先保存当前 Word 文档。
2. 打开 Word，按 `Option + F11` 或从菜单进入 VBA 编辑器。
3. `Insert > Module` 新建一个普通模块。
4. 把下面代码块中的全部代码粘贴进去。
5. 回到 Word，运行宏 `SwitchNumericReferencesToAuthorYear`。

重要：请先手动复制一份 Word 原稿，再在副本里运行宏。

为了避开 Mac Word / 受保护文档 / 云同步目录中常见的 `5892 该方法无法用于对那个对象` 报错，这版宏不再自动另存副本，而是直接处理当前打开的文档。

## 适用前提

- 正文引用是纯文本，例如 `[1]`、`[2, 4, 5]`、`[33-37]`。
- 文末参考文献标题是 `References`、`Reference`、`Bibliography`、`Works Cited` 或 `参考文献`。
- 文末参考文献以编号开头，例如：

```text
1. K. L. Alvin, R. J. Murphy, “Variation in fibre and parenchyma wall thickness in culms of the bamboo Sinobambusa tootsik”, IAWA Journal 9 no.4 (1988) 353-361.
```

## 当前目标格式

宏会尽量把文末参考文献改成类似下面的格式：

```text
Alvin KL, Murphy RJ (1988) Variation in fibre and parenchyma wall thickness in culms of the bamboo Sinobambusa tootsik. IAWA Journal 9:353-361
Wang SY, Tsai MH, Lo SF et al (2008) Effects of manufacturing conditions on the adsorption capacity of heavy metal ions by Makino bamboo charcoal. Bioresource Technology 99:7027-33
```

默认规则：

- 文内：`(Rowell 1983)`、`(Alvin and Murphy 1988)`、`(Wang et al. 2008)`
- 文末作者：`K. L. Alvin` 转为 `Alvin KL`
- 文末作者超过 3 位：保留前 3 位作者，然后加 `et al`
- 文末排序：按第一作者姓氏排序
- 文末条目之间：不额外空行
- 同一文内标签重复时：自动加 `a/b/c`，例如 `(Chen et al. 2020a)`、`(Chen et al. 2020b)`

## VBA 代码

```vb
Option Explicit

Private Type RefItem
    OldNumber As Long
    RawText As String
    AuthorsPart As String
    FirstAuthorSurname As String
    CitationText As String
    YearText As String
    DisplayYearText As String
    SortKey As String
    ParseStatus As String
End Type

Private RefItems() As RefItem
Private RefCount As Long
Private Problems As Collection
Private ConvertedCitationCount As Long

Public Sub SwitchNumericReferencesToAuthorYear()
    On Error GoTo FailFast

    Dim doc As Document
    Dim refHeadingIndex As Long
    Dim bodyEndPos As Long

    Set doc = ActiveDocument
    Set Problems = New Collection
    ConvertedCitationCount = 0

    If doc.ProtectionType <> wdNoProtection Then
        MsgBox "当前文档处于保护状态，请先取消保护或另存为普通 .docx 副本后再运行宏。", vbExclamation
        Exit Sub
    End If

    refHeadingIndex = FindReferencesHeadingParagraph(doc)
    If refHeadingIndex = 0 Then
        MsgBox "没有找到参考文献标题。请确认标题是 References / Reference / Bibliography / Works Cited / 参考文献。", vbExclamation
        Exit Sub
    End If

    ParseReferenceSection doc, refHeadingIndex
    If RefCount = 0 Then
        MsgBox "没有解析到编号参考文献。请确认文末格式类似：1. Author, Title, Journal (2020) pages.", vbExclamation
        Exit Sub
    End If

    AssignYearSuffixesForDuplicateCitations

    bodyEndPos = doc.Paragraphs(refHeadingIndex).Range.Start
    ReplaceCitationsInRange doc.Range(0, bodyEndPos)
    RewriteReferenceSection doc, refHeadingIndex
    AppendConversionReport doc

    doc.Save
    MsgBox "转换完成。请检查文末的 Reference Style Switch Report。", vbInformation
    Exit Sub

FailFast:
    MsgBox "宏运行失败：" & Err.Number & vbCrLf & Err.Description, vbCritical
End Sub

Private Function FindReferencesHeadingParagraph(ByVal doc As Document) As Long
    Dim i As Long
    Dim t As String

    For i = 1 To doc.Paragraphs.Count
        t = LCase$(NormalizeParagraphText(doc.Paragraphs(i).Range.Text))

        If t = "references" _
            Or t = "reference" _
            Or t = "bibliography" _
            Or t = "works cited" _
            Or t = "参考文献" Then

            FindReferencesHeadingParagraph = i
            Exit Function
        End If
    Next i

    FindReferencesHeadingParagraph = 0
End Function

Private Sub ParseReferenceSection(ByVal doc As Document, ByVal headingParaIndex As Long)
    Dim i As Long
    Dim paraText As String
    Dim currentNumber As Long
    Dim currentText As String
    Dim parsedNumber As Long
    Dim restText As String

    RefCount = 0
    Erase RefItems

    currentNumber = 0
    currentText = ""

    For i = headingParaIndex + 1 To doc.Paragraphs.Count
        paraText = NormalizeParagraphText(doc.Paragraphs(i).Range.Text)

        If paraText <> "" Then
            If TryParseReferenceStart(paraText, parsedNumber, restText) Then
                If currentNumber > 0 Then
                    AddReferenceItem currentNumber, currentText
                End If

                currentNumber = parsedNumber
                currentText = restText
            Else
                If currentNumber > 0 Then
                    currentText = currentText & " " & paraText
                End If
            End If
        End If
    Next i

    If currentNumber > 0 Then
        AddReferenceItem currentNumber, currentText
    End If
End Sub

Private Function TryParseReferenceStart(ByVal textValue As String, ByRef numberValue As Long, ByRef restText As String) As Boolean
    Dim i As Long
    Dim ch As String
    Dim numberText As String

    textValue = Trim$(textValue)
    numberText = ""

    For i = 1 To Len(textValue)
        ch = Mid$(textValue, i, 1)

        If ch >= "0" And ch <= "9" Then
            numberText = numberText & ch
        Else
            Exit For
        End If
    Next i

    If numberText = "" Then
        TryParseReferenceStart = False
        Exit Function
    End If

    If i > Len(textValue) Then
        TryParseReferenceStart = False
        Exit Function
    End If

    ch = Mid$(textValue, i, 1)
    If ch <> "." And ch <> ")" Then
        TryParseReferenceStart = False
        Exit Function
    End If

    numberValue = CLng(numberText)
    restText = Trim$(Mid$(textValue, i + 1))
    TryParseReferenceStart = (restText <> "")
End Function

Private Sub AddReferenceItem(ByVal oldNumber As Long, ByVal rawReferenceText As String)
    Dim item As RefItem

    item.OldNumber = oldNumber
    item.RawText = rawReferenceText
    item.YearText = ExtractYear(rawReferenceText)
    item.DisplayYearText = item.YearText
    item.AuthorsPart = ExtractAuthorsPart(rawReferenceText)
    item.FirstAuthorSurname = ExtractFirstAuthorSurname(item.AuthorsPart)
    item.CitationText = BuildCitationText(item.AuthorsPart, item.DisplayYearText)
    item.SortKey = LCase$(item.FirstAuthorSurname & "|" & item.DisplayYearText & "|" & item.RawText)
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
    Dim i As Long
    Dim candidate As String

    For i = 1 To Len(textValue) - 3
        candidate = Mid$(textValue, i, 4)

        If IsFourDigitYear(candidate) Then
            ExtractYear = candidate
            Exit Function
        End If
    Next i

    ExtractYear = ""
End Function

Private Function IsFourDigitYear(ByVal s As String) As Boolean
    If Len(s) <> 4 Then
        IsFourDigitYear = False
        Exit Function
    End If

    If Not IsNumeric(s) Then
        IsFourDigitYear = False
        Exit Function
    End If

    IsFourDigitYear = (CLng(s) >= 1800 And CLng(s) <= 2099)
End Function

Private Function ExtractAuthorsPart(ByVal rawReferenceText As String) As String
    Dim p As Long
    Dim y As String

    p = InStr(rawReferenceText, ChrW(8220))
    If p > 1 Then
        ExtractAuthorsPart = CleanTrailingPunctuation(Left$(rawReferenceText, p - 1))
        Exit Function
    End If

    p = InStr(rawReferenceText, """")
    If p > 1 Then
        ExtractAuthorsPart = CleanTrailingPunctuation(Left$(rawReferenceText, p - 1))
        Exit Function
    End If

    y = ExtractYear(rawReferenceText)
    If y <> "" Then
        p = InStr(rawReferenceText, y)
        If p > 1 Then
            ExtractAuthorsPart = CleanTrailingPunctuation(Left$(rawReferenceText, p - 1))
            Exit Function
        End If
    End If

    p = InStr(rawReferenceText, ",")
    If p > 1 Then
        ExtractAuthorsPart = CleanTrailingPunctuation(Left$(rawReferenceText, p - 1))
    Else
        ExtractAuthorsPart = ""
    End If
End Function

Private Function CleanTrailingPunctuation(ByVal textValue As String) As String
    textValue = Trim$(textValue)

    Do While Len(textValue) > 0
        Select Case Right$(textValue, 1)
            Case ",", ".", ";", ":"
                textValue = Trim$(Left$(textValue, Len(textValue) - 1))
            Case Else
                Exit Do
        End Select
    Loop

    CleanTrailingPunctuation = textValue
End Function

Private Function ExtractFirstAuthorSurname(ByVal authorsPart As String) As String
    Dim firstAuthor As String

    authorsPart = Trim$(authorsPart)
    If authorsPart = "" Then
        ExtractFirstAuthorSurname = ""
        Exit Function
    End If

    firstAuthor = Split(authorsPart, ",")(0)
    ExtractFirstAuthorSurname = ExtractSurnameFromAuthor(firstAuthor)
End Function

Private Function BuildCitationText(ByVal authorsPart As String, ByVal yearText As String) As String
    Dim authorList As Collection
    Dim firstSurname As String
    Dim secondSurname As String

    Set authorList = SplitAuthorsSimple(authorsPart)

    If authorList.Count = 0 Then
        BuildCitationText = "Unknown " & FallbackYear(yearText)
    ElseIf authorList.Count = 1 Then
        firstSurname = ExtractSurnameFromAuthor(CStr(authorList(1)))
        BuildCitationText = firstSurname & " " & FallbackYear(yearText)
    ElseIf authorList.Count = 2 Then
        firstSurname = ExtractSurnameFromAuthor(CStr(authorList(1)))
        secondSurname = ExtractSurnameFromAuthor(CStr(authorList(2)))
        BuildCitationText = firstSurname & " and " & secondSurname & " " & FallbackYear(yearText)
    Else
        firstSurname = ExtractSurnameFromAuthor(CStr(authorList(1)))
        BuildCitationText = firstSurname & " et al. " & FallbackYear(yearText)
    End If
End Function

Private Function SplitAuthorsSimple(ByVal authorsPart As String) As Collection
    Dim result As New Collection
    Dim parts() As String
    Dim i As Long
    Dim candidate As String
    Dim previous As String

    authorsPart = Replace(authorsPart, " and ", ", ")
    parts = Split(authorsPart, ",")

    For i = LBound(parts) To UBound(parts)
        candidate = Trim$(parts(i))

        If candidate <> "" Then
            If LooksLikeInitials(candidate) And result.Count > 0 Then
                previous = CStr(result(result.Count))
                result.Remove result.Count
                result.Add previous & ", " & candidate
            Else
                result.Add candidate
            End If
        End If
    Next i

    Set SplitAuthorsSimple = result
End Function

Private Function LooksLikeInitials(ByVal textValue As String) As Boolean
    Dim i As Long
    Dim ch As String
    Dim hasLetter As Boolean

    textValue = Trim$(textValue)
    If textValue = "" Then
        LooksLikeInitials = False
        Exit Function
    End If

    For i = 1 To Len(textValue)
        ch = Mid$(textValue, i, 1)

        If ch >= "A" And ch <= "Z" Then
            hasLetter = True
        ElseIf ch = "." Or ch = " " Then
        Else
            LooksLikeInitials = False
            Exit Function
        End If
    Next i

    LooksLikeInitials = hasLetter
End Function

Private Function ExtractSurnameFromAuthor(ByVal authorText As String) As String
    Dim tokens() As String
    Dim t As String

    t = Trim$(authorText)
    If t = "" Then
        ExtractSurnameFromAuthor = "Unknown"
        Exit Function
    End If

    If InStr(t, ",") > 0 Then
        ExtractSurnameFromAuthor = CleanAuthorToken(Split(t, ",")(0))
        Exit Function
    End If

    tokens = Split(t, " ")
    ExtractSurnameFromAuthor = CleanAuthorToken(tokens(UBound(tokens)))
End Function

Private Function CleanAuthorToken(ByVal token As String) As String
    token = Trim$(token)
    token = Replace(token, ".", "")
    token = Replace(token, ",", "")
    token = Replace(token, ";", "")
    token = Replace(token, ":", "")
    CleanAuthorToken = token
End Function

Private Function FallbackYear(ByVal yearText As String) As String
    If yearText = "" Then
        FallbackYear = "n.d."
    Else
        FallbackYear = yearText
    End If
End Function

Private Sub AssignYearSuffixesForDuplicateCitations()
    Dim i As Long
    Dim j As Long
    Dim duplicateCount As Long
    Dim rank As Long
    Dim baseCitation As String
    Dim otherBaseCitation As String
    Dim currentKey As String
    Dim compareKey As String

    For i = 1 To RefCount
        RefItems(i).DisplayYearText = RefItems(i).YearText
        RefItems(i).CitationText = BuildCitationText(RefItems(i).AuthorsPart, RefItems(i).DisplayYearText)
    Next i

    For i = 1 To RefCount
        If RefItems(i).YearText <> "" Then
            baseCitation = BuildCitationText(RefItems(i).AuthorsPart, RefItems(i).YearText)
            duplicateCount = 0

            For j = 1 To RefCount
                If RefItems(j).YearText <> "" Then
                    otherBaseCitation = BuildCitationText(RefItems(j).AuthorsPart, RefItems(j).YearText)

                    If otherBaseCitation = baseCitation Then
                        duplicateCount = duplicateCount + 1
                    End If
                End If
            Next j

            If duplicateCount > 1 Then
                currentKey = DuplicateCitationOrderKey(RefItems(i))
                rank = 1

                For j = 1 To RefCount
                    If j <> i And RefItems(j).YearText <> "" Then
                        otherBaseCitation = BuildCitationText(RefItems(j).AuthorsPart, RefItems(j).YearText)

                        If otherBaseCitation = baseCitation Then
                            compareKey = DuplicateCitationOrderKey(RefItems(j))

                            If compareKey < currentKey Then
                                rank = rank + 1
                            ElseIf compareKey = currentKey And RefItems(j).OldNumber < RefItems(i).OldNumber Then
                                rank = rank + 1
                            End If
                        End If
                    End If
                Next j

                RefItems(i).DisplayYearText = RefItems(i).YearText & LetterFromRank(rank)
                RefItems(i).CitationText = BuildCitationText(RefItems(i).AuthorsPart, RefItems(i).DisplayYearText)
                RefItems(i).SortKey = LCase$(RefItems(i).FirstAuthorSurname & "|" & RefItems(i).DisplayYearText & "|" & RefItems(i).RawText)
            End If
        End If
    Next i
End Sub

Private Function DuplicateCitationOrderKey(ByRef item As RefItem) As String
    Dim titleText As String

    titleText = ExtractTitleFromReference(item.RawText)
    If titleText = "" Then
        titleText = item.RawText
    End If

    DuplicateCitationOrderKey = LCase$(titleText)
End Function

Private Function LetterFromRank(ByVal rank As Long) As String
    Dim n As Long
    Dim result As String

    n = rank
    result = ""

    Do While n > 0
        n = n - 1
        result = Chr$(97 + (n Mod 26)) & result
        n = n \ 26
    Loop

    LetterFromRank = result
End Function

Private Sub ReplaceCitationsInRange(ByVal rng As Range)
    Dim searchRange As Range
    Dim bracketRange As Range
    Dim innerText As String
    Dim replacement As String
    Dim moved As Long

    Set searchRange = rng.Duplicate

    With searchRange.Find
        .ClearFormatting
        .Text = "["
        .Forward = True
        .Wrap = wdFindStop
        .Format = False
        .MatchWildcards = False
    End With

    Do While searchRange.Find.Execute
        Set bracketRange = searchRange.Duplicate
        moved = bracketRange.MoveEndUntil(Cset:="]", Count:=wdForward)

        If moved > 0 Then
            bracketRange.MoveEnd Unit:=wdCharacter, Count:=1
            innerText = bracketRange.Text
            innerText = Mid$(innerText, 2, Len(innerText) - 2)

            If LooksLikeNumericCitation(innerText) Then
                replacement = BuildReplacementForCitation(innerText)

                If replacement <> "" Then
                    bracketRange.Text = replacement
                    ConvertedCitationCount = ConvertedCitationCount + 1
                    searchRange.SetRange Start:=bracketRange.End, End:=rng.End
                Else
                    searchRange.SetRange Start:=bracketRange.End, End:=rng.End
                End If
            Else
                searchRange.SetRange Start:=bracketRange.End, End:=rng.End
            End If
        Else
            searchRange.SetRange Start:=searchRange.End, End:=rng.End
        End If

        With searchRange.Find
            .ClearFormatting
            .Text = "["
            .Forward = True
            .Wrap = wdFindStop
            .Format = False
            .MatchWildcards = False
        End With
    Loop
End Sub

Private Function LooksLikeNumericCitation(ByVal innerText As String) As Boolean
    Dim i As Long
    Dim ch As String
    Dim hasDigit As Boolean

    innerText = Trim$(innerText)
    If innerText = "" Then
        LooksLikeNumericCitation = False
        Exit Function
    End If

    For i = 1 To Len(innerText)
        ch = Mid$(innerText, i, 1)

        If ch >= "0" And ch <= "9" Then
            hasDigit = True
        ElseIf ch = " " Or ch = "," Or ch = "-" Or AscW(ch) = 8211 Or AscW(ch) = 8212 Then
        Else
            LooksLikeNumericCitation = False
            Exit Function
        End If
    Next i

    LooksLikeNumericCitation = hasDigit
End Function

Private Function BuildReplacementForCitation(ByVal innerText As String) As String
    Dim numbers As Collection
    Dim citations As Collection
    Dim n As Variant
    Dim idx As Long
    Dim result As String
    Dim i As Long

    Set numbers = ExpandCitationNumbers(innerText)
    Set citations = New Collection

    For Each n In numbers
        idx = FindRefItemIndex(CLng(n))

        If idx > 0 Then
            citations.Add RefItems(idx).CitationText
        Else
            Problems.Add "正文引用 [" & CStr(n) & "] 在文末未找到对应参考文献。"
        End If
    Next n

    If citations.Count = 0 Then
        BuildReplacementForCitation = ""
        Exit Function
    End If

    result = ""
    For i = 1 To citations.Count
        If result <> "" Then
            result = result & "; "
        End If
        result = result & CStr(citations(i))
    Next i

    BuildReplacementForCitation = "(" & result & ")"
End Function

Private Function ExpandCitationNumbers(ByVal innerText As String) As Collection
    Dim result As New Collection
    Dim parts() As String
    Dim part As Variant
    Dim onePart As String
    Dim dashPos As Long
    Dim startN As Long
    Dim endN As Long
    Dim i As Long

    innerText = Replace(innerText, ChrW(8211), "-")
    innerText = Replace(innerText, ChrW(8212), "-")
    parts = Split(innerText, ",")

    For Each part In parts
        onePart = Trim$(CStr(part))
        dashPos = InStr(onePart, "-")

        If dashPos > 0 Then
            If IsNumeric(Trim$(Left$(onePart, dashPos - 1))) And IsNumeric(Trim$(Mid$(onePart, dashPos + 1))) Then
                startN = CLng(Trim$(Left$(onePart, dashPos - 1)))
                endN = CLng(Trim$(Mid$(onePart, dashPos + 1)))

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
        Else
            If IsNumeric(onePart) Then
                result.Add CLng(onePart)
            End If
        End If
    Next part

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
    Dim outputText As String
    Dim i As Long

    SortReferences

    Set refRange = doc.Range(doc.Paragraphs(headingParaIndex + 1).Range.Start, doc.Content.End)

    outputText = ""
    For i = 1 To RefCount
        If outputText <> "" Then
            outputText = outputText & vbCr
        End If

        outputText = outputText & FormatReferenceForTargetJournal(RefItems(i))
    Next i

    refRange.Text = outputText
    refRange.ParagraphFormat.SpaceBefore = 0
    refRange.ParagraphFormat.SpaceAfter = 0
End Sub

Private Function FormatReferenceForTargetJournal(ByRef item As RefItem) As String
    Dim formattedAuthors As String
    Dim titleText As String
    Dim journalTail As String
    Dim journalText As String
    Dim volumeText As String
    Dim pagesText As String
    Dim result As String

    formattedAuthors = FormatAuthorsForReferenceList(item.AuthorsPart)
    titleText = ExtractTitleFromReference(item.RawText)
    journalTail = ExtractJournalTailAfterTitle(item.RawText)
    journalTail = RemoveYearFromText(journalTail, item.YearText)

    journalText = ExtractJournalName(journalTail)
    volumeText = ExtractVolumeText(journalTail)
    pagesText = ExtractPagesAfterYear(item.RawText, item.YearText)

    If formattedAuthors = "" Or item.YearText = "" Or titleText = "" Then
        Problems.Add "Reference [" & item.OldNumber & "] 目标格式重写不完整，请人工复核：" & item.RawText
        FormatReferenceForTargetJournal = item.RawText
        Exit Function
    End If

    result = formattedAuthors & " (" & item.DisplayYearText & ") " & titleText

    If Right$(result, 1) <> "." Then
        result = result & "."
    End If

    If journalText <> "" Then
        result = result & " " & journalText
    End If

    If volumeText <> "" Then
        result = result & " " & volumeText
    End If

    If pagesText <> "" Then
        If volumeText <> "" Then
            result = result & ":" & pagesText
        Else
            result = result & " " & pagesText
        End If
    End If

    FormatReferenceForTargetJournal = result
End Function

Private Function FormatAuthorsForReferenceList(ByVal authorsPart As String) As String
    Dim authorList As Collection
    Dim result As String
    Dim i As Long
    Dim maxAuthors As Long

    Set authorList = SplitAuthorsSimple(authorsPart)

    If authorList.Count = 0 Then
        FormatAuthorsForReferenceList = ""
        Exit Function
    End If

    If authorList.Count > 3 Then
        maxAuthors = 3
    Else
        maxAuthors = authorList.Count
    End If

    result = ""
    For i = 1 To maxAuthors
        If result <> "" Then
            result = result & ", "
        End If

        result = result & FormatOneAuthorForReferenceList(CStr(authorList(i)))
    Next i

    If authorList.Count > 3 Then
        result = result & " et al"
    End If

    FormatAuthorsForReferenceList = result
End Function

Private Function FormatOneAuthorForReferenceList(ByVal authorText As String) As String
    Dim tokens() As String
    Dim surname As String
    Dim initials As String
    Dim i As Long
    Dim token As String

    authorText = Trim$(Replace(authorText, ",", " "))
    Do While InStr(authorText, "  ") > 0
        authorText = Replace(authorText, "  ", " ")
    Loop

    If authorText = "" Then
        FormatOneAuthorForReferenceList = ""
        Exit Function
    End If

    tokens = Split(authorText, " ")
    surname = CleanAuthorToken(tokens(UBound(tokens)))
    initials = ""

    For i = LBound(tokens) To UBound(tokens) - 1
        token = CleanAuthorToken(tokens(i))

        If token <> "" Then
            initials = initials & Left$(token, 1)
        End If
    Next i

    FormatOneAuthorForReferenceList = surname & " " & initials
End Function

Private Function ExtractTitleFromReference(ByVal rawReferenceText As String) As String
    Dim p1 As Long
    Dim p2 As Long

    p1 = InStr(rawReferenceText, ChrW(8220))
    If p1 > 0 Then
        p2 = InStr(p1 + 1, rawReferenceText, ChrW(8221))
        If p2 > p1 Then
            ExtractTitleFromReference = Trim$(Mid$(rawReferenceText, p1 + 1, p2 - p1 - 1))
            Exit Function
        End If
    End If

    p1 = InStr(rawReferenceText, """")
    If p1 > 0 Then
        p2 = InStr(p1 + 1, rawReferenceText, """")
        If p2 > p1 Then
            ExtractTitleFromReference = Trim$(Mid$(rawReferenceText, p1 + 1, p2 - p1 - 1))
            Exit Function
        End If
    End If

    ExtractTitleFromReference = ""
End Function

Private Function ExtractJournalTailAfterTitle(ByVal rawReferenceText As String) As String
    Dim p1 As Long
    Dim p2 As Long
    Dim tailText As String

    p1 = InStr(rawReferenceText, ChrW(8220))
    If p1 > 0 Then
        p2 = InStr(p1 + 1, rawReferenceText, ChrW(8221))
        If p2 > p1 Then
            tailText = Mid$(rawReferenceText, p2 + 1)
            ExtractJournalTailAfterTitle = CleanLeadingPunctuation(tailText)
            Exit Function
        End If
    End If

    p1 = InStr(rawReferenceText, """")
    If p1 > 0 Then
        p2 = InStr(p1 + 1, rawReferenceText, """")
        If p2 > p1 Then
            tailText = Mid$(rawReferenceText, p2 + 1)
            ExtractJournalTailAfterTitle = CleanLeadingPunctuation(tailText)
            Exit Function
        End If
    End If

    ExtractJournalTailAfterTitle = ""
End Function

Private Function CleanLeadingPunctuation(ByVal textValue As String) As String
    textValue = Trim$(textValue)

    Do While Len(textValue) > 0
        Select Case Left$(textValue, 1)
            Case ",", ".", ";", ":"
                textValue = Trim$(Mid$(textValue, 2))
            Case Else
                Exit Do
        End Select
    Loop

    CleanLeadingPunctuation = textValue
End Function

Private Function RemoveYearFromText(ByVal textValue As String, ByVal yearText As String) As String
    If yearText <> "" Then
        textValue = Replace(textValue, "(" & yearText & ")", " ")
        textValue = Replace(textValue, yearText, " ")
    End If

    Do While InStr(textValue, "  ") > 0
        textValue = Replace(textValue, "  ", " ")
    Loop

    RemoveYearFromText = Trim$(textValue)
End Function

Private Function ExtractJournalName(ByVal journalTail As String) As String
    Dim words() As String
    Dim i As Long
    Dim result As String

    journalTail = RemoveIssueMarker(journalTail)
    words = Split(Trim$(journalTail), " ")
    result = ""

    For i = LBound(words) To UBound(words)
        If IsNumeric(CleanNumberToken(words(i))) Then
            Exit For
        End If

        If result <> "" Then
            result = result & " "
        End If
        result = result & words(i)
    Next i

    ExtractJournalName = CleanTrailingPunctuation(result)
End Function

Private Function ExtractVolumeText(ByVal journalTail As String) As String
    Dim words() As String
    Dim i As Long
    Dim token As String

    journalTail = RemoveIssueMarker(journalTail)
    words = Split(Trim$(journalTail), " ")

    For i = LBound(words) To UBound(words)
        token = CleanNumberToken(words(i))

        If IsNumeric(token) Then
            ExtractVolumeText = token
            Exit Function
        End If
    Next i

    ExtractVolumeText = ""
End Function

Private Function RemoveIssueMarker(ByVal textValue As String) As String
    Dim p As Long
    Dim beforeText As String
    Dim afterText As String
    Dim i As Long

    p = InStr(1, LCase$(textValue), " no.")
    If p = 0 Then
        p = InStr(1, LCase$(textValue), " no ")
    End If

    If p = 0 Then
        RemoveIssueMarker = textValue
        Exit Function
    End If

    beforeText = Left$(textValue, p - 1)
    afterText = Mid$(textValue, p + 4)
    afterText = Trim$(afterText)

    i = 1
    Do While i <= Len(afterText)
        If Mid$(afterText, i, 1) >= "0" And Mid$(afterText, i, 1) <= "9" Then
            i = i + 1
        ElseIf Mid$(afterText, i, 1) = "." Then
            i = i + 1
        Else
            Exit Do
        End If
    Loop

    RemoveIssueMarker = Trim$(beforeText & " " & Mid$(afterText, i))
End Function

Private Function ExtractPagesAfterYear(ByVal rawReferenceText As String, ByVal yearText As String) As String
    Dim p As Long
    Dim tailText As String
    Dim words() As String
    Dim i As Long
    Dim token As String

    If yearText = "" Then
        ExtractPagesAfterYear = ""
        Exit Function
    End If

    p = InStr(rawReferenceText, "(" & yearText & ")")
    If p > 0 Then
        tailText = Mid$(rawReferenceText, p + Len(yearText) + 2)
    Else
        p = InStr(rawReferenceText, yearText)
        If p > 0 Then
            tailText = Mid$(rawReferenceText, p + Len(yearText))
        Else
            ExtractPagesAfterYear = ""
            Exit Function
        End If
    End If

    words = Split(Trim$(tailText), " ")

    For i = LBound(words) To UBound(words)
        token = CleanPageToken(words(i))

        If LooksLikePageRange(token) Then
            ExtractPagesAfterYear = token
            Exit Function
        End If
    Next i

    ExtractPagesAfterYear = ""
End Function

Private Function CleanNumberToken(ByVal token As String) As String
    token = Replace(token, ",", "")
    token = Replace(token, ".", "")
    token = Replace(token, ";", "")
    token = Replace(token, ":", "")
    CleanNumberToken = Trim$(token)
End Function

Private Function CleanPageToken(ByVal token As String) As String
    token = Replace(token, ".", "")
    token = Replace(token, ",", "")
    token = Replace(token, ";", "")
    token = Replace(token, ChrW(8211), "-")
    token = Replace(token, ChrW(8212), "-")
    CleanPageToken = Trim$(token)
End Function

Private Function LooksLikePageRange(ByVal token As String) As Boolean
    Dim i As Long
    Dim ch As String
    Dim hasDigit As Boolean

    If token = "" Then
        LooksLikePageRange = False
        Exit Function
    End If

    For i = 1 To Len(token)
        ch = Mid$(token, i, 1)

        If ch >= "0" And ch <= "9" Then
            hasDigit = True
        ElseIf ch = "-" Then
        Else
            LooksLikePageRange = False
            Exit Function
        End If
    Next i

    LooksLikePageRange = hasDigit
End Function

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

Private Sub AppendConversionReport(ByVal doc As Document)
    Dim r As Range
    Dim report As String
    Dim i As Long

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
            report = report & "- " & CStr(Problems(i)) & vbCrLf
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
```

## 说明

这版特意没有使用 `VBScript.RegExp`，也没有 `.bas` 文件里的 `Attribute VB_Name` 行，更适合直接粘贴到 Mac Word 或 Windows Word 的普通模块里。

第一轮跑完后，请重点看文档末尾的 `Reference Style Switch Report`。如果里面出现 `Unknown`、`n.d.` 或 `Needs review`，说明对应参考文献需要人工核对。
