from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_socksdroid_route_keeps_entry_tls_and_protocol_failures_separate() -> None:
    # GIVEN：抓包 Skill 包含 VPN/tun2socks 强制转发说明。
    reference = (
        ROOT
        / "skills"
        / "capture-android-traffic"
        / "references"
        / "forced-routing-socksdroid.md"
    ).read_text(encoding="utf-8")

    # WHEN：检查失败分类和恢复约束。
    # THEN：流量入口、TLS/Pinning、QUIC 与停止恢复必须分别出现。
    assert "流量未进入代理" in reference
    assert "Pinning" in reference
    assert "QUIC" in reference
    assert "停止 VpnService" in reference


def test_mitm_session_supports_socks5_without_global_http_proxy() -> None:
    # GIVEN：mitmproxy 会话脚本承担 HTTP 与 SOCKS5 两种入口。
    script = (
        ROOT
        / "skills"
        / "process-android-traffic"
        / "scripts"
        / "mitmproxy-session.sh"
    ).read_text(encoding="utf-8")

    # WHEN：检查 SOCKS5 与 VPN 路由分支。
    # THEN：VPN 路线应清除全局 HTTP 代理并保留 USB reverse。
    assert 'MITM_MODE:-regular' in script
    assert 'MITM_ANDROID_ROUTE:-global-proxy' in script
    assert 'ANDROID_ROUTE" == "global-proxy' in script
    assert "settings put global http_proxy :0" in script


def test_socksdroid_script_braces_variables_next_to_unicode() -> None:
    # GIVEN：脚本输出使用中文标点。
    script = (
        ROOT
        / "skills"
        / "capture-android-traffic"
        / "scripts"
        / "socksdroid_capture.sh"
    ).read_text(encoding="utf-8")

    # WHEN：变量紧邻中文标点。
    # THEN：必须使用花括号，避免 locale 将标点并入变量名。
    assert "127.0.0.1:${PORT}，" in script
    assert "127.0.0.1:$PORT，" not in script


def test_socksdroid_green_requires_tun_and_restores_selinux_context() -> None:
    # GIVEN：Root 脚本负责写入 App 私有配置并判断 VPN 状态。
    script = (
        ROOT
        / "skills"
        / "capture-android-traffic"
        / "scripts"
        / "socksdroid_capture.sh"
    ).read_text(encoding="utf-8")

    # WHEN：检查设备配置和 Green 判据。
    # THEN：目录需恢复 UID/SELinux，且必须看到真实 TUN 地址。
    assert "chown -R $uid:$uid" in script
    assert "restorecon -RF" in script
    assert r"26\.26\.26\.1/24" in script


def test_socksdroid_routes_only_target_package_when_configured() -> None:
    # GIVEN：调用方明确提供本次研究的目标包名。
    script = (
        ROOT
        / "skills"
        / "capture-android-traffic"
        / "scripts"
        / "socksdroid_capture.sh"
    ).read_text(encoding="utf-8")

    # WHEN：启动 SocksDroid VpnService。
    # THEN：默认只强制转发目标 App，避免污染手机上其他应用的流量。
    assert "--ez SOCKSPERAPP true" in script
    assert "--ez SOCKSAPPBYPASS false" in script
    assert '--esa SOCKSAPPLIST "$TARGET_PACKAGE"' in script


def test_capture_skill_distinguishes_proxy_entry_from_business_success() -> None:
    # GIVEN：抓包 Skill 需要处理“有流量但业务失败”的真实案例。
    skill = (
        ROOT
        / "skills"
        / "capture-android-traffic"
        / "SKILL.md"
    ).read_text(encoding="utf-8")

    # WHEN：目标接口进入代理但服务端拒绝。
    # THEN：应转接口构造/风控诊断，而不是继续归因为代理故障。
    assert "zero-connection" in skill
    assert "non-target-only" in skill
    assert "target-request-non-2xx" in skill
    assert "抓包入口已恢复" in skill
