import typer
from app.controllers.client_controller import ClientController

def add_client(name: str = typer.Option(..., prompt=True, help="Name of the client."),
               file_name: str = typer.Option(None, help="Name of the file."), 
               psd_path: str = typer.Option(None, help="Full path to the client's PSD file."), 
               export_path: str = typer.Option(None, help="Path where exported files will be saved."), 
               google_drive_path: str = typer.Option(None, help="Google Drive path for the file."), 
               layer_path: str = typer.Option(None, help="Path to the text layer."),
               start_date_path: str = typer.Option(None, help="Path to the start date text layer."),
               end_date_path: str = typer.Option(None, help="Path to the end date text layer."),
               supported_artboards: str = typer.Option(None, help="Comma-separated names of the artboards to be processed.")):
    """
    Adds a new client with specific Photoshop file settings to Photomater.
    """
    client_controller = ClientController()
    files_data = []

    if file_name and psd_path and export_path and google_drive_path:
        path_object = {
            'Main': {
                'start': start_date_path,
                'end': end_date_path
            },
            'Layers': {
                'Supported': bool(supported_artboards),
                'Path': "" if not supported_artboards else layer_path
            }
        }

        file_data = {
            'name': file_name,
            'paths': {
                'PSD': psd_path,
                'Export': export_path,
                'Google Drive': google_drive_path
            },
            'path_object': path_object,
            'artboards': {
                'Boards': supported_artboards.split(',') if supported_artboards else []
            }
        }
        files_data.append(file_data)

    client_controller.add_client(name, files_data if files_data else None)

if __name__ == "__main__":
    typer.run(add_client)
