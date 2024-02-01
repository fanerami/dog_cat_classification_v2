from cnnClassifier import logger
from cnnClassifier.pipeline.step_1_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.step_2_prepare_base_model import PrepareBaseModelPipline
from cnnClassifier.pipeline.step_3_training import TrainingPipeline
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelPipline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
