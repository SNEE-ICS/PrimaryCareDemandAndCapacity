Title: Primary Care Appointment Duration in SNEE
Date: 2023-12-03
Modified: 2023-12-03
Category: Demand Analysis
Tags: pelican, publishing
Slug: Appointment-Duration
Authors: Ibrahim, Andrew
Summary: Primary Care appointment duration analysis

# Appointment Duration in SNEE Primary Care.

## Introduction & Background
In order to estimate future staffing requirements and demand in the SNEE footprint, it is important to understand how much demand (in time) is used for each appointment.  
Unfortunately, the exact time taken per appointment is not provided; so it is very difficult to perform analyses to produce summary statistics or useful insights that would be possible with record-level data. With this binned data, we can still use maximum likelihood estimation (MLE) to determine the parameters of a probability distribution which can be used in further modelling of appointment times. 
In this analysis we fit two empirical/theoretical distributions to the data in each sub-icb location for use in the system dynamics/ discrete event simulation analysis, the exponential distribution and a lognormal distribution. We use two, so that we can decide later on after discussion with stakeholders, which is more suitable for the model. We could also choose another distribution type.  
![Plot3]({attach}/img/appointment_duration_4.png)



## Data Sources
NHS England appointment data [link](https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice/october-2023) was used as the main data source in this analysis. This compiles primary care appointment times. Some cleaning was required, all appointments with 'unknown/data quality' were removed from the dataset.  

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>SUB_ICB_LOCATION_CODE</th>      <th>SUB_ICB_LOCATION_ONS_CODE</th>      <th>SUB_ICB_LOCATION_NAME</th>      <th>ICB_ONS_CODE</th>      <th>REGION_ONS_CODE</th>      <th>Appointment_Date</th>      <th>ACTUAL_DURATION</th>      <th>COUNT_OF_APPOINTMENTS</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>1-5 Minutes</td>      <td>1539</td>    </tr>    <tr>      <th>1</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>31-60 Minutes</td>      <td>364</td>    </tr>    <tr>      <th>2</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>Unknown / Data Quality</td>      <td>1277</td>    </tr>    <tr>      <th>3</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>16-20 Minutes</td>      <td>730</td>    </tr>    <tr>      <th>4</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>11-15 Minutes</td>      <td>1073</td>    </tr>    <tr>      <th>5</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>6-10 Minutes</td>      <td>1698</td>    </tr>    <tr>      <th>6</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>21-30 Minutes</td>      <td>619</td>    </tr>    <tr>      <th>7</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>02DEC2021</td>      <td>6-10 Minutes</td>      <td>1578</td>    </tr>    <tr>      <th>8</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>02DEC2021</td>      <td>Unknown / Data Quality</td>      <td>1391</td>    </tr>    <tr>      <th>9</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>02DEC2021</td>      <td>21-30 Minutes</td>      <td>601</td>    </tr>  </tbody></table>



## Method
After cleaning the data, we aggregated and counted the number of appointments in each time bin in each sub-ICB area as shown by the plots below. This was also grouped by financial year, to determine if there are any patterns or trends in the data. The distribution of the data is shown below, with the bin sizes reflective of how the data is provided.
![Appointment duration ]({attach}/img/appointment_duration_1.png)
![Plot2]({attach}/img/appointment_duration_2.png)
![Plot3]({attach}/img/appointment_duration_3.png)  
After examining the data, it was decided that FY2023 is probably the most 'normal' year representing more typical demand after COVID-19 disrupted the previous years, both in terms of appointment times and also formats.

### Maximum Likelihood estimation
We used numpy arrays to linearly space the observations within the bin edges, then used scipy's built in fit method (using MLE) to determine the best parameters for each distribution using the FY2023 data.


## Results
The results were a fitted set of distribution parameters which can be re-created during simulation runs. This is saved to a `yaml` file which is then easily read by the simulation application using a built in python package. These are positional arguments to scipy functions which recreate the distributions.
```yaml
Ipswich & East Suffolk:
  expon:
  - 1.0
  - 13.060152140044291
  lognorm:
  - 0.7551821071544044
  - -0.974990417176186
  - 11.467940407080306
North East Essex:
  expon:
  - 1.0
  - 12.806261222109528
  lognorm:
  - 0.6468566283947731
  - -1.8350298084742074
  - 12.754426837792252
West Suffolk:
  expon:
  - 1.0
  - 12.905713262336715
  lognorm:
  - 0.7234164989792777
  - -1.1943306133419396
  - 11.754347636020235

```

