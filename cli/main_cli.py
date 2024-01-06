import typer
from cli.commands.add_client import add_client
from cli.commands.edit_client import edit_client
from cli.commands.remove_client import remove_client
from cli.commands.list_clients import list_clients
from cli.commands.update_file import update_file
from cli.commands.export_file import export_file

app = typer.Typer()

app.command()(add_client)
app.command()(edit_client)
app.command()(remove_client)
app.command()(list_clients)
app.command()(update_file)
app.command()(export_file)


if __name__ == "__main__":
    app()
