Title: Appointments
Date: 2024-01-04
Modified: 2024-10-11
Category: Capacity Analysis
Authors: A.Jarman & I.Khan
Summary: Analysis on primary care appointments (Attended/DNA) in SNEE-ICB

<br>

## Introduction & Background
Understanding the frequency of missed appointments in SNEE footprints is crucial.  This analysis endeavors to construct a model that captures the instances of missed appointments, allowing patients to re-enter the system at a later date.
<br><br>

## Data Sources
The primary data for this analysis is derived from the extensive appointments dataset provided by NHS England, spanning from April 2021 to August 2023. While FY21 and FY22 were based on complete annual data, the assessment for FY23 is limited to the available data from April to August.
<table>
    <thead>
        <tr>
            <th>Dataset used</th>
            <th>Website URL</th>
            <th>Download zip</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Appointments dataset</td>
            <td><a href="https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice">NHS Digital - Appointments in General Practice</a></td>
            <td><a href="https://files.digital.nhs.uk/D5/4B437E/Appointments_GP_Regional_CSV_Aug_24.zip">Regional CSV SuffolkNEEssex (Mar22 - Aug24)</a></td>
        </tr>
    </tbody>
</table>
<br>


## Methodology
Before the analysis, the data was pre-processed. 

- Appointment months were converted into FY-years.
- Calculated the national averages and proportional representation for each appointment type.

1- Comparison with SNEE Area:

- Conducted a comparative analysis between the national averages and proportions with the SNEE area for fiscal years 2022, 2023, and 2024.
- Visualized the results through detailed comparison plots.

2- Detailed Proportion Analysis:

- Extracted proportions of attended, did not attend (DNA), and unknown appointments based on SUB-ICB, healthcare professional type (hcp_type), and appointment mode.
- Plotted the changes in did not attend (DNA) appointments over the years.

3- Correlation Matrix:

- Conducted a correlation matrix analysis to identify factors affecting the likelihood of DNA appointments  in the SNEE area.

4- Identifying Appointment Trends:

- Explored if certain appointments are more likely to be missed.
- Conducted additional analysis on appointment types with higher likelihood of being missed.

This approach involves a comprehensive examination of various factors influencing appointment attendance, utilizing visualizations for better understanding. This structured analysis should provide valuable insights into missed appointments trends and potential influencing factors in the SNEE area.
<br><br>

## Results and inferences 

### 1. Missed Appointments Comparison of Proportion and Average (per month): SNEE-ICB and National average

<table>
  <thead>
    <tr>
      <th rowspan="2">Year</th>
      <th colspan="2">Attended (Count, %)</th>
      <th colspan="2">DNA (Count, %)</th>
      <th colspan="2">Unknown (Count, %)</th>
    </tr>
    <tr>
      <th>Nation wide</th>
      <th>SNEE</th>
      <th>Nation wide</th>
      <th>SNEE</th>
      <th>Nation wide</th>
      <th>SNEE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>FY-2022</td>
      <td>608,099 (91.21%)</td>
      <td>465,022 (93.22%)</td>
      <td>31,569 (4.63%)</td>
      <td>17,823 (3.51%)</td>
      <td>27,096 (4.17%)</td>
      <td>16,936 (3.27%)</td>
    </tr>
    <tr>
      <td>FY-2023</td>
      <td>628,297 (90.04%)</td>
      <td>481,801 (91.84%)</td>
      <td>31,723 (4.45%)</td>
      <td>16,480 (3.11%)</td>
      <td>38,692 (5.51%)</td>
      <td>27,284 (5.06%)</td>
    </tr>
    <tr>
      <td>FY-2024 (Apr-Aug)</td>
      <td>629,349 (90.06%)</td>
      <td>493,590 (92.03%)</td>
      <td>30,356 (4.22%)</td>
      <td>15,572 (2.88%)</td>
      <td>40,010 (5.72%)</td>
      <td>27,752 (5.09%)</td>
    </tr>
  </tbody>
</table>
<br>

Based on the above table:

- The average percentage of **DNA appointments** for SNEE-ICB is consistently **lower** than the National Average across all observed years
- Conversely, the average percentage of **Attended appointments** for SNEE-ICB is consistently **higher** than the National Average for each year, suggesting a more favorable attendance trend in SNEE.
Overall, these findings highlight the effectiveness of SNEE-ICB's initiatives in reducing missed appointments while promoting higher attendance rates compared to the national landscape.<br>

We can confirm the lower average of (Attended/DNA) AppointmentsSNEE compared to other ICB'S from the graph below
<br>

![Average appointments]({attach}/img/appointment_attendance_1.png)

<br>

