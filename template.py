import os 
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    "research/research.ipynb"
]

# Krish Sir's code below :
for file_path in list_of_files:
    filepath = Path(file_path)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not (os.path.exists(filepath))) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating Empty file : {filepath}")
    
    else:
        logging.info(f"{filename} is already existing !")


# --- My simpler version --- yet contains lot of flaws
# for file_path in list_of_files:
#     path = Path(file_path)

#     # three major functions in path
#     # path.parent
#     # path.name
#     # path.exists()

#     path.parent.makedirs(parents = True, exist_ok = True)
#     if not path.exists():
#         path.touch()
#         logging.debug(f"Created empty file : {path}")


