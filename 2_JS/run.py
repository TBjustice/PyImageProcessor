import webview

window = webview.create_window("JavaScript", url="web\\index.html")
webview.start(http_server=True, debug=True)
