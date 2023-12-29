from app.services.file_service import FileService
from app.models.client_model import Client, FileDetails
from app.utils.cli_utils import show_error_message, show_success_message

class ClientController:
    def __init__(self):
        self.file_service = FileService()

    def add_client(self, name, files_data=None):
        existing_clients = self.file_service.get_all_clients()
        client_found = next((client for client in existing_clients if client['name'].lower() == name.lower()), None)

        if client_found:
            for file_data in files_data:
                file_name_exists = any(file['name'] == file_data['name'] for file in client_found['files'])
                if file_name_exists:
                    show_error_message(f"File name '{file_data['name']}' already exists in client '{name}'.")
                    return  
                else:
                    new_file = FileDetails(
                        name=file_data['name'],
                        psd_path=file_data['paths']['PSD'],
                        export_path=file_data['paths']['Export'],
                        google_drive_path=file_data['paths']['Google Drive'],
                        layer_path=file_data['layer_path'],
                        supported_artboards=file_data['artboards']['boards']
                    )
                    client_found['files'].append(new_file.__dict__)
                updated_client = Client(name=name.lower(), files=client_found['files'])
                self.file_service.update_client(updated_client)
                show_success_message(f"File '{file_data['name']}' added to client '{name}'.")
        else:
            files = [FileDetails(
                        name=file['name'],
                        psd_path=file['paths']['PSD'],
                        export_path=file['paths']['Export'],
                        google_drive_path=file['paths']['Google Drive'],
                        layer_path=file['layer_path'],
                        supported_artboards=file['artboards']['boards']
                    ) for file in files_data] if files_data else []
            new_client = Client(name=name.lower(), files=files)
            self.file_service.add_client(new_client)
            show_success_message(f"Client '{name}' added.")

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
