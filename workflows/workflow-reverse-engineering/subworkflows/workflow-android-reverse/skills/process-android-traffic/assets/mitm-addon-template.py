from mitmproxy import http

TARGET_HOST = "example.invalid"
TARGET_PATH = "/target"


def matches(flow: http.HTTPFlow) -> bool:
    return (
        flow.request.pretty_host == TARGET_HOST
        and flow.request.path.startswith(TARGET_PATH)
    )


def request(flow: http.HTTPFlow) -> None:
    if not matches(flow):
        return
    print({
        "method": flow.request.method,
        "path": flow.request.path,
        "content_length": len(flow.request.raw_content or b""),
    })


def response(flow: http.HTTPFlow) -> None:
    if not matches(flow):
        return
    print({
        "status_code": flow.response.status_code,
        "content_length": len(flow.response.raw_content or b""),
    })
