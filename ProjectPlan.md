# Final Project Plan
#### Team Individual: Ethan Hung
---

## Overview: 

This project investigates how a person’s role in a traffic crash relates to the severity of injuries they experience in Chicago. Using two publicly available datasets from the Chicago Data Portal—Traffic Crashes – Crashes and Traffic Crashes – People—the goal is to identify patterns in injury outcomes across different types of road users.

The approach involves three main steps. First, the datasets will be cleaned and integrated using the shared identifier CRASH_RECORD_ID, linking crash-level information with person-level injury data. Second, exploratory data analysis will be conducted to examine the distribution of injury severity across different person types, including drivers, passengers, pedestrians, and bicyclists.

By focusing on differences in injury outcomes across these groups, the project aims to provide insight into how exposure and level of protection relate to injury severity in traffic crashes.
---

## Team: 

This project is completed individually by Ethan Hung. All responsibilities across data acquisition, cleaning, integration, analysis, and documentation will be handled independently.

Ethan Hung: Will work with both the Traffic Crashes – People dataset and the Traffic Crashes – Crashes dataset and focus on cleaning and organizing both person-level and crash-level data. I will handle variables such as PERSON_TYPE, CRASH_RECORD_ID, and INJURY_CLASSIFICATION from the People dataset, as well as variables like WEATHER_CONDITION, FIRST_CRASH_TYPE, and ROADWAY_SURFACE_COND from the Crashes dataset.

I will be responsible for standardizing key fields, handling missing values, and removing variables with high levels of missingness or low relevance to the research question. I will integrate the two datasets using CRASH_RECORD_ID, ensuring that person-level records are preserved through a left join and correctly aligned with crash-level conditions.

I will also conduct exploratory data analysis and create visualizations to compare injury severity distributions across different person types, ensuring that the datasets are correctly linked and consistent across different levels of detail.
---

## Research or Business Question: 

How does a person’s role in a crash relate to the severity of injuries they experience in Chicago traffic crashes?

This project will focus on analyzing whether different types of road users—drivers, passengers, pedestrians, and bicyclists—experience different levels of injury severity. The analysis will combine the Traffic Crashes – People dataset and the Traffic Crashes – Crashes dataset using CRASH_RECORD_ID to link individual-level injury outcomes with crash-level conditions.

Injury severity will be measured using the INJURY_CLASSIFICATION variable, and comparisons will be made across person types (PERSON_TYPE). Rather than relying on raw counts, proportional distributions will be used to account for differences in group size and provide a more meaningful comparison.

The expected outputs include:
- Proportional comparisons of injury severity across person types  
- Summary tables showing injury distributions  
- Visualizations illustrating differences in injury outcomes across groups  
---

## Datasets:
  
 ### Dataset 1: Traffic Crashes – People
    
  - Source: City of Chicago Data Portal
  
  - Link: https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d/about_data 
  
  - Variable Examples: PERSON_ID, PERSON_TYPE, CRASH_RECORD_ID, VEHICLE_ID, CRASH_DATE, SEAT_NO, CITY, STATE, ZIPCODE, SEX, AGE, DRIVERS_LICENSE_STATE, DRIVERS_LICENSE_CLASS, SAFETY_EQUIPMENT, AIRBAG_DEPLOYED, EJECTION, INJURY_CLASSIFICATION, HOSPITAL, EMS_AGENCY, EMS_RUN_NO, DRIVER_ACTION, DRIVER_VISION, PHYSICAL_CONDITION, PEDPEDAL_ACTION, PEDPEDAL_VISIBILITY, PEDPEDAL_LOCATION, BAC_RESULT, BAC_RESULT_VALUE, CELL_PHONE_USE

  - Description: The Traffic Crashes – People dataset contains information about individuals involved in traffic crashes in Chicago and whether they were injured. Each row represents one person involved in a crash, including drivers, passengers, pedestrians, or cyclists. The dataset includes characteristics such as age, gender, safety equipment use, airbag deployment, and injury classification. Records can be linked to crash events and vehicles using the shared CRASH_RECORD_ID, allowing analysis of how crash conditions and vehicle involvement relate to injuries.

 ### Dataset 2: Traffic Crashes - Crashes
  
  - Source: City of Chicago Data Portal
    
  - Link: https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data
    
  - Variable Examples: CRASH_RECORD_ID, CRASH_DATE_EST_I, CRASH_DATE, POSTED_SPEED_LIMIT, TRAFFIC_CONTROL_DEVICE, DEVICE_CONDITION, WEATHER_CONDITION, LIGHTING_CONDITION, FIRST_CRASH_TYPE, TRAFFICWAY_TYPE, LANE_CNT, ALIGNMENT, ROADWAY_SURFACE_COND, ROAD_DEFECT, REPORT_TYPE, CRASH_TYPE

  - Description: This dataset contains detailed records of traffic crashes occurring within the City of Chicago under the jurisdiction of the Chicago Police Department (CPD). Each record represents a single crash event and includes information such as crash date and time, location, environmental conditions, and contributing factors. The data are sourced from CPD’s electronic crash reporting system (E-Crash) and are updated as reports are finalized or amended.
