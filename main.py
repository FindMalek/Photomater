import typer
import sys
from cli.main_cli import app as cli_app

def main():
    """
    Entry point for the Photomater application.
    """
    if len(sys.argv) > 1:
        cli_app()

    else:
        typer.echo("Welcome to Photomater!")
        typer.echo("A Python-based automation tool for updating text layers in Adobe Photoshop files.")
        typer.echo("Use --help to see available commands or execute a command directly.")

        # Displaying an interactive menu or additional help can be implemented here
        # For now, we'll just show the help for the Typer app
        typer.echo("\n")
        typer.echo("Available commands:")
        typer.echo("\n")
        # typer.echo(cli_app.get_help())

if __name__ == "__main__":
    main()