### Breaking Down Appointment Trends by SNEE Sub-ICB Areas
<table>
  <tr>
    <th>SUB_ICB_LOCATION_CODE</th>
    <th>FY_YEAR</th>
    <th>Attended (%)</th>
    <th>DNA (%)</th>
    <th>Unknown (%)</th>
  </tr>
  <tr>
    <td rowspan="3">Ipswich & East Suffolk (06L)</td>
    <td>FY2022</td>
    <td>93.62%</td>
    <td>2.79%</td>
    <td>3.59%</td>
  </tr>
  <tr>
    <td>FY2023</td>
    <td>91.44%</td>
    <td>2.79%</td>
    <td>5.77%</td>
  </tr>
  <tr>
    <td>FY2024</td>
    <td>92.04%</td>
    <td>2.50%</td>
    <td>5.46%</td>
  </tr>
  <tr>
    <td rowspan="3">North East Essex (06T)</td>
    <td>FY2022</td>
    <td>91.16%</td>
    <td>4.91%</td>
    <td>3.92%</td>
  </tr>
  <tr>
    <td>FY2023</td>
    <td>90.65%</td>
    <td>3.85%</td>
    <td>5.50%</td>
  </tr>
  <tr>
    <td>FY2024</td>
    <td>90.38%</td>
    <td>3.79%</td>
    <td>5.83%</td>
  </tr>
  <tr>
    <td rowspan="3">West Suffolk (07K)</td>
    <td>FY2022</td>
    <td>94.88%</td>
    <td>2.84%</td>
    <td>2.29%</td>
  </tr>
  <tr>
    <td>FY2023</td>
    <td>93.42%</td>
    <td>2.68%</td>
    <td>3.90%</td>
  </tr>
  <tr>
    <td>FY2024</td>
    <td>93.67%</td>
    <td>2.36%</td>
    <td>3.97%</td>
  </tr>
</table>

- The sub-ICB North East Essex (06T) demonstrates the highest proportion of DNA appointments, suggesting a significant challenge in managing appointment attendance within this region.
- Conversely, the sub-ICB West Suffolk (07K) exhibits the maximum proportion of Attended appointments, indicating a strong performance in appointment adherence.
<br><br>


### 2. Appointment Trends Over Time/Years

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_5.png)

We can infer that -

- Nationally the missed appointments are consistent over years when appointment mode is Face to Face, home visit or telephonic.
- Nationally inconsistencies is observed in appointments with unknown or video/online modes over the years.

- Below graph represents the same information for SNEE-ICB areas

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_7.png)

<br><br>


### 3. To understand if Across staff groups & Sub-ICB, are some appointments more likely to be missed/attended

**Below table shows the comaparison between proportion of appointments (Attended,DNA and Unknown) National vs SNEE, based on HCP type and Appointment mode**

<table>
  <tr>
    <th colspan="2">TYPE</th>
    <th colspan="2">Attended</th>
    <th colspan="2">DNA</th>
    <th colspan="2">Unknown</th>
  </tr>
  <tr>
    <th>HCP_TYPE</th>
    <th>APPT_MODE</th>
    <th>National</th>
    <th>SNEE</th>
    <th>National</th>
    <th>SNEE</th>
    <th>National</th>
    <th>SNEE</th>
  </tr>
  <tr>
    <td rowspan="5">GP</td>
    <td>Face-to-Face</td>
    <td>93.02%</td>
    <td>94.93%</td>
    <td>3.61%</td>
    <td>2.21%</td>
    <td>3.37%</td>
    <td>2.86%</td>
  </tr>
  <tr>
    <td>Home Visit</td>
    <td>84.79%</td>
    <td>94.10%</td>
    <td>2.02%</td>
    <td>1.48%</td>
    <td>13.20%</td>
    <td>4.42%</td>
  </tr>
  <tr>
    <td>Telephone</td>
    <td>95.14%</td>
    <td>97.31%</td>
    <td>1.64%</td>
    <td>0.65%</td>
    <td>3.22%</td>
    <td>2.04%</td>
  </tr>
  <tr>
    <td>Unknown</td>
    <td>50.21%</td>
    <td>54.27%</td>
    <td>2.15%</td>
    <td>2.32%</td>
    <td>47.63%</td>
    <td>43.41%</td>
  </tr>
  <tr>
    <td>Video/Online</td>
    <td>89.91%</td>
    <td>93.06%</td>
    <td>0.80%</td>
    <td>0.88%</td>
    <td>9.30%</td>
    <td>6.06%</td>
  </tr>
  <tr>
    <td rowspan="5">Other Practice Staff</td>
    <td>Face-to-Face</td>
    <td>87.68%</td>
    <td>89.53%</td>
    <td>6.99%</td>
    <td>4.95%</td>
    <td>5.33%</td>
    <td>5.52%</td>
  </tr>
  <tr>
    <td>Home Visit</td>
    <td>82.84%</td>
    <td>89.38%</td>
    <td>3.16%</td>
    <td>3.22%</td>
    <td>14.01%</td>
    <td>7.40%</td>
  </tr>
  <tr>
    <td>Telephone</td>
    <td>92.03%</td>
    <td>95.14%</td>
    <td>3.38%</td>
    <td>1.20%</td>
    <td>4.59%</td>
    <td>3.66%</td>
  </tr>
  <tr>
    <td>Unknown</td>
    <td>41.40%</td>
    <td>47.27%</td>
    <td>2.94%</td>
    <td>3.10%</td>
    <td>55.67%</td>
    <td>49.63%</td>
  </tr>
  <tr>
    <td>Video/Online</td>
    <td>89.44%</td>
    <td>93.37%</td>
    <td>1.39%</td>
    <td>2.87%</td>
    <td>9.17%</td>
    <td>3.76%</td>
  </tr>
  <tr>
    <td rowspan="5">Unknown</td>
    <td>Face-to-Face</td>
    <td>75.70%</td>
    <td>41.70%</td>
    <td>2.29%</td>
    <td>49.28%</td>
    <td>24.33%</td>
    <td>9.02%</td>
  </tr>
  <tr>
    <td>Home Visit</td>
    <td>67.79%</td>
    <td>89.15%</td>
    <td>3.80%</td>
    <td>0.92%</td>
    <td>30.63%</td>
    <td>9.93%</td>
  </tr>
  <tr>
    <td>Telephone</td>
    <td>90.15%</td>
    <td>93.40%</td>
    <td>2.35%</td>
    <td>3.82%</td>
    <td>10.79%</td>
    <td>2.77%</td>
  </tr>
  <tr>
    <td>Unknown</td>
    <td>74.19%</td>
    <td>90.67%</td>
    <td>2.27%</td>
    <td>2.26%</td>
    <td>31.84%</td>
    <td>7.06%</td>
  </tr>
  <tr>
    <td>Video/Online</td>
    <td>79.00%</td>
    <td>100.00%</td>
    <td>2.73%</td>
    <td>2.76%</td>
    <td>21.19%</td>
    <td>18.84%</td>
  </tr>
