Title: Primary care appointment demand forecasting with simulation
Date: 2024-10-01
Modified: 2023-10-01
Category: Simulation Results
Authors: A.Jarman & I.Khan
Summary: Primary Care appointment volume forecasting

# Introduction & Background
In order to estimate future demand, we took two approaches - one a 'projection' using population demographics to estimate appointments per person per working day, based on the demographic profile of the area and the time of year.
This article focuses on a different approach - using univariate time series forecasting and a SARIMA model, we apply an autoregressive model incorporating seasonality and trend.
In order to normalise the number of (working) days in the month, our target variable was transformed into average appointments per working day

# Data Sources

The primary data used for this  analysis is derived from the extensive appointments dataset provided by NHS England. The primary datasets used include:
- [NHS GP Appointments by Region](https://files.digital.nhs.uk/A4/53CF11/Appointments_GP_Regional_CSV_Apr_24.zip) : This dataset spans from November 2021 to April 2024, provides current information on GP appointments at a SUB-ICB (Integrated Care Board) level, including details such as healthcare professional types, appointment counts and appointment month.
- [NHS GP Appointments Historical Data](https://files.digital.nhs.uk/CF/699F6F/Appointments_GP_Regional_Mar_22.zip) : This historical dataset, spans from October 2019 to March 2022, allows for the analysis of historical trends and patterns in GP appointments. It also includes details such as healthcare professional types, appointment counts and appointment month.

# Methodology
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_1.png)\
Before the forecast was prepared, the data for each sub-ICB area within SNEE was inspected using ACF and PACF correlation plots. In some areas the yearly seasonality was not apparent. 

A SARIMA model was used to forecast the future appointment demand in each area (Seasonal AutoRegressive Integrated Moving Average) this is particularly well-suited for time series data that exhibits both non-seasonal and seasonal patterns. 

- Handling Seasonal Patterns (12-Month Seasonality)
    - SARIMA is an extension of the ARIMA model that incorporates seasonal components. The seasonal component is useful for time series with recurring patterns over regular intervals, such as monthly seasonality in appointment data.
    - In this case, the time series has a 12-month seasonality pattern, meaning that there are predictable variations in the data that repeat every year. SARIMA captures these seasonal fluctuations with seasonal terms (denoted as P, D, Q) for the autoregressive, differencing, and moving average components of the seasonal pattern.
    - The model incorporates both short-term dependencies (via the non-seasonal AR and MA components) and long-term seasonal patterns (via the seasonal AR and MA components), allowing it to model yearly cycles effectively.
- Trend and Non-Stationary Data
    - The SARIMA model includes differencing (both non-seasonal differencing d and seasonal differencing D) to handle trends in the data, making it suitable for non-stationary time series where the data's mean and variance change over time.
    - By applying the appropriate differencing, SARIMA can remove trends and focus on modeling the underlying cyclical behavior.
- Modeling Long-Term Forecasts (10-15 Years)
    -SARIMA models can forecast well into the future because they explicitly account for seasonality and trends over time, unlike simpler models like ARIMA that only focus on non-seasonal components.
- With a 12-month seasonal cycle, SARIMA can extrapolate the seasonal patterns far into the future, making it suitable for long-term projections. The seasonal terms help the model repeat these cycles for each forecasted year, which is crucial for reliable predictions over long horizons, such as 10-15 years.
Since the model captures the yearly cycles and the overall trend (if present), it can predict future data based on historical patterns without requiring assumptions about future conditions beyond what the model has learned from past behavior.
- Handling Noise and Uncertainty
Over long forecast horizons, uncertainty increases, but SARIMA incorporates moving average components (both non-seasonal q and seasonal Q) to smooth out random noise in the data. This helps provide stable forecasts by reducing the impact of random fluctuations on the projections.
- Limitations:
    - While SARIMA is robust for long-term projections, it's important to note that it assumes that the underlying patterns (trend, seasonality, and autocorrelations) remain stable over time. If there are significant structural changes in the time series (e.g., due to policy changes, new technologies), the model might need to be adjusted or recalibrated.

## ACF & PACF Plots: Whole ICB
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_2.png)

## Seasonal Decomposition: Whole ICB
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_3.png)


## SARIMA model summary
### Ipswich & East Suffolk
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_4.png)
### North East Essex
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_5.png)
### West Suffolk
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_6.png)



# Results and inferences 

The forecasts provided can provide a rough baseline and an alternative demand scenario to the regression models, and are independent of the ONS population scenarios.

## Ipswich & East Suffolk
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_7.png)
## North East Essex
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_8.png)
## West Suffolk
![Number of Appointments Time Series](../../outputs/plots/num_appointments_timeseries_9.png)
