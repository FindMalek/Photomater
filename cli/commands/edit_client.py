import typer
from app.controllers.client_controller import ClientController

def edit_client(name: str = typer.Option(..., prompt=True, help="Name of the client."),
                new_name: str = None,
                new_file_location: str = None,
                new_export_location: str = None,
                new_artboards: str = None,
                new_layer_path: str = None):
    """
    Edits an existing client's details.
    """
    client_controller = ClientController()
    client_controller.edit_client(name, new_name, new_file_location, new_export_location, new_artboards, new_layer_path)
    typer.echo(f"Client '{name}' has been updated.")

if __name__ == "__main__":
    typer.run(edit_client)
