import json
from app.services.file_service import FileService
from app.models.client_model import Client, FileDetails

class ClientController:
    def __init__(self):
        self.file_service = FileService()

    def add_client(self, name, files_data=None):
        files = []
        if files_data:
            for file_data in files_data:
                file_details = FileDetails(
                    name=file_data['name'],
                    psd_path=file_data['paths']['PSD'],
                    export_path=file_data['paths']['Export'],
                    google_drive_path=file_data['paths']['Google Drive'],
                    layer_path=file_data['layer_path'],
                    supported_artboards=file_data['artboards']['boards']
                )
                files.append(file_details)

        client = Client(name=name, files=files)
        self.file_service.add_client(client)

    def edit_client(self, name, new_name=None, new_file_location=None, new_export_location=None, new_artboards=None, new_layer_path=None):
        # Logic to edit an existing client
        updated_data = {
            "name": new_name,
            "file_location": new_file_location,
            "export_location": new_export_location,
            "artboards": new_artboards.split(",") if new_artboards else None,
            "layer_path": new_layer_path
        }
        self.file_service.edit_client(name, updated_data)

    def remove_client(self, name):
        # Logic to remove a client
        self.file_service.remove_client(name)

    def list_clients(self):
        # Logic to list all clients
        return self.file_service.get_all_clients()

    def update_client_files(self, client_name, all_files=False, specific_file=None, save=False, export=False):
        client_data = self.file_service.get_client(client_name)
        if client_data:
            # Call PhotoshopController to perform updates
            self.photoshop_controller.update_text_layers(client_data, all_files, specific_file, save, export)
            return "Update process completed."
        else:
            return "Client not found."
