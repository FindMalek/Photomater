from photoshop import Session
from app.services.file_service import FileService
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
            else:
                show_error_message("No matching artboard found.")

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

                elif layer.typename == 'LayerSet':
                    return PhotoshopController.find_layer_recursive(layer, target_path[1:], new_path)

        return None