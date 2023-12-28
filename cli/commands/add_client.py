import typer
from app.controllers.client_controller import ClientController

def add_client(name: str, file_location: str, export_location: str, artboards: str, layer_path: str):
    """
    Adds a new client with their specific Photoshop file settings.
    """
    client_controller = ClientController()
    client_controller.add_client(name, file_location, export_location, artboards, layer_path)
    typer.echo(f"Client '{name}' added successfully.")

if __name__ == "__main__":
    typer.run(add_client)
