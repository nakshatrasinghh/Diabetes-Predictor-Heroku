# Diabetes Predictor - Deployment

Development Stack

![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

The notebook runs without downloading the datasets (Thanks to gdown). Just click, Learn and Explore.

If you forked this repository, you can link it to your heroku app afterwards 🔗.

**Summary**

The model was build by using the following [Dataset](https://www.kaggle.com/johndasilva/diabetes). 
Logistic Regression, Decision Trees, Random Forest, Support Vector Machine, XGBoost was used to train the model. Random Forest gave us the best model metrics, so I converted it into a pickel file and saved it.

**Run Deployed Model**

[![Deploy](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://diabetes-predictor-heroku-app.herokuapp.com/)

Click on the icon above to run the single page application in your browser directly. Just pass the values and the model will predict whether you have diabetes or not 💉.
