from photoshop import Session
from app.services.file_service import FileService
from app.services.date_service import DateService
from app.utils.cli_utils import show_success_message, show_error_message, show_warning_message, show_info_message

class PhotoshopController:
    def __init__(self):
        self.file_service = FileService()

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
    
    def update_text_artboard(self, file_data, week_date):
        if not file_data or 'path_object' not in file_data:
            show_error_message("File data is missing or incomplete.")
            return False

        psd_path = file_data['paths']['PSD']
        layer_path = file_data['path_object']['Layers']['Path'].split('/')
        target_artboards = file_data['artboards']['Boards']

        with Session(action=psd_path) as ps:
            document = ps.active_document
        
            for artboard in document.layers:
                if artboard.name in target_artboards:
                    show_info_message(f"Searching in artboard: {artboard.name}")
                    target_layer = self.find_layer_recursive(artboard, layer_path)
                    if target_layer and target_layer.kind == ps.LayerKind.TextLayer:
                        show_info_message(f"Found layer: {target_layer.name}, Text: {target_layer.textItem.contents}")
                        # @TODO: Add logic to update the text layer
                        # Create a function that gets the week pointer based on the layer name
                        target_layer.textItem.contents = "00/90"
                        show_success_message(f"Updated layer text to: {week_date}")
                    else:
                        show_warning_message("Target text layer not found in artboard.")
                        return False
        return True
    
    def update_text_layer(self, file_data, week_date):
        if not file_data or 'path_object' not in file_data:
            show_error_message("File data is missing or incomplete.")
            return

        psd_path = file_data['paths']['PSD']
        path_object = file_data['path_object']
        layer_paths = self.extract_layer_paths(path_object)

        with Session(psd_path) as ps:
            document = ps.active_document

            for layer_path in layer_paths:
                target_layer = self.find_layer_recursive(document, layer_path.split('/'))
                if target_layer and target_layer.kind == ps.LayerKind.TextLayer:
                    show_info_message(f"Found layer: {target_layer.name}, Text: {target_layer.textItem.contents}")

                    target_layer.textItem.contents = DateService.getWeekPointer(week_date, target_layer.name)
                else:
                    return False
        return True