The dataset includes both police-reported crashes and self-reported incidents, though some variables (e.g., weather, road conditions) are based on the reporting officer’s best available information at the time and may contain inconsistencies. Citywide coverage is available starting from September 2017. Crashes outside CPD jurisdiction (e.g., on interstate highways) are excluded.

 ### Dataset Integration                              
                                                                                                 
The two datasets will be integrated using the shared identifier CRASH_RECORD_ID. The Traffic Crashes – People dataset contains one row per individual involved in a crash, while the Traffic Crashes – Crashes dataset contains one row per crash event.

A left join will be performed with the People dataset as the base. This will ensure that all person-level records are preserved while attaching relevant crash-level information to each individual. This approach reflects the one-to-many relationship between crashes and people, where multiple individuals can be associated with a single crash.

This integration will allow injury outcomes at the individual level to be analyzed alongside crash conditions such as weather, crash type, and roadway characteristics, without aggregating away person-level detail.

---

 ## Timeline:

  ### Phase 1 — Project Planning (Before Apr 12) —  *Completed*                                            
                                                         
  - **Finalize research questions** (Apr 10) — 
         
    Define the primary research question focused on how a person’s role in a crash relates to injury severity in Chicago traffic crashes.
                                                         
  - **Identify and evaluate datasets** (Apr 10) — 
    
    Select 2 datasets from the Chicago Data Portal, confirm they are from trustworthy sources, and verify that they can be meaningfully integrated. *(Module 4: Data collection and acquisition)*
                                                         
  - **Review licenses and terms of use** (Apr 10) — 
    
    Identify any ethical, legal, or privacy constraints associated with each dataset and document how they will be addressed. *(Module 3: Ethical data handling)*

  - **Explore dataset structures** (Apr 11) — 
          
    Inspect column names, data types, and shared identifiers across both datasets to confirm integration is feasible. *(Module 7-8: Data integration)*
                                                         
  - **Set up GitHub repository and project structure** (Apr 11) — 
                                           
    Create the GitHub repository, define folder structure and file naming conventions, and organize project files. *(Module 2: Files, storage and organization)*

  - **Prepare and submit ProjectPlan.md** (Apr 12) — 
    
    Write and commit the project plan in Markdown, create a project-plan release, and submit the URL to Canvas.                                 

                                         
   
  ### Phase 2 — Data Cleaning and Initial Integration    
  (Apr 13 – Apr 19)                                    

  - **Download datasets and verify integrity** (Apr 13)
                                  
    Download both datasets from the Chicago Data Portal and verify file structure and completeness before analysis.                          
                                                         
  - **Profile each dataset** (Apr 14)
                                                  
    Assess the shape, data types, missing value rates, and value distributions for each dataset. Document data quality issues such as nulls, inconsistencies, and unexpected values. *(Module 10: Data quality)*         
                                                         
  - **Clean Traffic Crashes – Crashes dataset** (Apr 15)
                                                 
    handle missing or uninformative weather values used in the analysis. *(Module 11-12: Data cleaning)**(Module 11-12: Data cleaning)*
                                                         
  - **Clean Traffic Crashes – People dataset** (Apr 15)
                                                  
    Inspect and clean injury classification values, including handling UNKNOWN or missing entries *(Module 11-12: Data cleaning)*
                                                                                                                                                                                      
  - **Integrate Crashes and People datasets** (Apr 17) 
                                         
    Join the Traffic Crashes – People dataset with the Traffic Crashes – Crashes dataset using CRASH_RECORD_ID as the shared key, and validate the merge for completeness and correctness while preserving person-level records.  *(Module 7-8: Data integration)*
                                                         
  - **Conduct initial exploratory data analysis** (Apr 18)
                                              
    Examine distributions of injury severity, person types, and crash characteristics to identify patterns and inform later analysis.
                                                         
  - **Prepare and submit StatusReport.md** (Apr 19)                                                
    Write and commit the interim status report in  Markdown, create a status-report release, and submit the URL to Canvas.                      
                                          
   
  ### Phase 3 — Analysis and Final Development (Apr 20 – May 3)                                                                 
                                                    
  - **Perform detailed analysis** (Apr 25)
    
    Analyze how a person’s role in a crash (driver, passenger, pedestrian, bicyclist) relates to injury severity using the INJURY_CLASSIFICATION variable. Compute proportional distributions of injury outcomes within each group to enable meaningful comparison despite differences in group size.
                                                         
  - **Create visualizations** (Apr 26) 
      
    Generate bar charts showing proportional injury severity distributions across person types, clearly illustrating differences in injury outcomes between drivers, passengers, pedestrians, and bicyclists.     
                          
  - **Write data dictionary and codebook** (Apr 27)
                                      
    Document key variables from both the Traffic Crashes – People and Traffic Crashes – Crashes datasets, including variable name, data type, description, and known data quality issues, with emphasis on PERSON_TYPE, INJURY_CLASSIFICATION, and CRASH_RECORD_ID. (Module 15: Metadata and data documentation)
                                  
  - **Document data integration and cleaning workflow** (Apr 28)    

    Describe the process used to integrate the two datasets using CRASH_RECORD_ID, including the use of a left join to preserve person-level observations, along with detailed documentation of data cleaning steps such as dropping high-missing variables and filtering uninformative values. (Module 5: Data integration; Module 6: Data quality and cleaning)



  - **Write requirements.txt and verify reproducibility** (Apr 30)
                                
    Record all required Python dependencies and confirm that the notebook executes successfully from start to finish in a clean environment using the documented reproduction steps. (Module 14: Reproducibility and provenance)               
                                                         
  - **Write final README.md report** (May 2)
    
    Complete all required report sections including summary, data profile, data quality, data cleaning, findings, challenges, and reproduction steps.

  - **Create final-project release and submit to Canvas** (May 3) — 
  
    Commit all artifacts, create the final-project tag  and release on GitHub, and submit the release URL to Canvas by the deadline.

