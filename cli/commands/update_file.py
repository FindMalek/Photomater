import typer
from app.controllers.photoshop_controller import PhotoshopController
from app.controllers.client_controller import ClientController

from app.services.file_service import FileService
from app.services.date_service import DateService

from app.utils.artboard_support import supports_artboards
from app.utils.cli_utils import (
    show_error_message, 
    show_success_message, 
    show_info_message, 
    show_update_details
)

def update_file(client: str = typer.Option(..., prompt=True, help="Name of the client."),
                all_files: bool = typer.Option(False, "--all-files", help="Update all files for the client."),
                file: str = typer.Option(None, "--file", help="Name of the file to be updated.")):

    file_service = FileService()

    photoshop_controller = PhotoshopController()
    client_controller = ClientController()

    client_data = file_service.get_client(client)
    if not client_data:
        show_error_message(f"No client found with name '{client}'.")
        raise typer.Exit(code=1)

    if all_files:
        # @TODO: Add logic to update all files for the specified client 
        show_info_message(f"Updating all files for client '{client}' ...")

    elif file:
        file_data = file_service.get_client_file(client, file)
        artboards_supported = supports_artboards(file_data)

        if artboards_supported:
            show_info_message(f"Updating all artboards in file '{file}' for client '{client}' ...")
            show_update_details(client, file_data["name"], file_data['path_object']['Layers']['Path'], file_data['artboards'])
            # @TODO: Add logic to update all artboards in the file
        else:
            show_info_message(f"Updating a single layer in file '{file}' for client '{client}' ...")
            show_update_details(client, file_data["name"], file_data['path_object'])

            # @TODO: Add logic to update a single layer in the file
            week_date = DateService.get_week_date()
            client_controller.update_single_layer(file_data, week_date)

        # Placeholder for actual Photoshop update logic
    else:
        show_error_message("Please specify either '--all-files' or '--file' argument.")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    typer.run(update_file)
