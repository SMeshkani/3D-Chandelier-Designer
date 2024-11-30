# 3D Chandelier Designer

## Description
A Python-based tool for designing and generating 3D chandeliers with STL output and AutoCAD integration. The project includes a GUI application for interactive customization and an AutoCAD LISP script for real-time visualization.

## Features
- Generate 3D chandelier STL files based on user-defined parameters.
- Intuitive GUI for easy parameter entry.
- AutoCAD LISP script to visualize chandelier bulbs directly in AutoCAD.

## How to Use

### Python Scripts
1. **Wave Creator.py**:
   - A GUI tool for generating STL files.
   - Run the script:
     ```bash
     python "Wave Creator.py"
     ```
   - Enter the parameters for the chandelier (bulb quantity, spacing, diameter, height) in the GUI and save the STL file.

2. **create_exe.py**:
   - A helper script to package `Wave Creator.py` into a standalone `.exe` file.
   - Run the script:
     ```bash
     python create_exe.py
     ```
   - The `.exe` file will be generated in the `dist` folder.

### AutoCAD LISP Script
1. **ChandelierBulbs.lsp**:
   - Load the LISP script in AutoCAD using the `APPLOAD` command.
   - Type `ChandelierBulbs` in the command line to run the routine.
   - Follow the prompts to enter parameters and generate spheres in the AutoCAD model.

## Requirements
- **Python 3.7+**
- Libraries:
  - `numpy`
  - `numpy-stl`
  - `tkinter` (comes pre-installed with Python)
- AutoCAD for running the LISP script.

## Installation
1. Clone the repository or download the ZIP file.
2. Install required Python libraries:
   ```bash
   pip install numpy numpy-stl
