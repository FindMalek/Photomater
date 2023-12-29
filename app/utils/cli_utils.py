from rich.console import Console
from rich.table import Table
from rich import print as rich_print

console = Console()

def show_success_message(message: str):
    """Displays a success message."""
    console.print(f":white_check_mark: [bold green]{message}[/]")

def show_error_message(message: str):
    """Displays an error message."""
    console.print(f":x: [bold red]{message}[/]")

def show_warning_message(message: str):
    """Displays a warning message."""
    console.print(f":warning: [bold yellow]{message}[/]")

def show_info_message(message: str):
    """Displays an informational message."""
    console.print(f":information_source: [bold blue]{message}[/]")

def display_clients_table(clients):
    """Displays a table of clients."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim")
    table.add_column("Files", style="dim")
    
    for client in clients:
        files = ', '.join([f['name'] for f in client['files']])
        table.add_row(client['name'], files)

    console.print(table)

# You can add more utility functions as needed
