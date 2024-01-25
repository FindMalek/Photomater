from photoshop import Session
from app.services.file_service import FileService
from app.services.date_service import DateService
from app.utils.cli_utils import show_success_message, show_error_message, show_warning_message, show_info_message

class PhotoshopController:
    def __init__(self):
        self.file_service = FileService()

    def update_text_layer(self, client_name, file_name, week_date):
        print(f"Updating text layer in file '{file_name}' for client '{client_name}'.")
        file_data = self.file_service.get_client_file(client_name, file_name)
        layer_path = file_data['layer_path']

        with Session() as ps:
            document = ps.active_document
            artboards = document.artboards
            target_artboards = file_data['artboards']['Boards']

            for artboard in artboards:
                if artboard.name in target_artboards:
                    show_info_message(f"Searching in artboard: {artboard.name}")
                    target_layer = self.find_layer_recursive(artboard, layer_path.split())
                    if target_layer and target_layer.kind == ps.LayerKind.TextLayer:
                        show_info_message(f"Found layer: {target_layer.name}, Text: {target_layer.textItem.contents}")
                        target_layer.textItem.contents = week_date
                        show_success_message(f"Updated layer text to: {week_date}")
                        break
                    else:
                        show_warning_message("Target text layer not found in artboard.")
                        return False
            else:
                show_error_message("No matching artboard found.")
                return False
            
        return True

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
    
    def update_single_text_layer(self, file_data, week_date):
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
                    show_success_message(f"Updated layer text to: {week_date}")
                    return True

                else:
                    show_warning_message(f"Target text layer not found for path: {layer_path}")
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