import typer
from app.controllers.photoshop_controller import PhotoshopController

def update(client: str, all_files: bool = False, file: str = None, save: bool = False, export: bool = False):
    """
    Update text layers in Photoshop files and optionally export artboards.
    """
    photoshop_controller = PhotoshopController()
    # Add logic to update text layers and export artboards based on the arguments
    # This is a placeholder for the actual implementation
    typer.echo(f"Updated files for client '{client}'.")

if __name__ == "__main__":
    typer.run(update)
