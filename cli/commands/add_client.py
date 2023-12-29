import typer
from app.controllers.client_controller import ClientController

def add_client(name: str, file_name: str = typer.Option(None, help="Name of the file."), 
               psd_path: str = typer.Option(None, help="Full path to the client's PSD file."), 
               export_path: str = typer.Option(None, help="Path where exported files will be saved."), 
               google_drive_path: str = typer.Option(None, help="Google Drive path for the file."), 
               layer_path: str = typer.Option(None, help="Path to the target text layer within the Photoshop file using regex."), 
               supported_artboards: str = typer.Option(None, help="Comma-separated names of the artboards to be processed.")):
    """
    Adds a new client with specific Photoshop file settings to Photomater.
    """
    client_controller = ClientController()
    files_data = []

    if file_name and psd_path and export_path and google_drive_path and layer_path and supported_artboards:
        file_data = {
            'name': file_name,
            'paths': {
                'PSD': psd_path,
                'Export': export_path,
                'Google Drive': google_drive_path
            },
            'layer_path': layer_path,
            'artboards': {
                'boards': supported_artboards.split(',')
            }
        }
        files_data.append(file_data)

    client_controller.add_client(name, files_data if files_data else None)

    if files_data:
        typer.echo(f"Client '{name}' with file '{file_name}' added successfully.")
    else:
        typer.echo(f"Client '{name}' added successfully.")

if __name__ == "__main__":
    typer.run(add_client)
