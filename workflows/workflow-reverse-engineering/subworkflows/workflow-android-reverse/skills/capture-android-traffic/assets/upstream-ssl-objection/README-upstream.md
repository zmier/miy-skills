# SSL / Objection Upstream Assets

这些脚本来自课程资料中的通用抓包对抗工具，按 upstream 原件保留，使用前复制到具体 TASK 目录。

## 文件

- `byssl.js`：覆盖常见 Java 层 SSL Pinning / TrustManager / OkHttp / WebView / TrustKit / Cronet 等路线的通用 unpinning 脚本。
- `key-strore.js`：双向认证场景中导出客户端证书为 `.p12` 的通用 Frida 脚本，默认密码见脚本内变量。
- `ssluningping.aggressive-reference.js`：更激进的全栈绕过参考脚本，保留为参考入口，不作为默认安全模板。

## 使用边界

- 仅用于授权 App、课堂靶场或自有测试环境。
- 使用前先完成 `https-mitm-diagnosis.md` 的分层，不要把所有 HTTPS 失败直接当成 Pinning。
- `key-strore.js` 会导出客户端证书，属于高敏感证据，只能保存在 TASK 本地受控目录，不写入 Markdown。
- 绕过脚本恢复明文只证明抓包观察链恢复，不证明接口复现完成。
