# **Photomater**

Photomater is a Python-based automation tool designed to streamline the process of updating text layers in Adobe Photoshop files. This tool is now enhanced with a rich command-line interface (CLI), making it even more user-friendly and efficient for graphic designers.

## **Features**

- Automated updating of text layers in Photoshop files, tailored for weekly dates.
- Ability to handle multiple files and artboards, customizable for different clients and date formats.
- A rich CLI for easy interaction, supporting various commands for managing client data and automation tasks.
- Extendable architecture, allowing for additional Photoshop automation functionalities.

## **Getting Started**

These instructions will guide you in setting up and using Photomater on your local machine.

### **Prerequisites**

- Adobe Photoshop (with scripting support).
- Python 3.x.
- Basic understanding of Python and JavaScript (for Adobe Photoshop scripting).

### **Installation**

Clone the repository to your local machine:

```bash
git clone https://github.com/FindMalek/Photomater.git
cd photomater
```

Install any necessary Python dependencies:
```bash
pip install -r requirements.txt
```

### **Setting Up**

1. **Initial Configuration:**
Run python main.py to start the CLI. If the data/client_data.json file is empty or does not exist, the CLI will guide you through adding a new client with file paths and configurations.

2. **Managing Clients:**
You can add, edit, and remove client data using the CLI commands. The data is stored in `data/client_data.json`.

3. **Using the CLI:**
Photomater's CLI allows you to perform various actions, such as updating text layers, exporting artboards, and managing client data. Use the help command for guidance:
```bash
python main.py --help
```

### **CLI Commands**
Photomater's CLI offers a variety of commands to manage client data, update Photoshop files, and export artboards. Here's a detailed overview of each command and its arguments:

#### 1. Add Client
Add a new client with their specific Photoshop file settings.
* Command: `add-client`
* Base Arguments:
   * `--name` (required): Name of the client.
* Arguments:
   * `--file-name`: Name of the file.
   * `--psd-path`: Full path to the client's PSD file.
   * `--export-path`: Path where exported files will be saved.
   * `--google-drive-path`: Google Drive path for the file.
   * `--start-date-path`: Path to the start date text layer within the Photoshop file.
   * `--end-date-path`: Path to the end date text layer within the Photoshop file.
   * `--supported-artboards`: Comma-separated names of the artboards to be processed.

**Adding a Client Without Files**
```bash
python main.py add-client --name "CLIENT_NAME"
```

**Adding a Client With File Details**
```bash
python main.py add-client --name "CLIENT_NAME" --file-name "FILE_NAME" --psd-path "/path/to/psd" --export-path "/path/to/export" --google-drive-path "/path/to/drive" --start-date-path "folder/text_layer" --end-date-path "folder/text_layer" --supported-artboards "Artboard1,Artboard2" --layer-path "Date - * (EditText)"
```

#### 2. Edit Client
Edit an existing client's details.
* Command: `edit-client`
* Arguments:
   * `--name` (required): Name of the client.
   * `--new_name` (optional): New name for the client.
   * `--new_file_location`  (optional): New file location path.
   * `--new_export_location` (optional): New export location path.
   * `--new_google_drive_location` (optional): New Google Drive path for the file.
   * `--new_start_date_path ` (optional): New path for the start date text layer.
   * `--new_end_date_path ` (optional): New path for the end date text layer.
   * `--new_supported_artboards ` (optional): New artboard names, comma-separated.
