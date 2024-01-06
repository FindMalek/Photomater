import typer
from app.controllers.photoshop_controller import PhotoshopController

def export_file(name: str = typer.Option(..., prompt=True, help="Name of the client."),
                all_files: bool = typer.Option(False, help="Update all files for the client."),
                file: str = typer.Option(None, help="Name of the file to be updated.")):
    """
    Update text layers in Photoshop file, and then saves and exports the Photoshop file.
    """
    photoshop_controller = PhotoshopController()
    # Add logic to update text layers and export artboards based on the arguments
    # This is a placeholder for the actual implementation
    typer.echo(f"Updated & saved the files for client '{name}'.")

if __name__ == "__main__":
    typer.run(export_file)
