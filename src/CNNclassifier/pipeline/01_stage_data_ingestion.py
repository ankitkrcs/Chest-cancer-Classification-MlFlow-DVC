from src.CNNclassifier.config.configuration import ConfigurationManager
from src.CNNclassifier.components.data_ingestion import DataIngestion
from src.CNNclassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def _init_(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_files()
        data_ingestion.extract_zip_files()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e