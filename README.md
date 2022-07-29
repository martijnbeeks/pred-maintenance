<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Predictive Maintenance for water pumps in Tanzania</h3>

  <p align="center">
    Martijn Beeks
    <br />
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

This repository contains code for assessment of the Machine Learning Engineer vacancy at Vantage AI.
It is divided in two parts:
1. Data analysis and model training
2. Model deployment and serving predictions

<!-- GETTING STARTED -->
## 1. Data analysis and model training

This is an example on how to setup this project locally with python 3.8.13. This part displays notebooks
which containt exploratory analysis and model training.

1. ```sh
   python -m pip install -r requirements.txt
   ```
2. ```sh
   python -m notebook
   ```

This will display two notebooks: train_experiment_analysis and train_experiment_hyperparameter_tuning.
As the naming indicates, the first contains a notebook with an exploratory analysis and initial model training.
The latter notebook contains a hyper-parameter tuning model that outputs and saves the best model. 
This last model is also used in the deployment part of this project.


## 2. Model deployment and serving predictions
This part of the project contains deploying the trained model using FastApi and serving the predictions
using Streamlit. This is an example on how to setup this project locally using Docker in the /app directory. The docker-compose 
file spins up two containers: a frontend and a backend with the following command.
```sh
   docker-compose up -d --build
```
This will serve the frontend at localhost:8501 and the backend as API at localhost:8080. 
An user can test the entire application by going to the frontend and to the predict tab.
On this page, a user can upload /data/test_set.csv in the upload field and the prediction 
with related class probabilities is served. 