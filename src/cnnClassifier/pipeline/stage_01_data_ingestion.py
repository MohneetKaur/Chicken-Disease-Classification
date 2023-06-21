from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion stage" # defines a constant variable STAGE_NAME to hold the name of the current stage.

class DataIngestionTrainingPipeline:
    def __init__(self): # constructor method for the DataIngestionTrainingPipeline class
        pass # doesn't have any specific implementation and is left empty with the pass statement.

    def main(self):
        config = ConfigurationManager() # create an instance of the ConfigurationManager class to manage the configuration
        data_ingestion_config = config.get_data_ingestion_config() # retrieve the data ingestion configuration using the get_data_ingestion_config method of the ConfigurationManager class.
        data_ingestion = DataIngestion(config=data_ingestion_config) # create an instance of the DataIngestion class, passing the data ingestion configuration as an argument.
        data_ingestion.download_file() # call the download_file method of the DataIngestion instance to download the data file
        data_ingestion.extract_zip_file() # call the extract_zip_file method of the DataIngestion instance to extract the contents of the zip file




if __name__ == '__main__': # checks if the script is being run directly and not imported as a module
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") # log an information message indicating the start of the data ingestion stage.
        obj = DataIngestionTrainingPipeline() # create an instance of the DataIngestionTrainingPipeline class.
        obj.main() # call the main method of the DataIngestionTrainingPipeline instance to execute the main logic of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x") # logs an information message indicating the completion of the data ingestion stage
    except Exception as e:
        logger.exception(e) #  If an exception occurs during the execution, it logs the exception information using the logger.exception method
        raise e # re-raises the exception after logging
