from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    # Modify response headers
    flow.response.headers["Cache-Control"] = "public, max-age=31536000"
    flow.response.headers["X-Content-Type-Options"] = "nosniff"