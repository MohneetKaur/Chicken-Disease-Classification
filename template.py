import os # os module provides functions for interacting with the operating system
from pathlib import Path # Path class from the pathlib module represents a file or directory path
import logging # logging module is used for logging messages


# logging.basicConfig() function is called to configure the logging module. It sets the logging level to INFO and defines the format of the log messages.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# variable project_name is assigned the value "cnnClassifier"
project_name = "cnnClassifier"


# The list_of_files is a list of file paths that need to be created. Each path is a string specifying the file or directory location relative to the current directory
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # constructor
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]


# loop iterates over each file path in the list_of_files
for filepath in list_of_files:
    filepath = Path(filepath) # file path is converted to a Path object using Path(filepath)
    filedir, filename = os.path.split(filepath) # separate the file path into directory and filename. The filedir variable contains the directory part, and the filename variable contains the filename.


    if filedir !="": # If the filedir is not an empty string, it means the file is located in a directory (not in the current directory)
        os.makedirs(filedir, exist_ok=True) # os.makedirs() function is called to create the directory if it doesn't already exist. The exist_ok=True parameter ensures that the function does not raise an error if the directory already exists
        logging.info(f"Creating directory; {filedir} for the file: {filename}") # A log message is generated using the logging.info() function to indicate the creation of the directory.


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # hecks if the file does not exist or if its size is zero (indicating an empty file)
        with open(filepath, "w") as f: # If either condition is true, a new file is created using the open(filepath, "w")
            pass # The file is opened in write mode ("w") and immediately closed without writing anything (pass statement inside the with block)
            logging.info(f"Creating empty file: {filepath}") # A log message is generated to indicate the creation of an empty file


    else:
        logging.info(f"{filename} is already exists") # If the file already exists and is not empty, a log message is generated to indicate that the file already exists


# To create all these files run 'python template.py' in Git Bash

# Then to push all these files to GitHub: type in Git Bash
# Step 1: git add .
# Step 2: git commit -m "folder structure added"
# Step 3: git push origin main
