Title: Primary Care Appointment Duration in SNEE
Date: 2023-12-03
Modified: 2023-12-03
Category: Analysis blogs
Tags: pelican, publishing
Slug: Appointment-Duration
Authors: Ibrahim, Andrew
Summary: Primary Care appointment duration analysis

# Appointment Duration in SNEE Primary Care.

## Introduction & Background
In order to estimate future staffing requirements and demand in the SNEE footprint, it is important to understand how much demand (in time) is used for each appointment.\n
Unfortunately, the exact time taken per appointment is not provided; so it is very difficult to perform analyses to produce summary statistics or useful insights that would be possible with record-level data. With this the binned data, we can still use  maximum likelihood estimation (MLE) to determine the parameters of a probability distribution which can be used in further modelling of appointment times. \n
In this analysis we fit two empirical/theoretical distributions to the data in each sub-icb location for use in the system dynamics/ discrete event simulation analysis, the exponential distribution and a lognormal distribution.
![Plot3]({attach}/img/appointment_duration_4.png)



## Data Sources
NHS England appointment data [link](https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice/october-2023) was used as the main data source in this analysis. This compiles primary care appointment times. Some cleaning was required, all appointments with 'unknown/data quality' were removed from the dataset.\n

<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>SUB_ICB_LOCATION_CODE</th>\n      <th>SUB_ICB_LOCATION_ONS_CODE</th>\n      <th>SUB_ICB_LOCATION_NAME</th>\n      <th>ICB_ONS_CODE</th>\n      <th>REGION_ONS_CODE</th>\n      <th>Appointment_Date</th>\n      <th>ACTUAL_DURATION</th>\n      <th>COUNT_OF_APPOINTMENTS</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>01DEC2021</td>\n      <td>1-5 Minutes</td>\n      <td>1539</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>01DEC2021</td>\n      <td>31-60 Minutes</td>\n      <td>364</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>01DEC2021</td>\n      <td>Unknown / Data Quality</td>\n      <td>1277</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>01DEC2021</td>\n      <td>16-20 Minutes</td>\n      <td>730</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>01DEC2021</td>\n      <td>11-15 Minutes</td>\n      <td>1073</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>01DEC2021</td>\n      <td>6-10 Minutes</td>\n      <td>1698</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>01DEC2021</td>\n      <td>21-30 Minutes</td>\n      <td>619</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>02DEC2021</td>\n      <td>6-10 Minutes</td>\n      <td>1578</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>02DEC2021</td>\n      <td>Unknown / Data Quality</td>\n      <td>1391</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>00L</td>\n      <td>E38000130</td>\n      <td>NHS North East and North Cumbria ICB - 00L</td>\n      <td>E54000050</td>\n      <td>E40000012</td>\n      <td>02DEC2021</td>\n      <td>21-30 Minutes</td>\n      <td>601</td>\n    </tr>\n  </tbody>\n</table>



## Method
After cleaning the data, we counted the number of appointments in each time bin in each sub-ICB area as shown by the plots below. This was also grouped by financial year, to determine if there are any patterns or trends in the data.
![Appointment duration ]({attach}/img/appointment_duration_1.png)
![Plot2]({attach}/img/appointment_duration_2.png)
![Plot3]({attach}/img/appointment_duration_3.png)

After examining the data, it was decided that FY2023 is probably the most 'normal' year representing more typical demand after COVID-19 disrupted the previous years, both in terms of appointment times and also formats.

### Maximum Likelihood estimation
