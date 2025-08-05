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


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class TrainerConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data_path: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

@dataclass(frozen=True)
class ModelEvaluationConfig:
    path_to_model: Path
    training_data_path: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int