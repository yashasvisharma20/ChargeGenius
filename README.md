# Insurance Charges Prediction

## Overview
This project predicts insurance charges based on various features using two machine learning models: **Random Forest Regression** and **K-Nearest Neighbors (KNN)**. The application is built using **Flask** to provide a user-friendly interface.

## Features
- **Data Preprocessing**: Cleaned and transformed the dataset.
- **Feature Selection**: Identified relevant features for prediction.
- **Model Training**:
    - **Random Forest Regression**: Ensemble model for accurate predictions.
    - **KNN**: Instance-based model for comparison.
- **Web Application**:
    - Created a Flask app to input user data and get predicted insurance charges.
    - Deployed the app for easy access.

## Usage
1. Install required Python libraries:
    ```bash
    pip install flask pandas scikit-learn
    ```

2. Run the Flask app:
    ```bash
    python app.py
    ```

3. Access the app in your browser at `http://localhost:5000`.

## Data Source
The dataset used for this project contains information about individuals' age, sex, BMI, number of children, smoker status, and region.

## Next Steps
- Optimize hyperparameters.
- Explore feature importance.
- Enhance the web interface.

