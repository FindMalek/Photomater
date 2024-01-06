import json
from app.models.client_model import Client

class FileService:
    def __init__(self):
        self.file_path = 'data/client_data.json'

    def read_json_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_json_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def client_to_dict(self, client: Client, update=False):
        if update:
            return {
                "name": client.name,
                "files": [
                    {
                        "name": file_data.get('name', ''),
                        "paths": file_data.get('paths', {}),
                        "layer_path": file_data.get('layer_path', ''),
                        "artboards": file_data.get('artboards', {})
                    } for file_data in client.files
                ]
            }
        return {
            "name": client.name,
            "files": [
                {
                    "name": file.name,
                    "paths": file.paths,
                    "layer_path": file.layer_path,
                    "artboards": file.artboards
                } for file in client.files
            ]
        }
    
    def add_client(self, client: Client):
        clients = self.read_json_file()
        client_dict = self.client_to_dict(client)
        clients.append(client_dict)
        self.write_json_file(clients)

    def edit_client(self, name, updated_data):
        clients = self.read_json_file()
        for client in clients:
            if client['name'] == name:
                client.update(updated_data)
                break
        self.write_json_file(clients)

    def update_client(self, updated_client: Client):
        clients = self.read_json_file()
        client_dict = self.client_to_dict(updated_client, update=True)

        for client in clients:
            if client['name'] == updated_client.name:
                client.update(client_dict)
                break
        self.write_json_file(clients)

    def remove_client(self, name):
        clients = self.read_json_file()
        clients = [client for client in clients if client['name'] != name]
        self.write_json_file(clients)

    def get_client(self, name):
        clients = self.read_json_file()
        client_found = next((client for client in clients if client['name'].lower() == name.lower()), None)
        return client_found

    def get_all_clients(self):
        return self.read_json_file()
    
    def get_client_file(self, name, file_name):
        client = self.get_client(name)
        if client:
            files = client['files']
            file_found = next((file for file in files if file['name'].lower() == file_name.lower()), None)
            return file_found
        return None
    
    def get_client_files(self, name):
        client = self.get_client(name)
        return client['files'] if client else None