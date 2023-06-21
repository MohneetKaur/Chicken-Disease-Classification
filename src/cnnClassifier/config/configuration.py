from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager: # define the name of the class
    def __init__( # constructor method for the ConfigurationManager class
        self,
        # takes two optional parameters: config_filepath and params_filepath
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        # read the YAML file specified by config_filepath and assign the contents to the self.config attribute. The read_yaml function is assumed to be defined elsewhere and is responsible for parsing the YAML file.
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # call a function create_directories and pass a list containing the artifacts_root attribute from the self.config object. This function is be defined elsewhere and is responsible for creating the specified directories.

        create_directories([self.config.artifacts_root])


    
    # This method returns an instance of DataIngestionConfig, which is a data class representing the configuration for data ingestion.
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # retrieve the data_ingestion attribute from the self.config object and assigns it to the config variable.

        create_directories([config.root_dir]) # call the create_directories function to create the directory specified by config.root_dir.


        # creates an instance of DataIngestionConfig using the values from the config object. This instance represents the configuration for the data ingestion stage.
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config # eturns the data_ingestion_config object