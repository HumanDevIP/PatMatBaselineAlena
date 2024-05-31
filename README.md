# Early Baseline PatentMatch Paragraph Classification


Link to Plan of Experiment: <a href:=https://www.notion.so/Early-baseline-for-claim-cited-paragraph-classification-on-PatentMatch-Alena-fca8a73a8cc94544845944be9aed1087>Link</a>


Link to Full Report: <a href:=https://www.notion.so/Report-Alena-Early-Baseline-PatentMatch-Paragraph-Classification-7b3fbf5890eb4a5b8b4c08bb2f3625b8>Link</a>


## Goal of the experiment
1. On-hands discovery of the PatentMatch dataset, obtaining very preliminary baseline quality on the claim&cited-paragraph classification task (2 texts on model input, one binary classification label on output).
2. Learn how to use the newly introduced standards for implementation of research experiments.


## Data
The small sample of the PatentMatch dataset is provided in the train.parquet and test.parquet files available on <a href:=https://drive.google.com/drive/folders/16JQErGdej1Z33RIwUCoPAdNc6QY59iyl>Google Drive</a>


## How to run the experiment


### 1. Clone the repository
```
git clone git@github.com:HumanDevIP/PatMatBaselineAlena.git
```
If you run the experiment on Colab, put the cloned PatMatBaselineAlena folder on you Google drive in the root foolder.

### 2. Put the dataset into the data folder
To start the experiment, download the .parquet files from Google Drive and place them in the data folder of the project directory.

### 3. Put the credentials into .env file
Put the credentials into .env file with MLFLOW_TRACKING_URI, MLFLOW_TRACKING_USERNAME and MLFLOW_TRACKING_PASSWORD environment variables in the root of the project directory.

### 4. Run the notebooks/preprocessing.ipynb file
If you run the experiment on your local machine you may want to preliminarily create virtual environment, see <a href:=https://docs.python.org/3/library/venv.html>here</a>
The preprocessing notebook will install all necessary dependencies from requirements.txt file, read the .parquet files, clean up the dataset, prepare it for future training (splitting into train, validation and test sets) and save the 3 sets into .jsonl files into the data folder.

### 5. Run the notebooks/experiment.ipynb file
The experiment notebook will download the base transformers model and tokenizer for it, read the 3 sets (train, validation and test) from .jsonl files in data folder, train the model, save the best and the last model in the created "models" folder and log the metrics, hyperparameters and artifacts to mlflow.


## Compute Environment Information 

#### Local, CPU only:
- Python version: 3.11.7
- Compute environment: Windows 11

#### Colab
- Python version: 3.10.12
- TPU RAM 15.0 GB
