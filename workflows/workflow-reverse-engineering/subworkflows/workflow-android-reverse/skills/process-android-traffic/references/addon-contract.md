# mitmproxy Addon 契约

- 先过滤再读取正文。
- 只读观察和修改实验使用不同脚本或显式模式。
- 不在控制台打印 Cookie、Token、手机号、密码和完整设备标识。
- 修改实验记录唯一变量、原始请求编号、响应业务码和恢复基线。
- 上游代理、TLS 选项、连接复用与 HTTP 版本都是实验变量。
- 异常时不吞掉原请求，除非 TASK 明确要求阻断。
- mitmproxy 12 的 `request.query` 是 `MultiDictView`；使用其 `keys()` 或
  `items(multi=True)`，不要把它直接传给 `urllib.parse.parse_qsl`。
