# Photomater

Photomater is a Python-based automation tool designed to streamline the process of updating text layers in Adobe Photoshop files. This tool is now enhanced with a rich command-line interface (CLI), making it even more user-friendly and efficient for graphic designers.

## Features

- Automated updating of text layers in Photoshop files, tailored for weekly dates.
- Ability to handle multiple files and artboards, customizable for different clients and date formats.
- A rich CLI for easy interaction, supporting various commands for managing client data and automation tasks.
- Extendable architecture, allowing for additional Photoshop automation functionalities.

## Getting Started

These instructions will guide you in setting up and using Photomater on your local machine.

### Prerequisites

- Adobe Photoshop (with scripting support).
- Python 3.x.
- Basic understanding of Python and JavaScript (for Adobe Photoshop scripting).

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/FindMalek/Photomater.git
cd photomater
```

Install any necessary Python dependencies:
```bash
pip install -r requirements.txt
```

### Setting Up

1. **Initial Configuration:**
Run python main.py to start the CLI. If the data/client_data.json file is empty or does not exist, the CLI will guide you through adding a new client with file paths and configurations.

2. **Managing Clients:**
You can add, edit, and remove client data using the CLI commands. The data is stored in `data/client_data.json`.

3. **Using the CLI:**
Photomater's CLI allows you to perform various actions, such as updating text layers, exporting artboards, and managing client data. Use the help command for guidance:
```bash
python main.py --help
```

### CLI Commands
Photomater's CLI offers a variety of commands to manage client data, update Photoshop files, and export artboards. Here's a detailed overview of each command and its arguments:

#### 1. Add Client
Add a new client with their specific Photoshop file settings.
* Command: `add-client`
* Arguments:
   * `--name` (required): Name of the client.
   * `--file_location` (required): Full path to the client's PSD file.
   * `--export_location` (required): Path where exported files will be saved.
   * `--artboards` (required): Comma-separated names of the artboards to be processed.
   * `--layer_path` (required): Path to the target text layer within the Photoshop file.
```bash
python main.py add-client --name "Client1" --file_location "/path/to/psd" --export_location "/path/to/export" --artboards "Artboard1,Artboard2" --layer_path "path/to/layer"
```

#### 2. Edit Client
Edit an existing client's details.
* Command: `edit-client`
* Arguments:
   * `--name` (required): Name of the client.
   * `--new_name` (optional): New name for the client.
   * `--new_file_location`  (optional): New file location path.
   * `--new_export_location` (optional): New export location path.
   * `--new_artboards` (optional): New artboard names, comma-separated.
   * `--new_layer_path` (optional): New layer path.
```bash
python main.py edit-client --name "Client1" --new_name "Client1Updated" --new_file_location "/new/path/to/psd"
```
#### 3. Remove Client
Remove an existing client from the system.
* Command: `remove-client`
* Arguments:
   * `--name` (required):  Name of the client to be removed.
```bash
python main.py remove-client --name "Client1"
```
#### 4. List Clients
List all clients currently stored in the system.
* Command: `list-client`
* No arguments required.
```bash
python main.py list-clients
```
#### 5. Update and Export
Update text layers in Photoshop files and optionally export artboards.
* Command: `update`
* Arguments:
   * `--client` (required): Name of the client.
   * `--all_files` (optional): Flag to process all files for the client.
   * `--file` (optional): Specify a single file name to process.
   * `--save` (optional): Flag to save changes to the PSD file.
   * `--export` (optional): Flag to export artboards after updating.
```bash
python main.py update --client "Client1" --all-files --export
```
Or for a specific file:
```bash
python main.py update --client "Client1" --file "FileName" --save
```
These commands provide a comprehensive interface for managing and automating tasks in Photoshop files, making Photomater a powerful tool for graphic designers.


### Project Structure
The project is organized into several directories:

```
photoshop_automation/
│
├── app/                            # Main application code
│   ├── controllers/                # Controllers for handling business logic
│   │   ├── photoshop_controller.py # Logic for interacting with Photoshop
│   │   └── client_controller.py    # Logic for managing client data
│   │
│   ├── models/                     # Data models
│   │   ├── client_model.py         # Model for client data
│   │   └── layer_model.py          # Model for layer paths and related data
│   │
│   ├── services/                   # Services for specific tasks
│   │   └── file_service.py         # File handling, read/write JSON, etc.
│   │
│   └── utils/                      # Utility functions and constants
│       ├── constants.py            # Constants used across the application
│       └── cli_utils.py            # Utilities for CLI styling and interaction
│
├── data/                           # Data storage
│   └── client_data.json            # Client data storage in JSON format
│
├── cli/                            # CLI-related code
│   ├── commands/                   # Individual CLI commands
│   │   ├── add_client.py           # Command for adding a new client
│   │   ├── edit_client.py          # Command for editing client details
│   │   ├── remove_client.py        # Command for removing a client
│   │   └── list_clients.py         # Command for listing all clients
│   │
│   └── main_cli.py                 # Entry point for the CLI application
│
├── scripts/                        # JavaScript scripts for Photoshop
│   └── updateText.jsx              # Example Photoshop script
│
├── main.py                         # Main script to run the application
├── README.md                       # Documentation for the project
└── requirements.txt                # Python dependencies
```

* **`/app`** - Core application code, including controllers for business logic and models for data structures.
* **`/cli`** - CLI-related code, housing individual commands and the main CLI application.
* **`/data`** - Data storage, including the JSON file for client data.
* **`/scripts`** - JavaScript scripts for Photoshop.
* **`main.py`** - Main script to run the CLI application.
* **`requirements.txt`** -  Required Python dependencies.

### Usage
Photomater can be used through its rich CLI. Here are some example commands:

* **Add a new client:**
```bash
python main.py add-client --name "Client1" --file_location "/path/to/psd" --export_location "/path/to/export" --artboards "Artboard1,Artboard2" --layer_path "path/to/layer"
```
* **Update text layers and export artboards:**
```bash
python main.py --client "Client1" --all-files --export
```
* **Update text layers in a specific file:**
```bash
python main.py --client "Client1" --file "FileName" --save
```

For more detailed information on each command, use the `--help` flag.