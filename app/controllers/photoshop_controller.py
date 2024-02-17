from photoshop import Session
from app.services.file_service import FileService
from app.services.date_service import DateService
from app.utils.cli_utils import show_error_message, show_warning_message, show_info_message

class PhotoshopController:
    def __init__(self):
        self.file_service = FileService()
        self.date_service = DateService()
        self.week_date = self.date_service.get_week_date()
        self.ps = None 

    def open_document(self, psd_path):
        self.ps = Session()
        show_info_message(f"Opened document: {psd_path}")
        return self.ps.app.load(psd_path)
    
    def action_document(self, action):
        """
        Executes an action on the current Photoshop document.
        For example: "save" or "export".
        """
        if action == "save":
            self.ps.app.activeDocument.save()
            show_info_message("Saved changes to document.")
        elif action == "export":
            self.ps.app.activeDocument.export()
            show_info_message("Exported document.")

    def close_session(self):
        show_info_message("Closed Photoshop session.")
        if self.ps:
            self.ps.close()
            self.ps.app.activeDocument.close()
            self.ps = None

    def update_layer_text(self, target_layer, text):
        if target_layer and target_layer.kind == self.ps.LayerKind.TextLayer:
            target_layer.textItem.contents = text
            return True
        return False

    @staticmethod
    def extract_layer_paths(path_object, type):
        """
        Extracts layer paths from the path_object.
        """
        layer_paths = []

        if type == "artboard":
            for key in path_object["Main"]:
                layer_paths.append("Main/" + path_object["Main"][key])
        elif type == "layer":
            for key in path_object["Main"]:
                layer_paths.append(path_object["Main"][key])

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
    
    def update_text_in_artboard(self, artboard, layer_path):
        target_layer = self.find_layer_recursive(artboard, layer_path)

        artboard_date = self.date_service.getWeekDict(artboard.name, self.week_date)

        if self.update_layer_text(target_layer, artboard_date[artboard.name]): 
            show_info_message(f"Updated '{artboard.name}', '{target_layer.name}' to: {artboard_date[artboard.name]}")
        else:
            show_warning_message("Target text layer not found in artboard.")

    def update_weekdate_layers(self, document, layer_paths):
        for layer_path in layer_paths:
            target_layer = self.find_layer_recursive(document, layer_path.split('/'))

            if target_layer and self.update_layer_text(target_layer, DateService.getWeekPointer(self.week_date, target_layer.name)):
                show_info_message(f"Updated '{target_layer.name}'.")
            else:
                show_warning_message(f"Layer not found: {layer_path}")
                return False

    def update_type_artboard(self, file_data, action):
        if not file_data or 'path_object' not in file_data:
            show_error_message("File data is missing or incomplete.")
            return False

        document = self.open_document(file_data['paths']['PSD'])
        layer_path = file_data['path_object']['Layers']['Path'].split('/')
        target_artboards = file_data['artboards']['Boards']

        for artboard in document.layers:
            if artboard.name in target_artboards:
                self.update_text_in_artboard(artboard, layer_path)

        layer_paths = self.extract_layer_paths(file_data['path_object'], "artboard")
        self.update_weekdate_layers(document, layer_paths)

        self.action_document(action)
        self.close_session()
        return True

    def update_type_layer(self, file_data, action):
        if not file_data or 'path_object' not in file_data:
            show_error_message("File data is missing or incomplete.")
            return False

        document = self.open_document(file_data['paths']['PSD'])
        layer_paths = self.extract_layer_paths(file_data['path_object'], "layer")

        self.update_weekdate_layers(document, layer_paths)
            
        self.action_document(action)
        self.close_session()
        return True