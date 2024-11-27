from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    # Modify response headers
    flow.response.headers["Cache-Control"] = "public, max-age=31536000"
    flow.response.headers["X-Content-Type-Options"] = "nosniff"

# Run => mitmdump -s modify_headers.py -p 8081 on command prompt <= to start the proxy server.

