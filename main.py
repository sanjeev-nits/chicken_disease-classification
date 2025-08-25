from cnnClassifier import logger

from cnnClassifier.pipeline.data_ingestion_pipe import DataIngestionTrainingPipeline

STAGE_NAME='Data Ingestion'


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e