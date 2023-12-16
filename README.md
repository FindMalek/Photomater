# Photomater

Photomater is a Python-based automation tool designed to streamline the process of updating text layers in Adobe Photoshop files. This tool is specifically tailored for graphic designers who need to routinely update date information in Photoshop templates.

## Features

- Automated updating of 'Week Date' layers in Photoshop files.
- Capability to handle multiple files and artboards.
- Customizable for different clients and date formats.
- Extendable to various other Photoshop automation tasks.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Adobe Photoshop (with scripting support)
- Python 3.x
- Basic understanding of Python and JavaScript (for Adobe Photoshop scripting)

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/FindMalek/Photomater.git
cd photomater
```

Install any necessary Python dependencies

```bash
pip install -r requirements.txt
```

### Setting Up

1. **Initial Configuration**:

   - Run `python main.py`. If the `data/client_data.json` file is empty or does not exist, the program will prompt you to enter the paths to your Photoshop files.

2. **Entering File Paths**:

   - When prompted, input the full paths to your Photoshop files. These paths will be stored in `data/client_data.json` for future automation runs.

3. **Automated Detection**:

   - On subsequent runs, Photomater will automatically check `data/client_data.json` for the file paths. If the paths are present, it will proceed with the automation process. If not, it will prompt you again for the file paths.

4. **Editing File Paths**:
   - You can manually edit `data/client_data.json` at any time to update or change the stored Photoshop file paths.

### Usage

Run the main script to start the automation process:

```bash
python main.py
```

Follow any on-screen prompts or configure the script to run without manual inputs.

### Structure

The project follows an MVC-like structure:

- `/app` - Application code including controllers and models.
- `/data` - Data files and configurations.
- `/scripts` - JavaScript scripts for Photoshop.
- `requirements.txt` - The necessary Python dependencies.
- `main.py` - Entry point of the automation tool.
