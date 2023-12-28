import typer
from cli.commands.add_client import add_client
from cli.commands.edit_client import edit_client
from cli.commands.remove_client import remove_client
from cli.commands.list_clients import list_clients

app = typer.Typer()

app.command()(add_client)
app.command()(edit_client)
app.command()(remove_client)
app.command()(list_clients)

if __name__ == "__main__":
    app()
