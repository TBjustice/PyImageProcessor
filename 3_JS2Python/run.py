import webview

class Api:
    def add(self, a, b):
        print("Python")
        return a+b

api=Api()
window = webview.create_window("My First App", url="web\\index.html", js_api=api)
webview.start(http_server=True, debug=True)
