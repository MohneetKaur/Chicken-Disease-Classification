import os
from box.exceptions import BoxValueError # This exception is raised when there is an issue with the value of a Box object.
import yaml
from cnnClassifier import logger # imports the logger object from the cnnClassifier
import json # provides functions for working with JSON data.
import joblib # provides tools for saving and loading Python objects in binary format.
from ensure import ensure_annotations # ensure_annotations decorator is used to enforce type annotations on function arguments and return values.
from box import ConfigBox # ConfigBox class is a specialized Box object that allows accessing dictionary values as class attributes.
from pathlib import Path  # provides an object-oriented interface for working with file system paths
from typing import Any
import base64 # provides functions for encoding and decoding binary data as base64.



# This is a decorator that enforces type annotations on the decorated function. It ensures that the function arguments and return values adhere to the specified types.
@ensure_annotations
# a function named read_yaml that takes a Path object as an argument representing the path to a YAML file. It returns a ConfigBox object that wraps the content of the YAML file. The function loads the YAML file, logs a message if the file is successfully loaded, and raises a ValueError if the file is empty.
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
# function named create_directories that takes a list of paths (path_to_directories) representing the directories to be created. It creates the directories using os.makedirs() and logs a message for each created directory. The verbose argument determines whether or not to log the messages (default is True).
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
# function named save_json that takes a Path object (path) representing the path to a JSON file and a dictionary (data) to be saved in the JSON file. It saves the dictionary as JSON data in the specified file using json.dump() and logs a message indicating the file path.
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
# function named load_json that takes a Path object (path) representing the path to a JSON file. It loads the JSON file using json.load() and returns a ConfigBox object wrapping the loaded content. It logs a message indicating the file path.
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)



@ensure_annotations
#  function named save_bin that takes two arguments: data of type Any and path of type Path. It is responsible for saving binary data to a file.
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path) # save the data as a binary file at the specified path
    logger.info(f"binary file saved at: {path}") # After saving the file, the function logs a message indicating the file path where the binary file was saved using the logger object



@ensure_annotations
# function named load_bin that takes a Path object (path) representing the path to a binary file. It loads the binary data from the file using joblib.load() and returns the loaded object. It logs a message indicating the file path from which the binary file was loaded.
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
# function named get_size that takes a Path object (path) representing the path of a file. It calculates the size of the file in kilobytes (KB) by dividing the file size in bytes by 1024. It rounds the result to the nearest integer using round(). Then, it returns a string representation of the size in KB
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"



# function named decodeImage that takes two arguments: imgstring representing a base64-encoded image string and fileName representing the name of the file to which the decoded image will be saved. It decodes the base64-encoded image string using base64.b64decode() and assigns the decoded image data to the variable imgdata. Then, it opens the specified file in binary write mode ('wb') using open(), writes the decoded image data to the file using write(), and finally closes the file using close(). This function is useful for decoding and saving base64-encoded images.
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()



# function named encodeImageIntoBase64 that takes one argument croppedImagePath representing the path to an image file. It opens the specified image file in binary read mode ("rb") using open(), reads the content of the file using read(), and encodes the content as base64 using base64.b64encode(). Finally, it returns the base64-encoded image data. This function is useful for encoding images as base64.
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())