import json
from app.services.file_service import FileService

class ClientController:
    def __init__(self):
        self.file_service = FileService()

    def add_client(self, name, file_location, export_location, artboards, layer_path):
        # Logic to add a new client
        client_data = {
            "name": name,
            "file_location": file_location,
            "export_location": export_location,
            "artboards": artboards.split(","),
            "layer_path": layer_path
        }
        self.file_service.add_client(client_data)

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
