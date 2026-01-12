# End-to-End-NLP-project-with-Hugging-face-and-Transformers
This is my second end to end project with respect to ML and NLP. Implemented step by step heuristically and documented each steps and notes within docs


# Objective
- To understand and implement the ML and NLP project step by step heuristically.
- To create a simple text summarization.
- Documenting each step with its difficulty and nuances.

# Implementation

## What is hugging face and why is it essentional?
- In my understanding, Hugging face is a platform where the models, datasets, documentation of different transformers are available.
- These resources are open, thus can be practioned by any personal, thus it is essential for every machine learning practioner.


## step-1: uv installation
- `pip install uv`
- `uv init --python 3.11`
- `uv sync`
- For installation of packages and grouping them together
    ```
    uv add --group groupName\
        pandas\
        numpy\
        matplotlib
    ```
- We can categorize them with group name.

## step-2: Create template.py
- Objective: To create the project folder structure automatically
- Create `template.py`
- Ensure `.gitignore` file is made and [`.venv`,`artifacts/`] are excluded.
- In terminal, run the following command `python template.py`

## step-3: Creating the logging and common utils functionalities; read json, save json, read yaml
### Building the logger
    - move to `src/logging`
    - we can write the commands within `__init__.py`
    1. What is your logging directory?
        - Creating `logs` in root directory of the project
    2. what is the logging format?
    3. What is your logging file path

    - Once the logger function is ready, we can execute them and check in `main.py`

### Building the common functionalities
- For effective handling of files and data we use:
    - `from box.exceptions import BoxValueError`
    - `from ensure import ensure_annotations`   --> Ensures only the right or intended data type enters the given function (decorator basically)
    - `from box import ConfigBox`  --> loading the dictionary in `dict1.k1` format 
    - `from typing import Any`
- Functions like:
    - read_yaml
    - create_directories
    - save_json
    - read_json
    - save_model