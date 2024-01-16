Title: Primary Care Appointments (Attended/DNA) in SNEE
Date: 2024-01-04
Modified: 2024-01-04
Category: Analysis blogs
Tags: pelican, publishing
Slug: Attended and DNA Appointments
Authors: Ibrahim, Andrew
Summary: Primary Care appointments Attended/DNA analysis


# Introduction & Background
Understanding the frequency of missed appointments in SNEE footprints is crucial.  This analysis endeavors to construct a model that captures the instances of missed appointments, allowing patients to re-enter the system at a later date.


# Data Sources
The primary data for this analysis is derived from the extensive appointments dataset provided by NHS England, spanning from April 2021 to August 2023. While FY21 and FY22 were based on complete annual data, the assessment for FY23 is limited to the available data from April to August.
Dataset --> [NHS Digital - Appointments in General Practice](https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice)


# Methodology

Before the analysis, the data was pre-processed. 

- Appointment months were converted into FY-years.
- Extracted national average and proportion for all appointment types.

1- Comparison with SNEE Area:

- Compared national average and proportion with SNEE area for FY-YEAR 2021, 2022, and 2023.
- Plotted the comparisons.

2- Detailed Proportion Analysis:

- Extracted proportions of attended, DNA, and unknown appointments based on SUB-ICB, healthcare professional type (hcp_type), and appointment mode.
- Plotted the changes in missed appointments over the years.

3- Correlation Matrix:

- Conducted a correlation matrix analysis to identify factors affecting the likelihood of missing appointments (DNA) in the SNEE area.

4- Identifying Appointment Trends:

- Explored if certain appointments are more likely to be missed.
- Conducted additional analysis on appointment types with higher likelihood of being missed.

This approach involves a comprehensive examination of various factors influencing appointment attendance, utilizing visualizations for better understanding. This structured analysis should provide valuable insights into missed appointments trends and potential influencing factors in the SNEE area.


# Results and inferences 

## 1. Missed Appointments Comparison of Proportion and Average (per month): SNEE sub-ICB and National average


<style>
  table { border-collapse: collapse; width: 100%;}
  th { border: 1px solid black; padding: 8px; text-align: center;}
  td { border: 1px solid black; padding: 8px; text-align: left;}
</style>

<table>
  <thead>
    <tr><th rowspan="2">Year</th><th colspan="3">National (avg, %) each month of the year</th><th colspan="3">SNEE (AVG, %)</th></tr>
    <tr><th>Attended</th><th>DNA</th><th>Unknown</th><th>Attended</th><th>DNA</th><th>Unknown</th></tr>
  </thead>
  <tbody>
    <tr><td>FY-2021</td><td>579332.27 (91.56%)</td><td>27252.8 (4.26%)</td><td>25638.21 (4.18%)</td><td>450111.8 (93.55%)</td><td>16323.2 (3.32%)</td><td>15382.2 (3.13%)</td></tr>
    <tr><td>FY-2022</td><td>608099.22 (91.21%)</td><td>31568.7 (4.63%)</td><td>27095.84 (4.17%)</td><td>465021.9 (93.22%)</td><td>17822.6 (3.51%)</td><td>16936.3 (3.27%)</td></tr>
    <tr><td>FY-2023 (April-August)</td><td>591085.91 (90.55%)</td><td>29004.74 (4.35%)</td><td>33054.93 (5.10%)</td><td>448269.2 (92.17%)</td><td>14968 (3.05%)</td><td>23803 (4.78%)</td></tr>
  </tbody>
</table>


Based on the provided table:

- The average percentage of **DNA appointments** for SNEE-ICB is marginally **lower**, consistently falling notably below the National Average for each year.
- Conversely, the average percentage of **Attended appointments** for SNEE-ICB is slightly **higher**, distinctly surpassing the National Average for each year
We can infer that SNEE icb is performing marginally better than the National average

We can confirm the lower average of (Attended/DNA) AppointmentsSNEE compared to other ICB'S from the graph below
![Average appointments]({attach}/img/appointment_attendance_9.png)

### The table below illustrates the percentage of appointments categorized as Attended, DNA (Did Not Attend), and Unknown in SNEE-SUB-ICB's

<table>
  <tr><th>SUB_ICB_LOCATION_CODE</th><th>FY_YEAR</th><th>Attended</th><th>DNA</th><th>Unknown</th></tr>
  <tr><td rowspan="3">06L</td><td>FY2021</td><td>94.44%</td><td>2.4%</td><td>3.16%</td></tr>
  <tr><td>FY2022</td><td>93.62%</td><td>2.79%</td><td>3.59%</td></tr>
  <tr><td>FY2023</td><td>91.95%</td><td>2.7%</td><td>5.35%</td></tr>
  <tr><td rowspan="3">06T</td><td>FY2021</td><td>91.55%</td><td>4.97%</td><td>3.48%</td></tr>
  <tr><td>FY2022</td><td>91.16%</td><td>4.91%</td><td>3.92%</td></tr>
  <tr><td>FY2023</td><td>91%</td><td>3.83%</td><td>5.17%</td></tr>
  <tr><td rowspan="3">07K</td><td>FY2021</td><td>94.66%</td><td>2.58%</td><td>2.76%</td></tr>
  <tr><td>FY2022</td><td>94.88%</td><td>2.84%</td><td>2.29%</td></tr>
  <tr><td>FY2023</td><td>93.56%</td><td>2.62%</td><td>3.82%</td></tr>
</table>

- The sub-ICB North East Essex (06T) demonstrates the highest proportion of DNA appointments, indicating a significant number of missed appointments.
- Conversely, the sub-ICB West Suffolk (07K) exhibits the maximum proportion of Attended appointments,


## 2. Appointment Trends Over Time/Years

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_5.png)

We can easily infer that -

- Nationally the missed appointments are consistent over years when appointment mode is Face to Face, home visit or telephonic.
- Nationally inconsistencies is observed in appointments with unknown or video/online modes over the years.

- Below graph represents the same information for SNEE-ICB areas

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_7.png)



## 3. To understand if Across staff groups & Sub-ICB, are some appointments more likely to be missed/attended

### Below table shows the comaparison between % of appointments (Attended,DNA and Unknwon) National vs SNEE, based on HCP type and Appointment mode