---

## Constraints:

### Structural Differences Between Datasets
A key constraint in this project is the difference in structure between the two datasets. The Traffic Crashes – Crashes dataset records information at the crash level, while the Traffic Crashes – People dataset records information at the individual level. Because multiple individuals can be associated with a single crash, the merged dataset contains multiple rows per crash. This is appropriate for the analysis, but it requires careful interpretation to ensure that conclusions are drawn at the correct level (person-level rather than crash-level) and that repeated crash entries are not misinterpreted as independent events.

### Data Quality and Missing Information
Both datasets contain variables with missing, inconsistent, or ambiguous values. Fields such as INJURY_CLASSIFICATION, SAFETY_EQUIPMENT, and contributing factors often include entries like “UNKNOWN” or “NOT APPLICABLE.” These values limit the ability to perform more detailed analysis and require filtering or simplification during data cleaning. In addition, some variables have extremely high levels of missingness and must be removed entirely, which reduces the overall amount of usable information.

### Limitations of Reported Data
The datasets only include crashes that were officially reported and recorded. This introduces a constraint because not all traffic incidents are captured, especially minor or unreported events. As a result, the dataset may not fully represent overall traffic risk, and the findings should be interpreted as patterns within reported crashes rather than all real-world incidents.

### Limited Variables for Explaining Outcomes
While the datasets provide useful descriptive information, they do not include all factors that influence injury severity. Important variables such as traffic volume, driver behavior, road design specifics, and real-time environmental conditions are not fully captured. Because of this, the analysis is limited to identifying patterns and associations rather than explaining the underlying causes of injury severity differences.

### Sampling and Computational Constraints
To ensure the analysis remains computationally manageable within the notebook environment, a subset of the full dataset is used. While the sample size is still large enough to observe meaningful patterns, it may not fully capture all rare events or edge cases. This introduces a tradeoff between efficiency and completeness in the analysis.
---

## Gaps:

### Limited Context on Underlying Causes:
While the datasets allow for comparison of injury severity across different person types, they do not provide enough detail to fully explain why these differences occur. Variables such as driver behavior, reaction time, traffic density, and real-time decision-making are not captured in the data. As a result, the analysis can identify patterns in injury outcomes but cannot fully explain the mechanisms behind those patterns.

### Lack of Exposure-Based Measures
The datasets do not include information on how frequently each type of road user is exposed to traffic conditions. For example, while pedestrians may show a higher proportion of severe injuries, the data does not indicate how often pedestrians are present relative to drivers. Without exposure data (such as traffic volume or pedestrian counts), it is difficult to determine whether differences in injury severity reflect higher risk per incident or simply differences in exposure frequency.

### Limited Temporal and Spatial Analysis
Although the datasets include time and location information, the current analysis does not fully explore how injury severity varies across different areas or time periods. Incorporating spatial or temporal breakdowns could provide deeper insight into where and when higher-risk outcomes occur, but this is beyond the scope of the current project.

### Constraints from Sampling
To keep the analysis computationally manageable, a subset of the full dataset is used. While the sample size is still large, it may not capture all rare events or edge cases, such as certain types of severe injuries or less common crash scenarios. This introduces a limitation in how fully the results represent the entire dataset.