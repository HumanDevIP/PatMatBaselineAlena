import os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.getcwd(), '.env'))


path_1 = os.path.join(os.getcwd(), '.env')


MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI')
MLFLOW_TRACKING_USERNAME = os.getenv('MLFLOW_TRACKING_USERNAME')
MLFLOW_TRACKING_PASSWORD = os.getenv('MLFLOW_TRACKING_PASSWORD')