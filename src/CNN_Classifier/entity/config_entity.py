# create an entity - a class created with a dataclass decorator.
# a class in which we can define any class variables without using self.
# when we set frozen=True, we are stating that we do not allow adding any other variables inside that class.
# by creating an entity, we can create a custom return type for a function.

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path