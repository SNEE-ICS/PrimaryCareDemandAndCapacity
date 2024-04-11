Title: Population Projection and Demographics in SNEE ICS
Date: 2024-01-03
Modified: 2024-01-03
Category: Demand Analysis
Tags: pelican, publishing
Slug: population-projection
Authors: Ibrahim, Andrew
Summary: Primary Care appointment duration analysis

# Appointment Duration in SNEE Primary Care.

## Introduction & Background
In order to estimate future staffing requirements and demand for primary care services in the SNEE footprint, it is essential to understand the likely changes in population and demographics over the 10 year horizon that the D&C model investigates. 
![Plot3]({attach}/img/appointment_duration_4.png)



## Data Sources

### ONS Population projections

[Population projections for CCGs provided by the ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/clinicalcommissioninggroupsinenglandz2) were used for the forward-looking population estimates used in the model. These are unfortunately 2018-based, so are not in line with the 2021 census, however they were revised in 2020. These are provided at the Clinical Commissioning Group (CCG) level (now sub-ICBs).

### Patients Registered at a GP practice

[Patients Registered at a GP practice, October 2023](https://digital.nhs.uk/data-and-information/publications/statistical/patients-registered-at-a-gp-practice/october-2023) was used for the baseline 2023 population of registered patients. There are myriad reasons why a patient would be registered in another CCG/GP Alliance area, including student term time address or living on area boundaries.


<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>SUB_ICB_LOCATION_CODE</th>      <th>SUB_ICB_LOCATION_ONS_CODE</th>      <th>SUB_ICB_LOCATION_NAME</th>      <th>ICB_ONS_CODE</th>      <th>REGION_ONS_CODE</th>      <th>Appointment_Date</th>      <th>ACTUAL_DURATION</th>      <th>COUNT_OF_APPOINTMENTS</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>1-5 Minutes</td>      <td>1539</td>    </tr>    <tr>      <th>1</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>31-60 Minutes</td>      <td>364</td>    </tr>    <tr>      <th>2</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>Unknown / Data Quality</td>      <td>1277</td>    </tr>    <tr>      <th>3</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>16-20 Minutes</td>      <td>730</td>    </tr>    <tr>      <th>4</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>11-15 Minutes</td>      <td>1073</td>    </tr>    <tr>      <th>5</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>6-10 Minutes</td>      <td>1698</td>    </tr>    <tr>      <th>6</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>01DEC2021</td>      <td>21-30 Minutes</td>      <td>619</td>    </tr>    <tr>      <th>7</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>02DEC2021</td>      <td>6-10 Minutes</td>      <td>1578</td>    </tr>    <tr>      <th>8</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>02DEC2021</td>      <td>Unknown / Data Quality</td>      <td>1391</td>    </tr>    <tr>      <th>9</th>      <td>00L</td>      <td>E38000130</td>      <td>NHS North East and North Cumbria ICB - 00L</td>      <td>E54000050</td>      <td>E40000012</td>      <td>02DEC2021</td>      <td>21-30 Minutes</td>      <td>601</td>    </tr>  </tbody></table>



## Method
A 'baseline' population was established using the GP patient lists for each sub-ICB area. A set of coefficients for each year and each 5 year age band was then calculated from the ONS population scenarios, again using 2023 as a baseline. The baseline population was then multiplied by these coefficients to product a population projection for each scenario.
![Appointment duration ]({attach}/img/appointment_duration_1.png)
![Plot2]({attach}/img/appointment_duration_2.png)
![Plot3]({attach}/img/appointment_duration_3.png)  
After examining the data, it was decided that FY2023 is probably the most 'normal' year representing more typical demand after COVID-19 disrupted the previous years, both in terms of appointment times and also formats.

# Caveats & Problems
The geographical mapping between Ipswich and East Suffolk / West Suffolk sub ICBs are not identical to the Primary care network (PCN) boundaries; in this case those patients in the Ixworth (IP31) area would be considered to be in the Ipswich & east Suffolk ICB, however they are located in the West suffolk PCN. Therefore the population estimates for the two sub-ICB locations/ PCN locations are slightly misaligned and the expectation is that the projections would be expected to be marginally less accurate.

## Results
The results were a fitted set of distribution parameters which can be re-created during simulation runs. This is saved to a `yaml` file which is then easily read by the simulation application using a built in python package. These are positional arguments to scipy functions which recreate the distributions.