<table>
  <tr><th colspan="2">TYPE</th><th colspan="3">National</th><th colspan="3">SNEE</th></tr>
  <tr><th>HCP_TYPE</th><th>APPT_MODE</th><th>Attended</th><th>DNA</th><th>Unknown</th><th>Attended</th><th>DNA</th><th>Unknown</th></tr>
  <tr><td rowspan="5">GP</td><td>Face-to-Face</td><td>93.36%</td><td>3.43%</td><td>3.2%</td><td>95.26%</td><td>2.2%</td><td>2.54%</td></tr>
  <tr><td>Home Visit</td><td>83.07%</td><td>2.31%</td><td>14.62%</td><td>93.53%</td><td>1.78%</td><td>4.69%</td></tr>
  <tr><td>Telephone</td><td>95.99%</td><td>1.52%</td><td>2.49%</td><td>97.81%</td><td>0.68%</td><td>1.51%</td></tr>
  <tr><td>Unknown</td><td>59.83%</td><td>3.01%</td><td>37.23%</td><td>44.41%</td><td>2.79%</td><td>52.79%</td></tr>
  <tr><td>Video/Online</td><td>91.13%</td><td>1.46%</td><td>7.4%</td><td>91.22%</td><td>2.39%</td><td>6.39%</td></tr>
   <tr><td rowspan="5">Other Practice staff</td><td>Face-to-Face</td><td>87.69%</td><td>7.26%</td><td>5.05%</td><td>90.12%</td><td>5.22%</td><td>4.66%</td></tr>
  <tr><td>Home Visit</td><td>80.95%</td><td>3.35%</td><td>15.71%</td><td>88.89%</td><td>3.58%</td><td>7.53%</td></tr>
  <tr><td>Telephone</td><td>92.91%</td><td>3.13%</td><td>3.96%</td><td>95.89%</td><td>1.19%</td><td>2.91%</td></tr>
  <tr><td>Unknown</td><td>50.56%</td><td>4.09%</td><td>45.35%</td><td>34.29%</td><td>2.37%</td><td>63.34%</td></tr>
  <tr><td>Video/Online</td><td>86.81%</td><td>3.72%</td><td>9.48%</td><td>89.92%</td><td>6.38%</td><td>3.7%</td></tr>
  <tr><td rowspan="5">Unknown</td><td>Face-to-Face</td><td>76.37%</td><td>2.96%</td><td>23%</td><td>18.38%</td><td>72.26%</td><td>9.36%</td></tr>
  <tr><td>Home Visit</td><td>66.85%</td><td>3.99%</td><td>31.43%</td><td>87.96%</td><td>0.93%</td><td>11.12%</td></tr>
  <tr><td>Telephone</td><td>89.61%</td><td>2.6%</td><td>10.56%</td><td>91.25%</td><td>3.13%</td><td>5.62%</td></tr>
  <tr><td>Unknown</td><td>79.38%</td><td>2.74%</td><td>30.33%</td><td>92.12%</td><td>2.3%</td><td>5.58%</td></tr>
  <tr><td>Video/Online</td><td>81.71%</td><td>3.77%</td><td>19.86%</td><td>79.56%</td><td>3.28%</td><td>17.16%</td></tr>
</table>

 #### Inferences for Attended Appointments
  - GP: The **attendance** rate is **higher** Nationally and in SNEE area, compared to other HCP_TYPE. highest Where APPT_MODE is **Face-to-Face** followed by **Telephone**
  - Other Practice Staff:  **Telephone** appointments with **Other Practice Staff** have **high attendance** rates both nationally and in SNEE.

 #### Inferences for DNA Appointments
 - GP: GP appointments with **unknown modes** have the **highest DNA** rates both nationally and in SNEE.
 - Other Practice Staff: **Face-to-Face** appointments with **Other Practice Staff** have **highest DNA** rates followed by **Video/Online**.

 #### Other critical Inferences:
 - Appointments with **unknown HCP types**, under all **APPT_MODE**, have significantly **higher DNA** rates compared to other types.
 - Telephone appointments exhibit high attendance rates across all HCP types. This suggests a growing acceptance and comfort with telemedicine, emphasizing the importance of remote healthcare options.

### Graphical representation for the above table

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_4.png)

### Below graph represents the same information for SNEE-ICB areas

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_8.png)



## 4. Likelihood of Missing Appointments: from a combination of Sub-ICB, Staff type, Appointment type.

- To understand this in detail, we have generated a Correlation matrix between all the indicators under SNEE-ICB areas.
- Correlation between variables signifies the degree and direction of the relationship between them. It measures how changes in one variable correspond to changes in another.
Correlation is measured on a scale from -1 to 1:

- Close to 1 shows a strong positive relationship: both variables move in the same direction or increase together.
- Close to -1 indicates a strong negative relationship: the variables move in opposite directions, means as one variable goes up, the other tends to go down.
- Around 0 suggests a weak or no clear relationship between the variables.

<table border="1">
  <tr><th>Feature</th><th>Coefficient</th></tr>
  <tr><td>APPT_MODE_Face-to-Face</td><td>0.204919</td></tr>
  <tr><td>HCP_TYPE_Unknown</td><td>0.165292</td></tr>
  <tr><td>SUB_ICB_LOCATION_CODE_06T</td><td>0.101825</td></tr>
  <tr><td>APPT_MODE_Unknown</td><td>0.091138</td></tr>
  <tr><td>HCP_TYPE_Other Practice staff</td><td>0.050375</td></tr>
  <tr><td>SUB_ICB_LOCATION_CODE_06L</td><td>0.004799</td></tr>
  <tr><td>APPT_MODE_Video/Online</td><td>-0.019436</td></tr>
  <tr><td>SUB_ICB_LOCATION_CODE_07K</td><td>-0.110447</td></tr>
  <tr><td>APPT_MODE_Home Visit</td><td>-0.119116</td></tr>
  <tr><td>APPT_MODE_Telephone</td><td>-0.143173</td></tr>
  <tr><td>HCP_TYPE_GP</td><td>-0.190721</td></tr>
</table>

- In summary, **face-to-face appointments**, **unknown healthcare providers**, and specific location codes **(like '06T')** have **positive correlations** with **DNA** appointments, indicating that these factors increase the chances of appointment being missed. 
- While **home visits**, **telephone appointments**, **GPs**, and specific location codes **(like '07K')** have weak negative correlations, therefore these factors will decrese the chances of appointment being missed


## 5. Creating YAML for results

