
from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.model_trainer import ModelTrainer
from CNN_Classifier import logger

STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.get_base_model()
        model_trainer.train_valid_generator()
        model_trainer.train()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Started <<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Completed <<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
