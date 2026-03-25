import os 
import sys 
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.exceptions import CustomError
from src.logger import logging

ARTIFACTS_DIR = "artifacts"

@dataclass
class DataIngestionConfig:
    artifact_dir:str = ARTIFACTS_DIR
    train_data_path:str = os.path.join(ARTIFACTS_DIR, 'train.csv')
    test_data_path:str = os.path.join(ARTIFACTS_DIR, 'test.csv')
    raw_data_path:str = os.path.join(ARTIFACTS_DIR, 'raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info('Enter your data ingestion method or component')
        try:
            # ✅ safer path handling
            data_path = os.path.join("notebook", "data", "stud.csv")

            if not os.path.exists(data_path):
                raise FileNotFoundError(f"Dataset not found at {data_path}")

            df = pd.read_csv(data_path)
            logging.info("Dataset loaded successfully")
            
            # ✅ explicit directory creation
            os.makedirs(self.ingestion_config.artifact_dir, exist_ok=True)
            
            # ✅ save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=True)
            logging.info('Raw data save')
            
            # ✅ split data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=True)
            
            logging.info("Data ingestion completed successfully")
            
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
            
        except Exception as e:
            raise CustomError(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
        