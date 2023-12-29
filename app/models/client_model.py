class FileDetails:
    def __init__(self, name: str, psd_path: str, export_path: str, google_drive_path: str, layer_path: str, supported_artboards: list):
        self.name = name
        self.paths = {
            "PSD": psd_path,
            "Export": export_path,
            "Google Drive": google_drive_path
        }
        self.layer_path = layer_path
        self.artboards = {
            "Supported": True if supported_artboards else False,
            "boards": supported_artboards
        }

class Client:
    def __init__(self, name: str, files: list):
        self.name = name
        self.files = files
