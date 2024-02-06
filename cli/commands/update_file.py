import typer
from app.controllers.photoshop_controller import PhotoshopController

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
        week_date = DateService.get_week_date()

        if artboards_supported:
            show_info_message(f"Updating all artboards in file '{file}' for client '{client}' ...")
            show_update_details(client, file_data["name"], file_data['path_object']['Layers']['Path'], file_data['artboards'])
            # @TODO: Add logic to update a single layer in each specified artboard

            outcome = photoshop_controller.update_text_artboard(file_data, week_date)
            if outcome:
                show_success_message(f"All artboards in file '{file_data['name']}' updated successfully.")
            else:
                show_error_message(f"File '{file_data['name']}' could not be updated.")

        else:
            show_info_message(f"Updating a single layer in file '{file}' for client '{client}' ...")
            show_update_details(client, file_data["name"], file_data['path_object'])

            outcome = photoshop_controller.update_weekdate_layers(file_data, week_date)
            if outcome:
                show_success_message(f"Layer in file '{file_data['name']}' updated successfully.")
            else:
                show_error_message(f"File '{file_data['name']}' could not be updated.")

    else:
        show_error_message("Please specify either '--all-files' or '--file' argument.")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    typer.run(update_file)