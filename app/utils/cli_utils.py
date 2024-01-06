from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def show_success_message(message: str):
    """Displays a success message."""
    console.print(Panel(f"[bold green]:white_check_mark:  Success[/]: {message}", border_style="green", box=box.ROUNDED))

def show_error_message(message: str):
    """Displays an error message."""
    console.print(Panel(f"[bold red]:x:  Error[/]: {message}", border_style="red", box=box.ROUNDED))

def show_warning_message(message: str):
    """Displays a warning message."""
    console.print(Panel(f"[bold yellow]:warning:  Warning[/]: {message}", border_style="yellow", box=box.ROUNDED))

def show_info_message(message: str):
    """Displays an informational message."""
    console.print(Panel(f"[bold blue]:information_source:  Info[/]: {message}", border_style="blue", box=box.ROUNDED))

def display_clients_table(clients):
    """Displays a table of clients."""
    table = Table(show_header=True, header_style="bold magenta", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("Name", style="dim")
    table.add_column("Files", style="dim")

    for client in clients:
        files = ', '.join([f['name'] for f in client['files']])
        table.add_row(client['name'], files)

    console.print(table)

def show_update_details(client_name: str, file_name: str, layer_path: str, artboards=None):
    """Displays detailed update information in a formatted panel."""
    details_text = Text()

    details_text.append("Client: ", style="bold blue")
    details_text.append(client_name + "\n", style="bold")
    details_text.append("File: ", style="bold blue")
    details_text.append(file_name + "\n", style="bold")

    if artboards and artboards['Supported']:
        details_text.append("Artboards to be updated: ", style="bold blue")
        details_text.append(', '.join(artboards['Boards']) + "\n", style="bold")
    else:
        details_text.append("Layer to be updated: ", style="bold blue")
        details_text.append(layer_path + "\n", style="bold")

    console.print(Panel(details_text, title="[bold blue]Update Details[/]", border_style="blue", box=box.ROUNDED))
