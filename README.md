# End-to-End-Cancer-Classification-using-MLFlow-DVC

## Workflows

1. Update config/config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity: src/CNN_Classifier/entity
5. Update the configuration manager in src/CNN_Classifier/config
6. Update the components: src/CNN_Classifier/components
7. Update the pipeline: src/CNN_Classifier/pipeline
8. Update main.py
9. Update dvc.yaml

### Dagshub

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/karan-1700/End-to-End-Cancer-Classification-using-MLFlow-DVC.mlflow
export MLFLOW_TRACKING_USERNAME=karan-1700
export MLFLOW_TRACKING_PASSWORD=<Password>
```

### DVC

To initialize DVC:
Run `dvc init` in the terminal.
Then, execute `dvc repro`.
Then, when you want to train your model with any different params, run `dvc repro` instead of `main.py`.
