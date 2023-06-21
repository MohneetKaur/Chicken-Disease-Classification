from dataclasses import dataclass
from pathlib import Path


# decorator is used to automatically generate special methods for the class based on its defined fields
@dataclass(frozen=True) #  frozen=True parameter makes the class immutable, meaning its fields cannot be modified after instantiation
class DataIngestionConfig: #  define the name of the data class
    root_dir: Path # field of the class named root_dir of type Path from the pathlib module. It represents the root directory for the data ingestion stage
    source_URL: str # field of the class named source_URL of type str. It represents the URL from which the data for ingestion will be sourced.
    local_data_file: Path # field of the class named local_data_file of type Path. It represents the path where the downloaded data file will be stored locally.
    unzip_dir: Path # field of the class named unzip_dir of type Path. It represents the directory where the downloaded zip file will be extracted/unzipped.