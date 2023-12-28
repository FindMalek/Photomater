import typer
from app.controllers.client_controller import ClientController

def remove_client(name: str):
    """
    Removes an existing client from the system.
    """
    client_controller = ClientController()
    client_controller.remove_client(name)
    typer.echo(f"Client '{name}' removed successfully.")

if __name__ == "__main__":
    typer.run(remove_client)
