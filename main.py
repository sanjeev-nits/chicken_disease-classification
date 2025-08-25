from cnnClassifier import logger

from cnnClassifier.pipeline.data_ingestion_pipe import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.prepare_base_model_pipe import PrepareBaseModelPipeline

STAGE_NAME_0='Data Ingestion'
STAGE_NAME_1='prepare base model'


try:
    logger.info(f">>>>>> stage {STAGE_NAME_0} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME_0} completed <<<<<<\n\nx==========x")


    logger.info(f">>>>>> stage {STAGE_NAME_1} started <<<<<<")
    base_model = PrepareBaseModelPipeline()
    base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME_1} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e