</table>

**Major Highlights**

- SNEE consistently outperforms national averages across most appointment modes and HCP types, especially in home visits and telephone appointments.
- Face-to-Face Appointments: High attendance rates with low DNA rates, but a small percentage of unknown outcomes.
- Home Visits: Moderate attendance rates with low DNA rates, but a notable percentage of unknown outcomes.
- Telephone Appointments: Very high attendance rates with minimal DNA rates and low unknown outcomes.
- Unknown Mode: Low attendance rates with a high percentage of unknown outcomes, indicating a need for better tracking.
- Video/Online Appointments: High attendance rates with very low DNA rates and a moderate percentage of unknown outcomes

### Graphical representation for the above table

**Nation Wide**

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_4.png)

**SNEE-ICB**

![DNA-FY(21-22-23)]({attach}/img/appointment_attendance_8.png)

<br><br>


### 4. Likelihood of Missing Appointments: from a combination of Sub-ICB, Staff type, Appointment type.

- To understand this in detail, we have generated a Correlation matrix between all the indicators under SNEE-ICB areas.
- Correlation between variables signifies the degree and direction of the relationship between them. It measures how changes in one variable correspond to changes in another.
Correlation is measured on a scale from -1 to 1:
- Close to 1 shows a strong positive relationship: both variables move in the same direction or increase together.
- Close to -1 indicates a strong negative relationship: the variables move in opposite directions, means as one variable goes up, the other tends to go down.
- Around 0 suggests a weak or no clear relationship between the variables.

<table> <tr> <th>Feature</th> <th>Coefficient</th> </tr> <tr> <td>Appointment Mode: Face-to-Face</td> <td>0.133321</td> </tr> <tr> <td>Appointment Mode: Unknown</td> <td>0.112205</td> </tr> <tr> <td>HCP Type: Other Practice Staff</td> <td>0.099106</td> </tr> <tr> <td>HCP Type: Unknown</td> <td>0.096461</td> </tr> <tr> <td>SUB ICB Location Code: 06L</td> <td>0.050065</td> </tr> <tr> <td>SUB ICB Location Code: 06T</td> <td>0.039058</td> </tr> <tr> <td>Appointment Mode: Video/Online</td> <td>-0.047138</td> </tr> <tr> <td>Appointment Mode: Home Visit</td> <td>-0.082667</td> </tr> <tr> <td>SUB ICB Location Code: 07K</td> <td>-0.090500</td> </tr> <tr> <td>Appointment Mode: Telephone</td> <td>-0.117008</td> </tr> <tr> <td>HCP Type: GP</td> <td>-0.175618</td> </tr> </table>

- In summary, **Appointment mode:Face-to-Face/Unknown**, **HCP Type: Unkown/Other practice staff**, and specific location codes **like '06L'** have **positive correlations** with **DNA** appointments, indicating that these factors increase the chances of appointment being missed. 
- While **HCP Type:GPs**, **Appointment mode: home visits/telephone**, and specific location codes **like '07K'** have weak negative correlations, therefore these factors will decrease the chances of appointment being missed
<br><br>


### 5. Creating YAML for results

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