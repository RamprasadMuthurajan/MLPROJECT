#Why Data Ingestion ?
#It is to read data from different data sources, for example some data will be stored in the MongoDB , some will be stored in the different databases
#dataclass is used only for configuration why
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas
import dataclasses
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

#decorator
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join("artifacts","train.csv")#.join(folder_name,file_name)
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method")
        try:
            #so far read it from the csv file after that we will read it from the MongoDB database
            data=pandas.read_csv(filepath_or_buffer="notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")

            #create those folder we mentioned in the DataIngestionConfig class
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #storing the data in the raw datapath
            data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            #Now to create test and train data and store it in the train and test data path
            train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")
            

            #returning test and train path so that test and train data can be used for the modelling and everything
            return(self.ingestion_config.test_data_path,self.ingestion_config.train_data_path)




        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion() #this method return train and test data stored path

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
    




