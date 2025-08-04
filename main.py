
from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} : Completed <<<<<<<<<<\n\n==========XXXXXXXXXX==========")
except Exception as e:
    logger.exception(e)
    raise e