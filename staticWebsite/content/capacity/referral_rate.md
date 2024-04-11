Title: Primary Care Referral Rate in SNEE
Date: 2024-01-04
Modified: 2024-01-04
Category: Capacity
Tags: capacity, snee, referrals
Slug: Referral-rate
Authors: Ibrahim
Summary: Primary Care referral rates analysis


## Introduction & Background
The referral rate, calculated as the number of referrals divided by the total number of appointments per year, is a critical metric in understanding healthcare dynamics. In this analysis, our focus is on comprehending the volume of referrals originating from each sub-ICB (Integrated Care Board) under SNEE (Suffolk and North East Essex) that remain within the area (ESNEFT and WSFT) and those extending beyond its borders.



## Data Sources
For this analysis, the primary data sources utilized were NHS England's referrals and appointments datasets, predominantly encompassing data points from September 2022 to August 2023.

- Referrals dataset --> [NHS England - Outpatient Referrals](https://www.england.nhs.uk/statistics/statistical-work-areas/outpatient-referrals/)    
- Appointments dataset --> [NHS Digital - Appointments in General Practice](https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice)



## Methodology
The initial step involved filtering the referrals dataset to collate the total number of referrals directed to all ICBs between September 2022 and August 2023 within the three SNEE areas—namely, Ipswich & East Suffolk (06L), West Suffolk (07K), and North East Essex (06T). Simultaneously, the appointments dataframe underwent a cleaning process where 'Unknown' entries under HCP-type were replaced with 'Other practice staff'. Subsequently, this dataset was filtered akin to the referrals dataset.

Upon preparing both datasets, the referral rate for each SNEE-ICB area was computed by dividing the referrals dataset by the appointments dataset. The resulting table, included at the conclusion of this document, outlines the referral rates for each SNEE SUB-ICB area concerning GP and Other practice staff.



## Insights through Sankey Diagram
Interpretation of the data via a Sankey Diagram revealed noteworthy insights:

- The sub-ICB, Ipswich & East Suffolk, demonstrated the highest volume of referrals in comparison to the other two sub-ICBs.
- Post SNEE-ICB, the highest number of referrals by both GPs and Other practice staff were directed towards the 'Cambridgeshire and Peterborough ICB'.

![GP-referrals]({attach}/img/Referral_rate_4.png)

![others-referrals]({attach}/img/Referral_rate_6.png "image Title")



## Results
The results were set of referrals rates which can be re-created during simulation runs. This is saved to a `yaml` file which is then easily read by the simulation application using a built in python package.
```yaml
06L:
  GP_Ref_rate: 0.0971
  Others_Ref_rate: 0.0506
06T:
  GP_Ref_rate: 0.0586
  Others_Ref_rate: 0.0322
07K:
  GP_Ref_rate: 0.0679
  Others_Ref_rate: 0.0644
```

<table>
  <caption>Referrals Rate</caption>
  <thead>
    <tr>
      <th style="border: 1px solid black; text-align: center;">Sub_ICB_Code</th>
      <th style="border: 1px solid black; text-align: center;">GP_Ref_rate</th>
      <th style="border: 1px solid black; text-align: center;">Others_Ref_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black;">06L - (Ipswich & East Suffolk)</td>
      <td style="border: 1px solid black; text-align: center;">0.097135</td>
      <td style="border: 1px solid black; text-align: center;">0.050638</td>
    </tr>
    <tr>
      <td style="border: 1px solid black;">06T - (North East Essex)</td>
      <td style="border: 1px solid black; text-align: center;">0.058573</td>
      <td style="border: 1px solid black; text-align: center;">0.032213</td>
    </tr>
    <tr>
      <td style="border: 1px solid black;">07K - (West Suffolk)</td>
      <td style="border: 1px solid black; text-align: center;">0.067881</td>
      <td style="border: 1px solid black; text-align: center;">0.064361</td>
    </tr>
  </tbody>
</table>