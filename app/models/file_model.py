class FileDetails:
    def __init__(self, name: str, psd_path: str, export_path: str, google_drive_path: str, path_object: dict, supported_artboards: list):
        self.name = name
        self.paths = {
            "PSD": psd_path,
            "Export": export_path,
            "Google Drive": google_drive_path
        }
        self.path_object = {
            "Main": {
                "start": path_object['Main']['start'],
                "end": path_object['Main']['end']
            },
            "Layers": {
                "Supported": bool(supported_artboards),
                "Path": "" if not supported_artboards else path_object['Layers']['Path']
            }
        } 
        self.artboards = {
            "Supported": bool(supported_artboards),
            "Boards": supported_artboards
        }