```bash
python main.py edit-client --name "CLIENT_NAME" --new_name "NEW_CLIENT_NAME" --new_file_location "/new/path/to/psd"
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

#### 5. Update File
Update text layers in Photoshop file, and then saves the Photoshop file.
* Command: `update`
* Arguments:
   * `--client` (required): Name of the client.
   * `--all-files` (optional): Flag to process all files for the client.
   * `--file` (optional): Specify a single file name to process.
```bash
python main.py update --client "Client1" --file "FileName"
```

#### 6. Export File
Update text layers in Photoshop file, and then saves and exports the Photoshop file.
* Command: `export`
* Arguments:
   * `--client` (required): Name of the client.
   * `--all-files` (optional): Flag to process all files for the client.
   * `--file` (optional): Specify a single file name to process.
```bash
python main.py export --client "Client1" --all-files
```

These commands provide a comprehensive interface for managing and automating tasks in Photoshop files, making Photomater a powerful tool for graphic designers. For more detailed information on each command, use the `--help` flag.

### **Client Data Structure**
Photomater manages client data with a comprehensive structure to accommodate various project requirements and workflows. Here is an overview of the client data structure:

#### Client Object
Each client object consists of a name and a list of files associated with that client.

   * `name`: The name of the client.
   * `files`: An array of File objects.

#### File Object
Each file object within a client includes detailed information about the file, paths, artboards, and the text layers to be updated.

- `name`: The name of the file or project.
- `paths`: An object containing paths related to the file.
  - `PSD`: The full path to the Photoshop (.psd) file.
  - `Export`: Path where exported files will be saved.
  - `Google Drive`: Google Drive path for the file.
- `path_object`: An object detailing the paths to the text layers.
  - `Main`: Contains paths to the main date-related text layers.
    - `start`: Path to the start date text layer.
    - `end`: Path to the end date text layer.
  - `Layers`: Contains information about additional layer paths.
    - `Supported`: Boolean indicating if additional layers are supported.
    - `Path`: The path to additional text layers, typically involving artboard names.
- `artboards`: Information about the artboards to be processed.
  - `Supported`: Boolean indicating if artboards are supported.
  - `Boards`: A list of the names of the artboards to be processed.

#### Example
Here is an example of a client data structure:
```json
{
    "name": "MoveU",
    "files": [
        {
            "name": "Daily Plan",
            "paths": {
                "PSD": "/path/to/project1.psd",
                "Export": "/path/to/export/project1",
                "Google Drive": "https://drive.google.com/drive/folders/project1"
            },
            "path_object": {
                "Main": {
                    "start": "Main/Text/Week Date/Start Date (EditText)",
                    "end": "Main/Text/Week Date/End Date (EditText)"
                },
                "Layers": {
                    "Supported": true,
                    "Path": "Main/Text/Week Date/Date - * (EditText)"
                }
            },
            "artboards": {
                "Supported": true,
                "Boards": ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
            }
        },
        {
            "name": "Weekly Plan",
            "paths": {
                "PSD": "/path/to/project2.psd",
                "Export": "/path/to/export/project2",
                "Google Drive": "https://drive.google.com/drive/folders/project2"
            },
            "path_object": {
                "Main": {
                    "start": "Main/Text/Week Date/Start Date (EditText)",
                    "end": "Main/Text/Week Date/End Date (EditText)"
                },
                "Layers": {
                    "Supported": false,
                    "Path": ""
                }
            },
            "artboards": {
                "Supported": false,
                "Boards": []
            }
        }
    ]
}
```
This structure provides flexibility for managing different types of projects and their specific requirements. It is crucial to maintain this format for the application to function correctly.



### **Project Structure**
The project is organized into several directories:

```
Photomater/
│
├── app/                            # Main application code
│   ├── controllers/                # Controllers for handling business logic
│   │   ├── photoshop_controller.py # Logic for interacting with Photoshop
│   │   └── client_controller.py    # Logic for managing client data
│   │
│   ├── models/                     # Data models
│   │   ├── client_model.py         # Model for client data
│   │   ├── file_model.py           # Model for file data
│   │   └── layer_model.py          # Model for layer paths and related data
│   │
│   ├── services/                   # Services for specific tasks
│   │   ├── date_service.py         # File handling all of the date specifications
│   │   └── file_service.py         # File handling, read/write JSON, etc.
│   │
│   └── utils/                      # Utility functions and constants
│       ├── artboard_support.py     # Utilities for the artboards supported by a given file
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
│   │   ├── list_clients.py         # Command for listing all clients
│   │   ├── update_file.py          # Command for saving the PSD and output files
│   │   └── export_file.py          # Command for saving & exporting the PSD and output files
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