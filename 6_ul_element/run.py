import webview
import glob

class Api:
    def selectTiff(self):
        file_types = ('Image Files (*.tif)', 'All files (*.*)')
        result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        return result
    def selectFolder(self):
        result = window.create_file_dialog(webview.FOLDER_DIALOG)
        if(result != None and len(result) >= 1):
            return glob.glob(result[0]+"\\"+"*.tif")
        else:
            return None

api=Api()
window = webview.create_window("My First App", url="web\\index.html", js_api=api)
webview.start(http_server=True, debug=True)
