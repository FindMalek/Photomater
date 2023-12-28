import typer
from app.controllers.client_controller import ClientController

def list_clients():
    """
    Lists all clients currently stored in the system.
    """
    client_controller = ClientController()
    clients = client_controller.list_clients()
    for client in clients:
        typer.echo(f"Name: {client['name']}, File Location: {client['file_location']}, Export Location: {client['export_location']}, Artboards: {client['artboards']}, Layer Path: {client['layer_path']}")

if __name__ == "__main__":
    typer.run(list_clients)
