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

    def client_to_dict(self, client: Client):
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

    def remove_client(self, name):
        clients = self.read_json_file()
        clients = [client for client in clients if client['name'] != name]
        self.write_json_file(clients)

    def get_all_clients(self):
        return self.read_json_file()