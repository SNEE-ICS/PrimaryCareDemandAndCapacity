Title: Primary care appointment demand forecasting in SNEE
Date: 2024-01-04
Modified: 2024-10-01
Category: Analysis blogs
Tags: pelican, publishing
Slug: Appointments Forecast
Authors: Ibrahim, Andrew
Summary: Primary care appointment demand forecasting


## Introduction
Appointment volumes have been increasing in SNEE. In order to estimate future appointments demand in the SNEE footprint, the project aims to leverage historical appointments data, analyze key patterns and trends, and details the process of developing a predictive/machine learning model to forecast the number of GP appointments at a regional level within the NHS framework. The project is focused on providing data-driven insights that can assist healthcare providers in better resource allocation, planning, and operational management. As patient numbers fluctuate due to various factors, predicting the number of future appointments can help mitigate overbooking or underutilization of healthcare services. The ultimate goal is to create a reliable and efficient predictive model that accounts for historical data and other relevant factors.
The predictive approach leverages machine learning techniques implemented through Scikit-learn, with particular focus on preprocessing large datasets, feature selection, and model evaluation using various metrics such as Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).


## Data source 
The primary data used for this  analysis is derived from the extensive appointments dataset provided by NHS England. The primary datasets used include:
- [NHS GP Appointments by Region](https://files.digital.nhs.uk/A4/53CF11/Appointments_GP_Regional_CSV_Apr_24.zip) : This dataset spans from November 2021 to April 2024, provides current information on GP appointments at a SUB-ICB (Integrated Care Board) level, including details such as healthcare professional types, appointment counts and appointment month.
- [NHS GP Appointments Historical Data](https://files.digital.nhs.uk/CF/699F6F/Appointments_GP_Regional_Mar_22.zip) : This historical dataset, spans from October 2019 to March 2022, allows for the analysis of historical trends and patterns in GP appointments. It also includes details such as healthcare professional types, appointment counts and appointment month.


## Methodology
1. Data Loading and Preprocessing:
Data from NHS GP appointments is loaded using pandas. Key variables such as appointment date, region, and healthcare provider type are selected for analysis.
Focus is placed on working-age individuals (20-65) and those over 65.
2. Exploratory Data Analysis (EDA):
Trends and patterns are explored using time series visualizations from matplotlib.
Autocorrelation (ACF) and partial autocorrelation (PACF) analysis using statsmodels helps identify time dependencies.
3. Modeling:
Various regression models, including Linear Regression, Lasso, and Ridge, are employed. A Pipeline from sklearn is used to streamline preprocessing and modeling steps.
Hyperparameter tuning is performed using GridSearchCV to identify the best model configuration.
Dimensionality reduction with Principal Component Analysis (PCA) improves model performance.
Cyclic Nature of Time (Months): To account for the cyclic nature of months (where January is close to December), the APPOINTMENT_MONTH column is transformed using sine and cosine functions. This maintains the cyclic pattern of time and allows the model to better capture seasonal effects.
Sin transformation: sin(2π×month/12)
Cos transformation: cos(2π×month/12)
Models are evaluated using Mean Squared Error (MSE), Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).
1. Forecasting:
The final model generates appointment predictions, which are visualized to highlight potential trends.
1. Model Saving:
The model is saved with joblib for future use without retraining.


## Statistical Forecast
There is a clear 12-month observed where the number of appointments peaks around october each year. When correcting for the number of working days in a year, this observed seasonality becomes stronger.


#### Placeholder: Trend plot


#### Placeholder: Trend plot (with appointments/working day)


## Machine learning Forecast




