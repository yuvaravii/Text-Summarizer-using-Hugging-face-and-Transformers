import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    with open(path_to_yaml, "r") as yaml_file:
        content = yaml.safe_load(yaml_file)

    if content is None:
        raise ValueError(f"YAML file is empty: {path_to_yaml}")

    return ConfigBox(content)


# @ensure_annotations
# def read_yaml(path_to_yaml:Path)->ConfigBox:
#     """
#     reads yaml file and returns configBox

#     Arguments
#         path_to_yaml (str):path to yaml file 

#     Raises
#         - error if yaml file is empty

#     Returns
#         - Config: ConfigBox type
#     """
#     try:
#         with open(path_to_yaml) as yaml_file:
#             content = yaml.safe_load(yaml_file)
#             logger.info(f"Yaml file : {yaml_file} loaded successfully....!")
#     except BoxValueError:
#         raise ValueError("yaml file is empty")
#     except Exception as e:
#         raise e
    
#     return ConfigBox(content)

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """
    creates the list of directories

    Arguments:
        - path_to_directories (list): list of path of directories
        - ignore_log (bool,optional): ignore if multiple path has to be created
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")