
from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} : Started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} : Completed <<<<<<<<<<\n\n==========XXXXXXXXXX==========")
except Exception as e:
    logger.exception(e)
    raise e



from CNN_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME = "Prepare Base Model"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} : Started <<<<<<<<<<")
        prepare_base_model_pipeline = PrepareBaseModelPipeline()
        prepare_base_model_pipeline.main()
        logger.info(f">>>>>>>>>> Stage : {STAGE_NAME} : Completed <<<<<<<<<<\n\n==========XXXXXXXXXX==========")
    except Exception as e:
        logger.exception(e)
        raise e



from CNN_Classifier.pipeline.stage_03_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Started <<<<<<<<<<")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Completed <<<<<<<<<<\n\n==========XXXXXXXXXX==========")

except Exception as e:
    logger.exception(e)
    raise e
