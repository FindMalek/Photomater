from photoshop import Session
from app.services.file_service import FileService
from app.services.date_service import DateService
from app.utils.cli_utils import show_success_message, show_error_message, show_warning_message, show_info_message

class PhotoshopController:
    def __init__(self):
        self.file_service = FileService()
        self.ps = None 

    def open_document(self, psd_path):
        self.ps = Session()
        show_info_message(f"Opened document: {psd_path}")
        return self.ps.app.load(psd_path)
    
    def close_session(self):
        show_info_message("Closed Photoshop session.")
        if self.ps:
            self.ps.close()
            self.ps = None

    def update_layer_text(self, target_layer, text):
        if target_layer and target_layer.kind == self.ps.LayerKind.TextLayer:
            target_layer.textItem.contents = text
            return True
        return False

    @staticmethod
    def extract_layer_paths(path_object):
        """
        Extracts layer paths from the path_object.
        """
        layer_paths = []
        for key in path_object:
            if key == "Layers" and path_object[key]["Supported"]:
                layer_paths.append(path_object[key]["Path"])
            elif key != "Layers":
                layer_paths.extend(path_object[key].values())
        return layer_paths
    
    @staticmethod
    def find_layer_recursive(layer_set, target_path, current_path=[]):
        """
        Recursively searches for a layer within a Photoshop layer set.
        """
        if not target_path:
            return None

        next_layer_name = target_path[0]

        for layer in layer_set.layers:
            new_path = current_path + [layer.name]

            if layer.name == next_layer_name:
                if len(target_path) == 1:
                    return layer
                elif hasattr(layer, 'layers'):  
                    return PhotoshopController.find_layer_recursive(layer, target_path[1:], new_path)

        return None
    
    def update_text_in_artboard(self, artboard, layer_path, week_date):
        target_layer = self.find_layer_recursive(artboard, layer_path)
        if self.update_layer_text(target_layer, "69/70"):  # TODO: Replace "69/70" with dynamic text if needed
            show_info_message(f"Updated '{artboard.name}', '{target_layer.name}' to: {week_date}")
        else:
            show_warning_message("Target text layer not found in artboard.")

    def update_text_artboard(self, file_data, week_date):
        if not file_data or 'path_object' not in file_data:
            show_error_message("File data is missing or incomplete.")
            return False

        document = self.open_document(file_data['paths']['PSD'])
        layer_path = file_data['path_object']['Layers']['Path'].split('/')
        target_artboards = file_data['artboards']['Boards']

        for artboard in document.layers:
            if artboard.name in target_artboards:
                self.update_text_in_artboard(artboard, layer_path, week_date)

        self.close_session()
        return True
    
    def update_weekdate_layers(self, file_data, week_date):
        if not file_data or 'path_object' not in file_data:
            show_error_message("File data is missing or incomplete.")
            return False

        document = self.open_document(file_data['paths']['PSD'])
        layer_paths = self.extract_layer_paths(file_data['path_object'])

        for layer_path in layer_paths:
            target_layer = self.find_layer_recursive(document, layer_path.split('/'))
            if self.update_layer_text(target_layer, DateService.getWeekPointer(week_date, target_layer.name)):
                show_info_message(f"Updated '{target_layer.name}' layer text to: {week_date}")
            else:
                return False
            
        self.close_session()
        return True