import typer

from app.services.file_service import FileService
from app.controllers.photoshop_controller import PhotoshopController

from app.utils.artboard_support import supports_artboards
from app.utils.cli_utils import (
    show_error_message, 
    show_success_message, 
    show_info_message, 
    show_update_details
)

def export_file(client: str = typer.Option(..., prompt=True, help="Name of the client."),
                all_files: bool = typer.Option(False, help="Update all files for the client."),
                file: str = typer.Option(None, help="Name of the file to be updated.")):
    """
    Update text layers in Photoshop file, and then saves and exports the Photoshop file.
    """
    file_service = FileService()
    photoshop_controller = PhotoshopController()

    client_data = file_service.get_client(client)
    if not client_data:
        show_error_message(f"No client found with name '{client}'.")
        raise typer.Exit(code=1)
    
    if all_files:
        show_info_message(f"Exporting all files for client '{client}' ...")
        client_files = file_service.get_client_files(client)

        for file in client_files:
            file_data = file_service.get_client_file(client, file['name'])
            artboards_supported = supports_artboards(file_data)

            if artboards_supported:
                show_info_message(f"Exporting all artboards in file '{file['name']}' for client '{client}' ...")
                show_update_details(client, file_data["name"], file_data['path_object']['Layers']['Path'], file_data['artboards'])

                outcome = photoshop_controller.update_type_artboard(file_data, "export")
                if outcome:
                    show_success_message(f"All artboards in file '{file_data['name']}' updated and exported successfully.")
                else:
                    show_error_message(f"File '{file_data['name']}' could not be updated.")

            else:
                show_info_message(f"Exporting a single layer in file '{file['name']}' for client '{client}' ...")
                show_update_details(client, file_data["name"], file_data['path_object'])

                outcome = photoshop_controller.update_type_layer(file_data, "export")
                if outcome:
                    show_success_message(f"Layer in file '{file_data['name']}' updated and exported successfully.")
                else:
                    show_error_message(f"File '{file_data['name']}' could not be updated.")

    elif file:
        file_data = file_service.get_client_file(client, file)
        artboards_supported = supports_artboards(file_data)

        if artboards_supported:
            show_info_message(f"Exporting all artboards in file '{file}' for client '{client}' ...")
            show_update_details(client, file_data["name"], file_data['path_object']['Layers']['Path'], file_data['artboards'])

            outcome = photoshop_controller.update_type_artboard(file_data, "export")
            if outcome:
                show_success_message(f"All artboards in file '{file_data['name']}' updated and exported successfully.")
            else:
                show_error_message(f"File '{file_data['name']}' could not be updated.")

        else:
            show_info_message(f"Exporting a single layer in file '{file}' for client '{client}' ...")
            show_update_details(client, file_data["name"], file_data['path_object'])

            outcome = photoshop_controller.update_type_layer(file_data, "export")
            if outcome:
                show_success_message(f"Layer in file '{file_data['name']}' updated and exported successfully.")
            else:
                show_error_message(f"File '{file_data['name']}' could not be updated.")

    else:
        show_error_message("Please specify either '--all-files' or '--file' argument.")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    typer.run(export_file)