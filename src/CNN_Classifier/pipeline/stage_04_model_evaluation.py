
from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.model_evaluation import ModelEvaluation
from CNN_Classifier import logger

STAGE_NAME = "Model Evaluationr"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
        model_evaluation.save_score()
        # # comment below line if you do not want your experiments to be logged in MLFlow.
        # model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Started <<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
