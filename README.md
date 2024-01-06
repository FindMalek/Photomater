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
   * `--layer-path`: Path to the target text layer within the Photoshop file using regex.
   * `--supported-artboards`: Comma-separated names of the artboards to be processed.

**Adding a Client Without Files**
```bash
python main.py add-client "Client1"
```
**Adding a Client Without Files**
```bash
python main.py add-client "Client1" --file-name "File1" --psd-path "/path/to/psd1" --export-path "/path/to/export1" --google-drive-path "/path/to/drive1" --layer-path "Date - (Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche) (EditText)" --supported-artboards "Artboard1,Artboard2"
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
Each file object within a client includes detailed information about the file, paths, artboards, and the text layer to be updated.

   * `name`: The name of the file or project.
   * `paths`: An object containing paths related to the file.
      * `PSD`: The full path to the Photoshop (.psd) file.
      * `Export`: A list of the names of the artboards to be processed.
      * `Google Drive`: A list of the names of the artboards to be processed.
   * `layer_path`: The regular expression `Date - (Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche) (EditText)` is used. This regex will match strings like `Date - Lundi (EditText)`, `Date - Mardi (EditText)`, etc., where the day of the week is one of the specified artboard names.
   * `artboards`: A list of the names of the artboards to be processed.
      * `Supported`: A list of the names of the artboards to be processed.
      * `boards`: A list of the names of the artboards to be processed.

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
            "layer_path": "Date - (Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche) (EditText)",
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
            "layer_path": "Date - Weekly (EditText)",
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
│   │   └── layer_model.py          # Model for layer paths and related data
│   │
│   ├── services/                   # Services for specific tasks
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