Finally, the results were processed into a YAML file for the simulation application, providing proportions of DNA appointments by sub-ICB areas, HCP types, and appointment modes.
- code "06L": Ipswich & East Suffolk, "07K": West Suffolk, "06T": North East Essex, corresponds to sub-areas under SNEE-ICB.
```yaml
00L:
  GP:
    Face-to-Face: 0.0223
    Home Visit: 0.0197
    Telephone: 0.0074
    Unknown: 0.0055
    Video/Online: 0.0238
  Other Practice staff:
    Face-to-Face: 0.0648
    Home Visit: 0.0075
    Telephone: 0.0243
    Unknown: 0.0152
    Video/Online: 0.031
  Unknown:
    Face-to-Face: 0.0003
    Home Visit: 0.0033
    Telephone: 0.0526
    Unknown: 0.0267
00N:
  GP:
    Face-to-Face: 0.0309
    Home Visit: 0.074
    Telephone: 0.0217
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0629
    Home Visit: 0.0297
    Telephone: 0.0476
    Unknown: .nan
    Video/Online: 0.0005
  Unknown:
    Face-to-Face: 0.0012
    Home Visit: 0.0198
    Telephone: 0.0291
00P:
  GP:
    Face-to-Face: 0.0425
    Home Visit: 0.0133
    Telephone: 0.0199
    Unknown: 0.0009
    Video/Online: 0.0001
  Other Practice staff:
    Face-to-Face: 0.0763
    Home Visit: 0.0105
    Telephone: 0.0504
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0045
    Home Visit: 0.0058
    Telephone: 0.3313
    Unknown: .nan
00Q:
  GP:
    Face-to-Face: 0.0441
    Home Visit: 0.0077
    Telephone: 0.0262
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.09
    Home Visit: 0.0349
    Telephone: 0.0593
    Unknown: .nan
    Video/Online: 0.0024
  Unknown:
    Face-to-Face: 0.0003
    Home Visit: 0.002
    Telephone: .nan
00R:
  GP:
    Face-to-Face: 0.05
    Home Visit: 0.0069
    Telephone: 0.0293
    Unknown: .nan
  Other Practice staff:
    Face-to-Face: 0.0863
    Home Visit: 0.0376
    Telephone: 0.0453
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0073
    Home Visit: 0.0293
    Telephone: 0.0281
00T:
  GP:
    Face-to-Face: 0.051
    Home Visit: 0.0086
    Telephone: 0.0439
    Unknown: 0.0632
    Video/Online: 0.0172
  Other Practice staff:
    Face-to-Face: 0.1014
    Home Visit: 0.0361
    Telephone: 0.0589
    Unknown: 0.0555
    Video/Online: 0.0409
  Unknown:
    Face-to-Face: 0.0022
    Home Visit: 0.1227
    Telephone: 0.0418
    Unknown: 0.0389
    Video/Online: .nan
00V:
  GP:
    Face-to-Face: 0.0461
    Home Visit: 0.0101
    Telephone: 0.0219
    Unknown: 0.0919
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0814
    Home Visit: 0.0184
    Telephone: 0.0338
    Unknown: 0.0163
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0028
    Home Visit: 0.0081
    Telephone: 0.0003
00X:
  GP:
    Face-to-Face: 0.0366
    Home Visit: 0.0069
    Telephone: 0.0222
    Unknown: .nan
    Video/Online: 0.0044
  Other Practice staff:
    Face-to-Face: 0.0685
    Home Visit: 0.0213
    Telephone: 0.0553
    Unknown: 0.0066
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.02
    Home Visit: 0.014
    Telephone: 0.0056
    Unknown: .nan
    Video/Online: .nan
00Y:
  GP:
    Face-to-Face: 0.0478
    Home Visit: 0.0079
    Telephone: 0.0202
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0979
    Home Visit: 0.0438
    Telephone: 0.0479
    Unknown: 0.0024
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0002
    Home Visit: 0.0028
    Telephone: .nan
    Unknown: .nan
    Video/Online: .nan
01A:
  GP:
    Face-to-Face: 0.0431
    Home Visit: 0.0199
    Telephone: 0.0238
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0795
    Home Visit: 0.0367
    Telephone: 0.0545
    Unknown: 0.002
    Video/Online: 0.0014
  Unknown:
    Face-to-Face: 0.0022
    Home Visit: 0.0039
    Telephone: 0.006
    Unknown: .nan
    Video/Online: .nan
01D:
  GP:
    Face-to-Face: 0.049
    Home Visit: 0.0117
    Telephone: 0.0301
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0988
    Home Visit: 0.0162
    Telephone: 0.0913
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0005
    Home Visit: 0.0116
    Telephone: 0.0498
    Unknown: .nan
01E:
  GP:
    Face-to-Face: 0.0385
    Home Visit: 0.005
    Telephone: 0.0193
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0798
    Home Visit: 0.0115
    Telephone: 0.0628
    Unknown: 0.002
    Video/Online: .nan
01F:
  GP:
    Face-to-Face: 0.0359
    Home Visit: 0.0078
    Telephone: 0.0416
    Unknown: 0.0046
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0829
    Home Visit: 0.0382
    Telephone: 0.0831
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0001
    Home Visit: 0.0081
    Telephone: 0.019
    Unknown: .nan
    Video/Online: .nan
01G:
  GP:
    Face-to-Face: 0.0601
    Home Visit: 0.0071
    Telephone: 0.0226
    Unknown: 0.0217
    Video/Online: 0.0013
  Other Practice staff:
    Face-to-Face: 0.101
    Home Visit: 0.0568
    Telephone: 0.0574
    Unknown: 0.0712
    Video/Online: 0.0007
  Unknown:
    Face-to-Face: 0.0006
    Home Visit: 0.018
    Telephone: 0.003
01H:
  GP:
    Face-to-Face: 0.0249
    Home Visit: 0.0071
    Telephone: 0.0199
    Unknown: 0.0049
    Video/Online: 0.0004
  Other Practice staff:
    Face-to-Face: 0.0654
    Home Visit: 0.018
    Telephone: 0.0472
    Unknown: 0.0083
    Video/Online: 0.0004
  Unknown:
    Face-to-Face: 0.0026
    Home Visit: 0.0041
    Telephone: 0.0114
    Unknown: .nan
    Video/Online: .nan
01J:
  GP:
    Face-to-Face: 0.0388
    Home Visit: 0.0142
    Telephone: 0.0263
    Unknown: .nan
  Other Practice staff:
    Face-to-Face: 0.1058
    Home Visit: 0.0298
    Telephone: 0.0632
    Unknown: .nan
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.009
    Telephone: 0.0028
01K:
  GP:
    Face-to-Face: 0.0327
    Home Visit: 0.0082
    Telephone: 0.0258
    Unknown: 0.0128
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0636
    Home Visit: 0.0165
    Telephone: 0.0466
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0007
    Home Visit: 0.0244
    Telephone: 0.0328
    Unknown: .nan
    Video/Online: .nan
01T:
  GP:
    Face-to-Face: 0.034
    Home Visit: 0.012
    Telephone: 0.0166
    Unknown: 0.0204
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0877
    Home Visit: 0.0116
    Telephone: 0.0401
    Unknown: 0.0223
    Video/Online: .nan
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0052
    Telephone: 0.0086
    Unknown: .nan
01V:
  GP:
    Face-to-Face: 0.029
    Home Visit: 0.0101
    Telephone: 0.0146
    Unknown: 0.1648
    Video/Online: 0.0001
  Other Practice staff:
    Face-to-Face: 0.072
    Home Visit: 0.01
    Telephone: 0.0401
    Unknown: .nan
    Video/Online: 0.0009
  Unknown:
    Face-to-Face: 0.0004
    Home Visit: 0.0029
    Telephone: 0.0028
    Unknown: .nan
    Video/Online: .nan
01W:
  GP:
    Face-to-Face: 0.0458
    Home Visit: 0.0068
    Telephone: 0.0256
    Unknown: 0.0032
    Video/Online: 0.0004
  Other Practice staff:
    Face-to-Face: 0.0726
    Home Visit: 0.0698
    Telephone: 0.0558
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.012
    Home Visit: 0.0177
    Telephone: 0.0299
    Unknown: .nan
    Video/Online: .nan
01X:
  GP:
    Face-to-Face: 0.0384
    Home Visit: 0.0094
    Telephone: 0.0266
    Unknown: 0.0068
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0805
    Home Visit: 0.018
    Telephone: 0.0639
    Unknown: 0.0005
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0009
    Home Visit: 0.0109
    Telephone: 0.012
    Unknown: .nan
01Y:
  GP:
    Face-to-Face: 0.0519
    Home Visit: 0.0085
    Telephone: 0.0319
    Unknown: 0.0112
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0892
    Home Visit: 0.0524
    Telephone: 0.067
    Unknown: 0.0171
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0006
    Home Visit: 0.0036
    Telephone: .nan
    Unknown: 0.0385
02A:
  GP:
    Face-to-Face: 0.0473
    Home Visit: 0.0114
    Telephone: 0.0353
    Unknown: .nan
    Video/Online: 0.0044
  Other Practice staff:
    Face-to-Face: 0.0977
    Home Visit: 0.0311
    Telephone: 0.0737
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0016
    Home Visit: 0.0084
    Telephone: 0.0609
    Video/Online: .nan
02E:
  GP:
    Face-to-Face: 0.0212
    Home Visit: 0.0395
    Telephone: 0.0093
    Unknown: 0.0149
    Video/Online: 0.0235
  Other Practice staff:
    Face-to-Face: 0.0624
    Home Visit: 0.0269
    Telephone: 0.0257
    Unknown: 0.0148
    Video/Online: 0.0517
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0171
    Telephone: .nan
    Unknown: 0.0264
02G:
  GP:
    Face-to-Face: 0.023
    Home Visit: 0.0155
    Telephone: 0.0232
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0614
    Home Visit: 0.0311
    Telephone: 0.0442
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0135
    Telephone: .nan
02H:
  GP:
    Face-to-Face: 0.0471
    Home Visit: 0.0092
    Telephone: 0.0232
    Unknown: 0.0597
    Video/Online: 0.0472
  Other Practice staff:
    Face-to-Face: 0.0903
    Home Visit: 0.0231
    Telephone: 0.0474
    Unknown: 0.0391
    Video/Online: 0.026
  Unknown:
    Face-to-Face: 0.0036
    Home Visit: 0.004
    Telephone: .nan
    Unknown: 0.0414
02M:
  GP:
    Face-to-Face: 0.036
    Home Visit: 0.0085
    Telephone: 0.0125
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0543
    Home Visit: 0.0231
    Telephone: 0.08
    Unknown: .nan
  Unknown:
    Face-to-Face: 0.0001
    Home Visit: 0.0074
    Telephone: 0.0011
    Unknown: .nan
    Video/Online: .nan
02P:
  GP:
    Face-to-Face: 0.0258
    Home Visit: 0.008
    Telephone: 0.0181
    Unknown: 0.1402
    Video/Online: 0.0043
  Other Practice staff:
    Face-to-Face: 0.0559
    Home Visit: 0.0172
    Telephone: 0.0343
    Unknown: 0.1082
    Video/Online: 0.0491
  Unknown:
    Face-to-Face: .nan
    Home Visit: .nan
    Telephone: 0.0029
    Unknown: 0.0293
02Q:
  GP:
    Face-to-Face: 0.0256
    Home Visit: 0.008
    Telephone: 0.0086
    Unknown: 0.0391
    Video/Online: 0.0058
  Other Practice staff:
    Face-to-Face: 0.0662
    Home Visit: 0.0016
    Telephone: 0.012
    Unknown: 0.0326
    Video/Online: 0.0051
  Unknown:
    Unknown: 0.0181
02T:
  GP:
    Face-to-Face: 0.0253
    Home Visit: 0.006
    Telephone: 0.0107
    Unknown: 0.0174
    Video/Online: 0.0265
  Other Practice staff:
    Face-to-Face: 0.0587
    Home Visit: 0.0396
    Telephone: 0.0152
    Unknown: 0.0183
    Video/Online: 0.0065
  Unknown:
    Face-to-Face: .nan
    Home Visit: .nan
    Unknown: 0.0264
    Video/Online: .nan
02X:
  GP:
    Face-to-Face: 0.0429
    Home Visit: 0.0114
    Telephone: 0.019
    Unknown: 0.0273
    Video/Online: 0.046
  Other Practice staff:
    Face-to-Face: 0.063
    Home Visit: 0.0664
    Telephone: 0.0277
    Unknown: 0.0218
    Video/Online: 0.0691
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0203
    Telephone: 0.001
    Unknown: 0.0357
    Video/Online: .nan
02Y:
  GP:
    Face-to-Face: 0.0245
    Home Visit: 0.0103
    Telephone: 0.0095
    Unknown: 0.0218
    Video/Online: 0.0096
  Other Practice staff:
    Face-to-Face: 0.0521
    Home Visit: 0.0202
    Telephone: 0.0311
    Unknown: 0.0163
    Video/Online: 0.0067
  Unknown:
    Face-to-Face: 0.0001
    Home Visit: .nan
    Telephone: 0.0025
    Unknown: 0.0194
03F:
  GP:
    Face-to-Face: 0.0371
    Home Visit: 0.0332
    Telephone: 0.0078
    Unknown: 0.0431
    Video/Online: 0.0377
  Other Practice staff:
    Face-to-Face: 0.0856
    Home Visit: 0.0401
    Telephone: 0.0346
    Unknown: 0.0335
    Video/Online: 0.1221
  Unknown:
    Face-to-Face: 0.0006
    Home Visit: 0.0065
    Telephone: 0.035
    Unknown: 0.0305
    Video/Online: .nan
03H:
  GP:
    Face-to-Face: 0.0167
    Home Visit: 0.0075
    Telephone: 0.0095
    Unknown: .nan
    Video/Online: 0.008
  Other Practice staff:
    Face-to-Face: 0.0473
    Home Visit: 0.0016
    Telephone: 0.0165
    Unknown: 0.0155
    Video/Online: 0.0604
  Unknown:
    Face-to-Face: 0.0003
    Telephone: 0.0084
    Unknown: 0.0201
03K:
  GP:
    Face-to-Face: 0.0211
    Home Visit: 0.0148
    Telephone: 0.0147
    Unknown: 0.0023
    Video/Online: 0.0096
  Other Practice staff:
    Face-to-Face: 0.0449
    Home Visit: 0.0143
    Telephone: 0.0202
    Unknown: 0.0077
    Video/Online: 0.022
  Unknown:
    Unknown: 0.0237
03L:
  GP:
    Face-to-Face: 0.0276
    Home Visit: 0.0126
    Telephone: 0.0099
    Unknown: 0.0023
    Video/Online: 0.012
  Other Practice staff:
    Face-to-Face: 0.0685
    Home Visit: 0.0341
    Telephone: 0.0232
    Unknown: 0.0264
    Video/Online: 0.0551
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0106
    Telephone: .nan
    Unknown: 0.0187
03N:
  GP:
    Face-to-Face: 0.0312
    Home Visit: 0.0202
    Telephone: 0.0111
    Unknown: 0.0214
    Video/Online: 0.0268
  Other Practice staff:
    Face-to-Face: 0.072
    Home Visit: 0.0302
    Telephone: 0.0119
    Unknown: 0.0349
    Video/Online: 0.0438
  Unknown:
    Face-to-Face: 0.0109
    Home Visit: 0.0243
    Telephone: 0.0232
    Unknown: 0.0232
    Video/Online: .nan
03Q:
  GP:
    Face-to-Face: 0.0335
    Home Visit: 0.0147
    Telephone: 0.0089
    Unknown: 0.0396
    Video/Online: 0.0026
  Other Practice staff:
    Face-to-Face: 0.0497
    Home Visit: 0.0343
    Telephone: 0.0171
    Unknown: 0.0331
    Video/Online: 0.0099
  Unknown:
    Face-to-Face: 0.0023
    Home Visit: 0.0312
    Telephone: .nan
    Unknown: 0.0116
03R:
  GP:
    Face-to-Face: 0.0219
    Home Visit: 0.0165
    Telephone: 0.006
    Unknown: 0.0328
    Video/Online: 0.0117
  Other Practice staff:
    Face-to-Face: 0.0578
    Home Visit: 0.0239
    Telephone: 0.0086
    Unknown: 0.0184
    Video/Online: 0.0429
  Unknown:
    Unknown: 0.0255
03W:
  GP:
    Face-to-Face: 0.0305
    Home Visit: 0.0219
    Telephone: 0.0061
    Unknown: 0.0405
    Video/Online: 0.0195
  Other Practice staff:
    Face-to-Face: 0.051
    Home Visit: 0.0343
    Telephone: 0.0063
    Unknown: 0.021
    Video/Online: 0.0581
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0203
    Telephone: .nan
    Unknown: 0.0234
04C:
  GP:
    Face-to-Face: 0.0305
    Home Visit: 0.0235
    Telephone: 0.0072
    Unknown: 0.0167
    Video/Online: 0.0305
  Other Practice staff:
    Face-to-Face: 0.0802
    Home Visit: 0.0578
    Telephone: 0.0221
    Unknown: 0.0301
    Video/Online: 0.0407
  Unknown:
    Unknown: 0.0358
04V:
  GP:
    Face-to-Face: 0.0246
    Home Visit: 0.0542
    Telephone: 0.0085
    Unknown: 0.014
    Video/Online: 0.0239
  Other Practice staff:
    Face-to-Face: 0.0522
    Home Visit: 0.0341
    Telephone: 0.0275
    Unknown: 0.0137
    Video/Online: 0.0574
  Unknown:
    Unknown: 0.0178
04Y:
  GP:
    Face-to-Face: 0.0331
    Home Visit: 0.0044
    Telephone: 0.018
    Unknown: .nan
    Video/Online: 0.0188
  Other Practice staff:
    Face-to-Face: 0.0661
    Home Visit: 0.0207
    Telephone: 0.0744
    Unknown: 0.0011
    Video/Online: 0.0377
  Unknown:
    Face-to-Face: 0.0036
    Home Visit: 0.0189
    Telephone: 0.1515
    Video/Online: .nan
05D:
  GP:
    Face-to-Face: 0.0366
    Home Visit: 0.0023
    Telephone: 0.0246
    Unknown: .nan
    Video/Online: 0.0236
  Other Practice staff:
    Face-to-Face: 0.0582
    Home Visit: 0.0313
    Telephone: 0.0565
    Unknown: 0.0005
    Video/Online: .nan
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0107
    Telephone: 0.0008
    Unknown: 0.0204
05G:
  GP:
    Face-to-Face: 0.0268
    Home Visit: 0.0091
    Telephone: 0.0167
    Unknown: 0.0079
    Video/Online: 0.0005
  Other Practice staff:
    Face-to-Face: 0.0615
    Home Visit: 0.017
    Telephone: 0.0381
    Unknown: 0.0121
    Video/Online: 0.0009
  Unknown:
    Face-to-Face: 0.0001
    Home Visit: 0.0053
    Telephone: .nan
    Unknown: 0.0118
    Video/Online: .nan
05Q:
  GP:
    Face-to-Face: 0.0407
    Home Visit: 0.0121
    Telephone: 0.0205
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0638
    Home Visit: 0.012
    Telephone: 0.0435
    Unknown: 0.0013
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0012
    Home Visit: 0.3073
    Telephone: 0.046
05V:
  GP:
    Face-to-Face: 0.0413
    Home Visit: 0.0191
    Telephone: 0.0204
    Unknown: .nan
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.0663
    Home Visit: 0.0424
    Telephone: 0.0411
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.0001
    Home Visit: 0.0065
    Telephone: .nan
05W:
  GP:
    Face-to-Face: 0.0475
    Home Visit: 0.0067
    Telephone: 0.0203
    Unknown: 0.0267
    Video/Online: 0.002
  Other Practice staff:
    Face-to-Face: 0.0847
    Home Visit: 0.0174
    Telephone: 0.0573
    Unknown: 0.0058
    Video/Online: 0.0004
  Unknown:
    Face-to-Face: 0.0001
    Home Visit: 0.006
    Telephone: 0.0029
    Unknown: 0.0257
06H:
  GP:
    Face-to-Face: 0.0291
    Home Visit: 0.0143
    Telephone: 0.0049
    Unknown: 0.0127
    Video/Online: 0.0044
  Other Practice staff:
    Face-to-Face: 0.0598
    Home Visit: 0.0185
    Telephone: 0.0136
    Unknown: 0.0384
    Video/Online: 0.0331
  Unknown:
    Face-to-Face: 0.0003
    Home Visit: 0.0285
    Telephone: 0.0096
    Unknown: 0.0194
06K:
  GP:
    Face-to-Face: 0.0234
    Home Visit: 0.0153
    Telephone: 0.0044
    Unknown: 0.0101
    Video/Online: 0.0186
  Other Practice staff:
    Face-to-Face: 0.0633
    Home Visit: 0.0177
    Telephone: 0.0101
    Unknown: 0.0386
    Video/Online: 0.0235
  Unknown:
    Home Visit: 0.0073
    Telephone: .nan
    Unknown: 0.0202
06L:
  GP:
    Face-to-Face: 0.0166
    Home Visit: 0.0145
    Telephone: 0.0015
    Unknown: 0.0122
    Video/Online: 0.0147
  Other Practice staff:
    Face-to-Face: 0.0464
    Home Visit: 0.0358
    Telephone: 0.0055
    Unknown: 0.0411
    Video/Online: 0.041
  Unknown:
    Unknown: 0.0221
06N:
  GP:
    Face-to-Face: 0.0397
    Home Visit: 0.0152
    Telephone: 0.0226
    Unknown: 0.0021
    Video/Online: 0.0005
  Other Practice staff:
    Face-to-Face: 0.0726
    Home Visit: 0.0141
    Telephone: 0.0531
    Unknown: .nan
    Video/Online: 0.0017
  Unknown:
    Face-to-Face: 0.0019
    Home Visit: 0.0293
    Telephone: 0.0018
    Unknown: 0.0123
06Q:
  GP:
    Face-to-Face: 0.0198
    Home Visit: 0.0378
    Telephone: 0.0072
    Unknown: 0.0373
    Video/Online: 0.0312
  Other Practice staff:
    Face-to-Face: 0.0461
    Home Visit: 0.0333
    Telephone: 0.0168
    Unknown: 0.0414
    Video/Online: 0.073
  Unknown:
    Unknown: 0.0265
06T:
  GP:
    Face-to-Face: 0.0268
    Home Visit: 0.0235
    Telephone: 0.0122
    Unknown: 0.0486
    Video/Online: 0.037
  Other Practice staff:
    Face-to-Face: 0.0568
    Home Visit: 0.0169
    Telephone: 0.0203
    Unknown: 0.0173
    Video/Online: 0.0719
  Unknown:
    Face-to-Face: 0.5313
    Home Visit: 0.0094
    Telephone: 0.0413
    Unknown: 0.036
07G:
  GP:
    Face-to-Face: 0.0254
    Home Visit: 0.0671
    Telephone: 0.0088
    Unknown: 0.0044
    Video/Online: 0.0148
  Other Practice staff:
    Face-to-Face: 0.0505
    Home Visit: .nan
    Telephone: 0.0066
    Unknown: 0.0057
    Video/Online: 0.0011
  Unknown:
    Unknown: 0.0344
07H:
  GP:
    Face-to-Face: 0.0265
    Home Visit: 0.0788
    Telephone: 0.0091
    Unknown: 0.0062
    Video/Online: 0.0811
  Other Practice staff:
    Face-to-Face: 0.059
    Home Visit: 0.0136
    Telephone: 0.0128
    Unknown: 0.0168
    Video/Online: 0.6546
  Unknown:
    Unknown: 0.0192
07K:
  GP:
    Face-to-Face: 0.0221
    Home Visit: 0.0084
    Telephone: 0.0072
    Unknown: 0.0147
    Video/Online: 0.0136
  Other Practice staff:
    Face-to-Face: 0.049
    Home Visit: 0.0658
    Telephone: 0.0127
    Unknown: 0.0213
    Video/Online: 0.0247
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0169
    Telephone: .nan
    Unknown: 0.0188
09D:
  GP:
    Face-to-Face: 0.0371
    Home Visit: 0.0168
    Telephone: 0.0127
    Unknown: 0.0143
    Video/Online: 0.0228
  Other Practice staff:
    Face-to-Face: 0.0845
    Home Visit: 0.0174
    Telephone: 0.0147
    Unknown: 0.0446
    Video/Online: 0.0056
  Unknown:
    Face-to-Face: 0.0519
    Home Visit: 0.002
    Telephone: 0.1536
    Unknown: 0.0293
10Q:
  GP:
    Face-to-Face: 0.0354
    Home Visit: 0.0196
    Telephone: 0.0227
    Unknown: .nan
    Video/Online: 0.0003
  Other Practice staff:
    Face-to-Face: 0.0698
    Home Visit: 0.0409
    Telephone: 0.038
    Unknown: .nan
    Video/Online: .nan
  Unknown:
    Face-to-Face: 0.1179
    Home Visit: 0.0207
    Telephone: 0.0027
    Video/Online: .nan
10R:
  GP:
    Face-to-Face: 0.0389
    Home Visit: .nan
    Telephone: 0.0028
    Unknown: .nan
    Video/Online: 0.007
  Other Practice staff:
    Face-to-Face: 0.0774
    Home Visit: 0.0223
    Telephone: 0.0065
    Unknown: 0.0528
    Video/Online: 0.0198
  Unknown:
    Unknown: 0.0264
11J:
  GP:
    Face-to-Face: 0.0254
    Home Visit: 0.0353
    Telephone: 0.0043
    Unknown: 0.0154
    Video/Online: 0.0102
  Other Practice staff:
    Face-to-Face: 0.054
    Home Visit: 0.0402
    Telephone: 0.0073
    Unknown: 0.0582
    Video/Online: 0.0354
  Unknown:
    Unknown: 0.0172
11M:
  GP:
    Face-to-Face: 0.0295
    Home Visit: 0.0369
    Telephone: 0.007
    Unknown: 0.0112
    Video/Online: 0.0708
  Other Practice staff:
    Face-to-Face: 0.0547
    Home Visit: 0.058
    Telephone: 0.0098
    Unknown: 0.0082
    Video/Online: 0.0316
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0059
    Telephone: 0.0143
    Unknown: 0.0179
    Video/Online: .nan
11N:
  GP:
    Face-to-Face: 0.034
    Home Visit: 0.0358
    Telephone: 0.0104
    Unknown: 0.0701
    Video/Online: 0.0036
  Other Practice staff:
    Face-to-Face: 0.0599
    Home Visit: 0.03
    Telephone: 0.0339
    Unknown: 0.0738
    Video/Online: 0.0061
  Unknown:
    Face-to-Face: 0.0032
    Home Visit: 0.0159
    Telephone: 0.0319
    Unknown: 0.0146
    Video/Online: .nan
11X:
  GP:
    Face-to-Face: 0.035
    Home Visit: 0.0206
    Telephone: 0.0279
    Unknown: 0.0167
    Video/Online: 0.0003
  Other Practice staff:
    Face-to-Face: 0.0645
    Home Visit: 0.0207
    Telephone: 0.0603
    Unknown: 0.0362
    Video/Online: 0.0001
  Unknown:
    Face-to-Face: 0.0204
    Home Visit: 0.0115
    Telephone: 0.0103
    Unknown: .nan
    Video/Online: .nan
12F:
  GP:
    Face-to-Face: 0.0414
    Home Visit: 0.0088
    Telephone: 0.0279
    Unknown: .nan
    Video/Online: 0.0034
  Other Practice staff:
    Face-to-Face: 0.0897
    Home Visit: 0.0242
    Telephone: 0.0768
    Unknown: .nan
    Video/Online: 0.0028
  Unknown:
    Face-to-Face: 0.0003
    Home Visit: 0.012
    Telephone: 0.0224
    Unknown: .nan
    Video/Online: .nan
13T:
  GP:
    Face-to-Face: 0.042
    Home Visit: 0.0522
    Telephone: 0.0171
    Unknown: 0.0049
    Video/Online: 0.0133
  Other Practice staff:
    Face-to-Face: 0.0789
    Home Visit: 0.1526
    Telephone: 0.0716
    Unknown: 0.0335
    Video/Online: 0.0114
  Unknown:
    Face-to-Face: 0.0008
    Home Visit: 0.01
    Telephone: 0.016
    Unknown: 0.0286
    Video/Online: .nan
14L:
  GP:
    Face-to-Face: 0.0586
    Home Visit: 0.0283
    Telephone: 0.0311
    Unknown: .nan
    Video/Online: 0.0002
  Other Practice staff:
    Face-to-Face: 0.1196
    Home Visit: 0.0631
    Telephone: 0.0636
    Unknown: 0.0021
    Video/Online: 0.0004
  Unknown:
    Face-to-Face: 0.0149
    Home Visit: 0.0142
    Telephone: 0.0259
    Unknown: .nan
    Video/Online: .nan
14Y:
  GP:
    Face-to-Face: 0.0331
    Home Visit: 0.0637
    Telephone: 0.0254
    Unknown: .nan
    Video/Online: 0.008
  Other Practice staff:
    Face-to-Face: 0.071
    Home Visit: 0.0206
    Telephone: 0.0376
    Unknown: 0.0038
    Video/Online: 0.0081
  Unknown:
    Face-to-Face: 0.0003
    Home Visit: 0.0085
    Telephone: 0.0046
    Unknown: 0.0235
15A:
  GP:
    Face-to-Face: 0.0347
    Home Visit: 0.0081
    Telephone: 0.0178
    Unknown: 0.055
    Video/Online: 0.0011
  Other Practice staff:
    Face-to-Face: 0.059
    Home Visit: 0.0181
    Telephone: 0.0508
    Unknown: 0.0635
    Video/Online: 0.0194
  Unknown:
    Face-to-Face: 0.0015
    Home Visit: 0.0166
    Telephone: 0.0425
    Unknown: 0.0107
    Video/Online: 0.0015
15C:
  GP:
    Face-to-Face: 0.0482
    Home Visit: 0.0231
    Telephone: 0.0211
    Unknown: 0.0301
    Video/Online: 0.0002
  Other Practice staff:
    Face-to-Face: 0.0733
    Home Visit: 0.0166
    Telephone: 0.0492
    Unknown: 0.0209
    Video/Online: 0.0004
  Unknown:
    Face-to-Face: 0.001
    Home Visit: 0.0172
    Telephone: 0.0191
    Unknown: .nan
    Video/Online: .nan
15E:
  GP:
    Face-to-Face: 0.0456
    Home Visit: 0.0321
    Telephone: 0.0207
    Unknown: 0.0505
    Video/Online: 0.0217
  Other Practice staff:
    Face-to-Face: 0.1059
    Home Visit: 0.0872
    Telephone: 0.0493
    Unknown: 0.0992
    Video/Online: 0.0373
  Unknown:
    Face-to-Face: 0.0008
    Home Visit: 0.7207
    Telephone: 0.0167
    Unknown: 0.0361
15F:
  GP:
    Face-to-Face: 0.034
    Home Visit: 0.0132
    Telephone: 0.0115
    Unknown: 0.0277
    Video/Online: 0.0249
  Other Practice staff:
    Face-to-Face: 0.0696
    Home Visit: 0.0291
    Telephone: 0.0168
    Unknown: 0.0445
    Video/Online: 0.0441
  Unknown:
    Face-to-Face: 0.001
    Home Visit: 0.0145
    Telephone: 0.0109
    Unknown: 0.0361
15M:
  GP:
    Face-to-Face: 0.0279
    Home Visit: 0.0211
    Telephone: 0.0099
    Unknown: 0.0105
    Video/Online: 0.0132
  Other Practice staff:
    Face-to-Face: 0.0569
    Home Visit: 0.0247
    Telephone: 0.0162
    Unknown: 0.0366
    Video/Online: 0.03
  Unknown:
    Face-to-Face: 0.0013
    Home Visit: .nan
    Telephone: .nan
    Unknown: 0.0224
15N:
  GP:
    Face-to-Face: 0.0334
    Home Visit: 0.0215
    Telephone: 0.0117
    Unknown: 0.0123
    Video/Online: 0.0143
  Other Practice staff:
    Face-to-Face: 0.0576
    Home Visit: 0.0247
    Telephone: 0.0179
    Unknown: 0.0541
    Video/Online: 0.0403
  Unknown:
    Face-to-Face: 0.0014
    Home Visit: 0.0033
    Telephone: 0.0014
    Unknown: 0.0168
16C:
  GP:
    Face-to-Face: 0.0324
    Home Visit: 0.0167
    Telephone: 0.0098
    Unknown: 0.0214
    Video/Online: 0.024
  Other Practice staff:
    Face-to-Face: 0.0749
    Home Visit: 0.0539
    Telephone: 0.0157
    Unknown: 0.0392
    Video/Online: 0.0773
  Unknown:
    Face-to-Face: 0.0009
    Home Visit: 0.0065
    Telephone: 0.0238
    Unknown: 0.035
    Video/Online: .nan
18C:
  GP:
    Face-to-Face: 0.0323
    Home Visit: 0.0119
    Telephone: 0.0223
    Unknown: 0.0011
    Video/Online: 0.0001
  Other Practice staff:
    Face-to-Face: 0.0586
    Home Visit: 0.0137
    Telephone: 0.0527
    Unknown: 0.001
    Video/Online: 0.0005
  Unknown:
    Face-to-Face: 0.0017
    Home Visit: 0.0034
    Telephone: 0.0443
    Unknown: .nan
    Video/Online: .nan
26A:
  GP:
    Face-to-Face: 0.0304
    Home Visit: 0.0129
    Telephone: 0.0058
    Unknown: 0.0183
    Video/Online: 0.0261
  Other Practice staff:
    Face-to-Face: 0.0557
    Home Visit: 0.0332
    Telephone: 0.0177
    Unknown: 0.0318
    Video/Online: 0.0523
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0099
    Telephone: .nan
    Unknown: 0.0197
27D:
  GP:
    Face-to-Face: 0.0366
    Home Visit: 0.1014
    Telephone: 0.029
    Unknown: 0.0181
    Video/Online: 0.0035
  Other Practice staff:
    Face-to-Face: 0.0782
    Home Visit: 0.0151
    Telephone: 0.0661
    Unknown: 0.0313
    Video/Online: 0.0004
  Unknown:
    Face-to-Face: 0.0023
    Home Visit: 0.0152
    Telephone: 0.0589
    Unknown: .nan
    Video/Online: .nan
36J:
  GP:
    Face-to-Face: 0.0225
    Home Visit: 0.0214
    Telephone: 0.0062
    Unknown: 0.0143
    Video/Online: 0.0068
  Other Practice staff:
    Face-to-Face: 0.0542
    Home Visit: 0.0147
    Telephone: 0.0074
    Unknown: 0.0129
    Video/Online: 0.0211
  Unknown:
    Unknown: 0.0225
36L:
  GP:
    Face-to-Face: 0.0518
    Home Visit: 0.0132
    Telephone: 0.0224
    Unknown: 0.0317
    Video/Online: 0.0035
  Other Practice staff:
    Face-to-Face: 0.0983
    Home Visit: 0.0335
    Telephone: 0.0621
    Unknown: 0.0307
    Video/Online: 0.0003
  Unknown:
    Face-to-Face: 0.0088
    Home Visit: 0.0299
    Telephone: 0.0857
    Unknown: .nan
    Video/Online: .nan
42D:
  GP:
    Face-to-Face: 0.0261
    Home Visit: 0.0124
    Telephone: 0.0063
    Unknown: 0.0185
    Video/Online: 0.0143
  Other Practice staff:
    Face-to-Face: 0.0466
    Home Visit: 0.0542
    Telephone: 0.0086
    Unknown: 0.0337
    Video/Online: 0.0205
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0029
    Telephone: .nan
    Unknown: 0.0187
52R:
  GP:
    Face-to-Face: 0.035
    Home Visit: 0.0169
    Telephone: 0.0079
    Unknown: 0.0529
    Video/Online: 0.0367
  Other Practice staff:
    Face-to-Face: 0.0691
    Home Visit: 0.0619
    Telephone: 0.0177
    Unknown: 0.0765
    Video/Online: 0.0539
  Unknown:
    Face-to-Face: .nan
    Unknown: 0.0291
70F:
  GP:
    Face-to-Face: 0.0267
    Home Visit: 0.0125
    Telephone: 0.0054
    Unknown: 0.0246
    Video/Online: 0.0102
  Other Practice staff:
    Face-to-Face: 0.0536
    Home Visit: 0.0204
    Telephone: 0.0161
    Unknown: 0.0253
    Video/Online: 0.0705
  Unknown:
    Face-to-Face: 0.0161
    Home Visit: 0.0051
    Telephone: .nan
    Unknown: 0.0188
    Video/Online: .nan
71E:
  GP:
    Face-to-Face: 0.0239
    Home Visit: 0.0304
    Telephone: 0.0076
    Unknown: 0.0175
    Video/Online: 0.0082
  Other Practice staff:
    Face-to-Face: 0.0555
    Home Visit: 0.0239
    Telephone: 0.0145
    Unknown: 0.033
    Video/Online: 0.0182
  Unknown:
    Face-to-Face: .nan
    Home Visit: .nan
    Telephone: .nan
    Unknown: 0.0244
72Q:
  GP:
    Face-to-Face: 0.0541
    Home Visit: 0.0177
    Telephone: 0.0297
    Unknown: 0.0221
    Video/Online: 0.0008
  Other Practice staff:
    Face-to-Face: 0.1154
    Home Visit: 0.0347
    Telephone: 0.0493
    Unknown: 0.0599
    Video/Online: 0.0047
  Unknown:
    Face-to-Face: 0.0016
    Home Visit: 0.0501
    Telephone: 0.013
    Unknown: .nan
    Video/Online: .nan
78H:
  GP:
    Face-to-Face: 0.0249
    Home Visit: 0.013
    Telephone: 0.0071
    Unknown: 0.0551
    Video/Online: 0.0087
  Other Practice staff:
    Face-to-Face: 0.0549
    Home Visit: 0.0368
    Telephone: 0.0139
    Unknown: 0.0313
    Video/Online: 0.0623
  Unknown:
    Face-to-Face: 0.024
    Home Visit: 0.0095
    Telephone: 0.0145
    Unknown: 0.019
84H:
  GP:
    Face-to-Face: 0.025
    Home Visit: 0.0737
    Telephone: 0.0099
    Unknown: 0.0145
    Video/Online: 0.0066
  Other Practice staff:
    Face-to-Face: 0.0555
    Home Visit: 0.0292
    Telephone: 0.0154
    Unknown: 0.0488
    Video/Online: 0.0461
  Unknown:
    Telephone: .nan
    Unknown: 0.0226
91Q:
  GP:
    Face-to-Face: 0.0423
    Home Visit: 0.0217
    Telephone: 0.0142
    Unknown: 0.0207
    Video/Online: 0.0023
  Other Practice staff:
    Face-to-Face: 0.0739
    Home Visit: 0.0204
    Telephone: 0.0456
    Unknown: 0.052
    Video/Online: 0.0029
  Unknown:
    Face-to-Face: 0.0042
    Home Visit: 0.0393
    Telephone: 0.0092
    Unknown: .nan
    Video/Online: .nan
92A:
  GP:
    Face-to-Face: 0.0349
    Home Visit: 0.0154
    Telephone: 0.0266
    Unknown: 0.0136
    Video/Online: 0.0
  Other Practice staff:
    Face-to-Face: 0.0649
    Home Visit: 0.0204
    Telephone: 0.0362
    Unknown: 0.025
    Video/Online: 0.0
  Unknown:
    Face-to-Face: 0.0059
    Home Visit: 0.013
    Telephone: 0.0768
    Unknown: 0.0193
    Video/Online: .nan
92G:
  GP:
    Face-to-Face: 0.0245
    Home Visit: 0.0096
    Telephone: 0.0033
    Unknown: 0.0219
    Video/Online: 0.0129
  Other Practice staff:
    Face-to-Face: 0.0522
    Home Visit: 0.022
    Telephone: 0.0073
    Unknown: 0.0275
    Video/Online: 0.0308
  Unknown:
    Face-to-Face: 0.0044
    Telephone: 0.0043
    Unknown: 0.0188
93C:
  GP:
    Face-to-Face: 0.0549
    Home Visit: 0.0126
    Telephone: 0.0241
    Unknown: 0.0023
    Video/Online: 0.0014
  Other Practice staff:
    Face-to-Face: 0.1088
    Home Visit: 0.0926
    Telephone: 0.0533
    Unknown: 0.0003
    Video/Online: 0.0003
  Unknown:
    Face-to-Face: 0.0111
    Home Visit: 0.0112
    Telephone: 0.0025
    Unknown: .nan
    Video/Online: .nan
97R:
  GP:
    Face-to-Face: 0.0298
    Home Visit: 0.0195
    Telephone: 0.0238
    Unknown: 0.0033
    Video/Online: 0.0043
  Other Practice staff:
    Face-to-Face: 0.0638
    Home Visit: 0.0237
    Telephone: 0.0394
    Unknown: 0.0051
    Video/Online: 0.0026
  Unknown:
    Face-to-Face: 0.0022
    Home Visit: 0.0242
    Telephone: 0.0165
    Unknown: 0.0255
99A:
  GP:
    Face-to-Face: 0.0452
    Home Visit: 0.0138
    Telephone: 0.031
    Unknown: 0.0233
    Video/Online: .nan
  Other Practice staff:
    Face-to-Face: 0.1167
    Home Visit: 0.0484
    Telephone: 0.0813
    Unknown: 0.0057
    Video/Online: 0.0022
  Unknown:
    Face-to-Face: 0.0032
    Home Visit: 0.0099
    Telephone: 0.0376
    Unknown: .nan
    Video/Online: .nan
99C:
  GP:
    Face-to-Face: 0.0296
    Home Visit: 0.0346
    Telephone: 0.0204
    Unknown: 0.0061
    Video/Online: 0.0054
  Other Practice staff:
    Face-to-Face: 0.0691
    Home Visit: 0.0188
    Telephone: 0.0505
    Unknown: 0.01
    Video/Online: 0.0754
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0627
    Telephone: 0.0058
    Unknown: 0.0259
99E:
  GP:
    Face-to-Face: 0.0178
    Home Visit: .nan
    Telephone: 0.004
    Unknown: 0.0035
    Video/Online: 0.0392
  Other Practice staff:
    Face-to-Face: 0.0411
    Home Visit: 0.0005
    Telephone: 0.0068
    Unknown: 0.0155
    Video/Online: 0.0346
  Unknown:
    Unknown: 0.0273
99F:
  GP:
    Face-to-Face: 0.0261
    Home Visit: 0.0286
    Telephone: 0.0099
    Unknown: 0.0341
    Video/Online: 0.0369
  Other Practice staff:
    Face-to-Face: 0.0435
    Home Visit: 0.0256
    Telephone: 0.0069
    Unknown: 0.0164
    Video/Online: 0.0414
  Unknown:
    Unknown: 0.028
99G:
  GP:
    Face-to-Face: 0.0262
    Home Visit: 0.002
    Telephone: 0.0172
    Unknown: 0.0288
    Video/Online: 0.018
  Other Practice staff:
    Face-to-Face: 0.075
    Home Visit: 0.0084
    Telephone: 0.0131
    Unknown: 0.0204
    Video/Online: 0.0717
  Unknown:
    Unknown: 0.0385
A3A8R:
  GP:
    Face-to-Face: 0.0524
    Home Visit: 0.0194
    Telephone: 0.0286
    Unknown: 0.0085
    Video/Online: 0.0032
  Other Practice staff:
    Face-to-Face: 0.1196
    Home Visit: 0.0295
    Telephone: 0.0524
    Unknown: 0.002
    Video/Online: 0.0022
  Unknown:
    Face-to-Face: 0.0026
    Home Visit: 0.0572
    Telephone: 0.0407
    Unknown: 0.0301
    Video/Online: .nan
B2M3M:
  GP:
    Face-to-Face: 0.0407
    Home Visit: 0.0092
    Telephone: 0.0196
    Unknown: .nan
    Video/Online: 0.0004
  Other Practice staff:
    Face-to-Face: 0.0829
    Home Visit: 0.013
    Telephone: 0.0482
    Unknown: 0.0007
    Video/Online: 0.0018
  Unknown:
    Face-to-Face: 0.0076
    Home Visit: 0.0055
    Telephone: 0.0089
    Unknown: .nan
    Video/Online: .nan
D2P2L:
  GP:
    Face-to-Face: 0.0485
    Home Visit: 0.0171
    Telephone: 0.022
    Unknown: 0.0288
    Video/Online: 0.009
  Other Practice staff:
    Face-to-Face: 0.0967
    Home Visit: 0.0237
    Telephone: 0.0568
    Unknown: 0.0334
    Video/Online: 0.0735
  Unknown:
    Face-to-Face: 0.0009
    Home Visit: 0.0099
    Telephone: 0.0024
    Unknown: 0.0423
    Video/Online: .nan
D4U1Y:
  GP:
    Face-to-Face: 0.0546
    Home Visit: 0.0123
    Telephone: 0.0391
    Unknown: 0.0068
    Video/Online: 0.0037
  Other Practice staff:
    Face-to-Face: 0.0862
    Home Visit: 0.022
    Telephone: 0.0476
    Unknown: 0.0379
    Video/Online: 0.0008
  Unknown:
    Face-to-Face: .nan
    Home Visit: 0.0134
    Telephone: .nan
    Unknown: .nan
    Video/Online: .nan
D9Y0V:
  GP:
    Face-to-Face: 0.0321
    Home Visit: 0.0136
    Telephone: 0.0443
    Unknown: 0.0172
    Video/Online: 0.0031
  Other Practice staff:
    Face-to-Face: 0.066
    Home Visit: 0.0229
    Telephone: 0.0393
    Unknown: 0.0417
    Video/Online: 0.0342
  Unknown:
    Face-to-Face: 0.0011
    Home Visit: 0.0128
    Telephone: 0.0511
    Unknown: 0.0285
    Video/Online: .nan
M1J4Y:
  GP:
    Face-to-Face: 0.0302
    Home Visit: 0.0235
    Telephone: 0.0062
    Unknown: 0.0313
    Video/Online: 0.0326
  Other Practice staff:
    Face-to-Face: 0.0683
    Home Visit: 0.0456
    Telephone: 0.0124
    Unknown: 0.0418
    Video/Online: 0.0542
  Unknown:
    Unknown: 0.0308
M2L0M:
  GP:
    Face-to-Face: 0.0329
    Home Visit: 0.0224
    Telephone: 0.0144
    Unknown: 0.0472
    Video/Online: 0.0002
  Other Practice staff:
    Face-to-Face: 0.0587
    Home Visit: 0.0341
    Telephone: 0.0378
    Unknown: 0.0678
    Video/Online: 0.0004
  Unknown:
    Face-to-Face: 0.0029
    Home Visit: 0.0828
    Telephone: 0.0057
    Unknown: .nan
    Video/Online: .nan
W2U3Z:
  GP:
    Face-to-Face: 0.0426
    Home Visit: 0.0272
    Telephone: 0.0187
    Unknown: 0.0125
    Video/Online: 0.0351
  Other Practice staff:
    Face-to-Face: 0.0906
    Home Visit: 0.0869
    Telephone: 0.0367
    Unknown: 0.0313
    Video/Online: 0.0832
  Unknown:
    Face-to-Face: 0.0069
    Home Visit: 0.0263
    Telephone: 0.0018
    Unknown: 0.0328
    Video/Online: 0.0625
X2C4Y:
  GP:
    Face-to-Face: 0.0266
    Home Visit: 0.0133
    Telephone: 0.0095
    Unknown: 0.0599
    Video/Online: 0.0285
  Other Practice staff:
    Face-to-Face: 0.0511
    Home Visit: 0.0122
    Telephone: 0.0097
    Unknown: 0.0428
    Video/Online: 0.0423
  Unknown:
    Face-to-Face: .nan
    Unknown: 0.0306
```