# create entity with dataclasses where the values are held
from dataclasses import dataclass
from pathlib import Path 

# input and output for DataIngestioncomponent
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path