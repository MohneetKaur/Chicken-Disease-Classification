import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion: # defines the name of the class
    def __init__(self, config: DataIngestionConfig): # constructor method for the DataIngestion class. It takes a single parameter config of type DataIngestionConfig
        self.config = config # assigns the config parameter to the self.config attribute, making it accessible within the class.


    
    # This method downloads the data file specified in the configuration.
    def download_file(self):
        if not os.path.exists(self.config.local_data_file): #  check if the local data file specified in the configuration does not already exist.
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, # urlretrieve function from the request module is used to download the file specified by the source_URL attribute in the configuration
                filename = self.config.local_data_file # The downloaded file is saved with the path specified by local_data_file.
            )

            # It logs an information message stating that the file has been downloaded, along with additional information such as the file name and headers.
            logger.info(f"{filename} download! with following info: \n{headers}")

        #  Else it logs an information message stating that the file already exists, along with its size    
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    # This method extracts a zip file into the data directory specified in the configuration.
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir # assign the unzip_dir attribute from the configuration to the unzip_path variable.
        os.makedirs(unzip_path, exist_ok=True) # creates the directory specified by unzip_path if it doesn't already exist.

        # opens the zip file specified by local_data_file attribute in the configuration for reading.
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path) # extracts all the contents of the zip file into the unzip_path directory.

