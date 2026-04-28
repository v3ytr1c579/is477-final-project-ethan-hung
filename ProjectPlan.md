# Final Project Plan
#### Team Outliers: Chenxi Zhang, Ethan Hung, Mustafa El Zayyat

---

## Overview: 

This project investigates whether a relationship exists between automated speed camera enforcement, traffic crash occurrences, and crash-related injuries in Chicago. Using three publicly available datasets from the Chicago Data Portal, Speed Camera Violations, Traffic Crashes – Crashes, and Traffic Crashes – People, we aim to identify spatial and temporal patterns that connect enforcement activity to crash frequency and injury outcomes across the city.

Our approach involves three main steps. First, we will clean and integrate the three datasets by linking crash records and person-level injury data through a shared date field, and spatially matching speed camera locations to nearby crash events. Second, we will conduct exploratory data analysis to describe the distribution of violations, crashes, and injuries across time, location, and road user type, identifying high-risk zones and periods where enforcement activity and crash severity overlap.

By combining enforcement data with crash-level and person-level records, this project aims to provide evidence on how Chicago's automated speed enforcement program relates to traffic safety outcomes. The findings will contribute to a broader understanding of what factors most strongly predict crash occurrences and injuries, and may offer insights. 

---

## Team: 

  Our project team consists of three members, each responsible for managing one dataset and contributing to integration and analysis.

  Chenxi Zhang: Will work with the traffic crashes – crashes dataset and focus on cleaning and organizing crash-level event data, handling variables such as crash date, time, location, weather conditions, and contributing factors. I will be responsible for standardizing key fields and preparing the dataset for integration with other datasets using shared identifiers. I will assist in aggregating crash level information and aligning it with person level injury data and speed camera violations data through temporal and spatial matching. I will also collaborate with team members on analysis and data integration to ensure that the datasets are correctly linked and consistent across different levels of detail.

  Mustafa El Zayyat: Will work with speed camera violations dataset and focus on cleaning and organizing the time series data, handling variables such as camera ID, location, and daily violation counts. I would also be responsible for preparing spatial information (camera locations) if necessary and summarizing enforcement intensity over time and across locations. Will also collaborate with team members on analysis and data integration to ensure that the datasets are correctly linked using shared identifiers. 

  Ethan Hung: Will work with the traffic crashes people dataset and focus on cleaning and       organizing person-level crash data, handling variables such as person ID, person type (driver/passenger), crash record ID, vehicle ID, crash date, and demographic information. Also, I will standardize fields related to occupant safety and injury outcomes, including safety equipment usage, airbag deployment, ejection status, and injury classification. Moreover, I will collaborate with team members on analysis and data integration to ensure person-level records are correctly linked with other datasets using shared identifiers.

---

## Research or Business Question: 

Is there a relationship between speed camera violations, traffic crashes, and crash injuries in Chicago? What factors are most strongly associated with traffic crash occurrences in Chicago?

We will combine the Traffic Crashes – Crashes dataset and the Traffic Crashes – People dataset to analyze how crash-level conditions such as weather, road surface, lighting, and posted speed limit relate to person-level injury outcomes including injury classification, airbag deployment, and ejection status. Person-level records will be aggregated to the crash level using the shared CRASH_RECORD_ID, and injury severity distributions will be compared across crash conditions.

Together, all three datasets will be integrated using date as the shared temporal key, connecting daily activity (Speed Camera Violations) to daily crash counts (Traffic Crashes – Crashes) to individual injury records (Traffic Crashes – People), allowing us to examine whether days and periods with higher enforcement activity correspond to differences in crash frequency and injury outcomes.

The expected outputs include correlation statistics between daily violation counts and crash frequency, summary tables of injury rates by crash condition, and time series visualizations showing enforcement activity alongside crash and injury trends across Chicago.

---

## Datasets:
  
### Dataset 1: Speed Camera Violations 
   
   - Source: City of Chicago Data Portal
    
   - Link: https://data.cityofchicago.org/Transportation/Speed-Camera-Violations/hhkd-xvj4/about_data
   
   - Variable Examples: ADDRESS, CAMERA_ID, VIOLATION_DATE, VIOLATIONS, X_COORDINATE, Y_COORDINATE, LATITUDE, LONGITUDE, LOCATION                                     
   
   - Description: This dataset reflects the daily volume of violations that have occurred in Children's Safety Zones for each camera. The data reflects violations that occurred from July 1, 2014 until present, minus the most recent 14 days. This data may change due to occasional time lags between the capturing of a potential violation and the processing and determination of a violation. The reported violations are those that have been collected by the camera and radar system and reviewed by two separate City contractors. Each row within the set represents the number of violations recorded by a specific camera on a given day which makes the dataset a time series panel of enforcement activity. Some of the variables included within the dataset are identifying information such as the address, unique camera ID, a timestamp indicating when the violation occurred, and the total number of violations observed.
   
 ### Dataset 2: Traffic Crashes – People
    
  - Source: City of Chicago Data Portal
  
  - Link: https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d/about_data 
  
  - Variable Examples: PERSON_ID, PERSON_TYPE, CRASH_RECORD_ID, VEHICLE_ID, CRASH_DATE, SEAT_NO, CITY, STATE, ZIPCODE, SEX, AGE, DRIVERS_LICENSE_STATE, DRIVERS_LICENSE_CLASS, SAFETY_EQUIPMENT, AIRBAG_DEPLOYED, EJECTION, INJURY_CLASSIFICATION, HOSPITAL, EMS_AGENCY, EMS_RUN_NO, DRIVER_ACTION, DRIVER_VISION, PHYSICAL_CONDITION, PEDPEDAL_ACTION, PEDPEDAL_VISIBILITY, PEDPEDAL_LOCATION, BAC_RESULT, BAC_RESULT_VALUE, CELL_PHONE_USE

  - Description: The Traffic Crashes – People dataset contains information about individuals involved in traffic crashes in Chicago and whether they were injured. Each row represents one person involved in a crash, including drivers, passengers, pedestrians, or cyclists. The dataset includes characteristics such as age, gender, safety equipment use, airbag deployment, and injury classification. Records can be linked to crash events and vehicles using the shared CRASH_RECORD_ID, allowing analysis of how crash conditions and vehicle involvement relate to injuries.

 ### Dataset 3: Traffic Crashes - Crashes
  
  - Source: City of Chicago Data Portal
    
  - Link: https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data
    
  - Variable Examples: CRASH_RECORD_ID, CRASH_DATE_EST_I, CRASH_DATE, POSTED_SPEED_LIMIT, TRAFFIC_CONTROL_DEVICE, DEVICE_CONDITION, WEATHER_CONDITION, LIGHTING_CONDITION, FIRST_CRASH_TYPE, TRAFFICWAY_TYPE, LANE_CNT, ALIGNMENT, ROADWAY_SURFACE_COND, ROAD_DEFECT, REPORT_TYPE, CRASH_TYPE

  - Description: This dataset contains detailed records of traffic crashes occurring within the City of Chicago under the jurisdiction of the Chicago Police Department (CPD). Each record represents a single crash event and includes information such as crash date and time, location, environmental conditions, and contributing factors. The data are sourced from CPD’s electronic crash reporting system (E-Crash) and are updated as reports are finalized or amended.
The dataset includes both police-reported crashes and self-reported incidents, though some variables (e.g., weather, road conditions) are based on the reporting officer’s best available information at the time and may contain inconsistencies. Citywide coverage is available starting from September 2017. Crashes outside CPD jurisdiction (e.g., on interstate highways) are excluded.

 ### Dataset Integration                              
                                                         
The three datasets will be integrated in two steps. First, the Traffic Crashes – Crashes dataset and the Traffic Crashes – People dataset will be joined using the shared CRASH_RECORD_ID identifier, which uniquely identifies each crash event across both datasets. This allows person-level injury records to be linked directly to their corresponding crash events.        

 Second, the integrated crash dataset will be connected to the Speed Camera Violations dataset using date as a shared temporal key. Since crash and violation records do not share a geographic identifier, both datasets will be aggregated to the daily level using CRASH_DATE and VIOLATION_DATE respectively, and merged by date to enable temporal analysis of enforcement activity alongside crash frequency and injury outcomes.


---

 ## Timeline:

  ### Phase 1 — Project Planning (Before Apr 12) —  *Completed*                                            
                                                         
  - **Finalize research questions** (Apr 10) — *All*
         
    Define the primary and secondary research questions about the relationship between speed camera enforcement, crash frequency, and injury outcomes in Chicago.
                                                         
  - **Identify and evaluate datasets** (Apr 10) — *All*
    
    Select three datasets from the Chicago Data Portal, confirm they are from trustworthy sources, and verify that they can be meaningfully integrated. *(Module 4: Data collection and acquisition)*
                                                         
  - **Review licenses and terms of use** (Apr 10) — *All*
    
    Identify any ethical, legal, or privacy constraints associated with each dataset and document how they will be addressed. *(Module 3: Ethical data handling)*

  - **Explore dataset structures** (Apr 11) — *All*
          
    Inspect column names, data types, and shared identifiers across all three datasets to confirm integration is feasible. *(Module 7-8: Data integration)*
                                                         
  - **Set up GitHub repository and project structure** (Apr 11) — *All*
                                           
    Create the shared GitHub repository, define folder structure and file naming conventions, and add all team members. *(Module 2: Files, storage and organization)*

  - **Prepare and submit ProjectPlan.md** (Apr 12) — *All*
    
    Write and commit the project plan in Markdown, create a project-plan release, and submit the URL to Canvas.                                 

                                         
   
  ### Phase 2 — Data Cleaning and Initial Integration    
  (Apr 13 – Apr 19)                                    

  - **Download datasets and verify integrity** (Apr 13) — *Mustafa*
                                  
    Programmatically download all three datasets using the Chicago Data Portal API and compute SHA-256 checksums to verify file integrity. *(Module 4: Data collection and acquisition)*                           
                                                         
  - **Profile each dataset** (Apr 14) — *Chenxi / Ethan / Mustafa*
                                                  
    Assess the shape, data types, missing value rates, and value distributions for each dataset. Document data quality issues such as nulls, inconsistencies, and unexpected values. *(Module 10: Data quality)*         
                                                         
  - **Clean Traffic Crashes – Crashes dataset** (Apr 15) — *Chenxi*
                                                 
    Standardize date and time formats, handle missing values in weather and road condition fields, and remove or flag records with unknown contributing factors. *(Module 11-12: Data cleaning)*
                                                         
  - **Clean Traffic Crashes – People dataset** (Apr 15) — *Ethan*
                                                  
    Standardize injury classification categories, filter out records with missing person type or crash record IDs, and handle entries coded as UNKNOWN or NOT APPLICABLE. *(Module 11-12: Data cleaning)*
                                                         
  - **Clean Speed Camera Violations dataset** (Apr 15) — *Mustafa*
                                                 
    Parse and standardize violation dates, handle missing or malformed location fields, and verify camera IDs are consistent across records. *(Module 11-12: Data cleaning)*                                             
                                                         
  - **Aggregate person-level data to crash level** (Apr 16) — *Ethan*
                                               
    Group the Traffic Crashes – People dataset by CRASH_RECORD_ID to produce crash-level summaries of injury counts, injury severity, and safety equipment usage. *(Module 7-8: Data integration)*                
                                                         
  - **Integrate Crashes and People datasets** (Apr 17) — *Chenxi / Ethan*
                                         
    Join the aggregated people data to the crashes dataset using CRASH_RECORD_ID as the shared key, and validate the merge for completeness and correctness.  *(Module 7-8: Data integration)*
                                                         
  - **Conduct initial exploratory data analysis** (Apr 18) — *All*
                                              
    Examine distributions of crash counts, violation    frequencies, and injury rates over time and across locations to identify patterns and inform later analysis.
                                                         
  - **Prepare and submit StatusReport.md** (Apr 19) — *All*                                                  
    Write and commit the interim status report in  Markdown, create a status-report release, and submit the URL to Canvas.                      

                                                 
   
  ### Phase 3 — Analysis and Final Development (Apr 20 – May 3)                                                                 
                                                         
  - **Perform detailed analysis** (Apr 25) — *All*
    
    Analyze the relationship between daily violation counts and crash frequency and injury severity, controlling for time and location. 
                                                         
  - **Create visualizations** (Apr 26) — *All*
      
    Generate time series plots, spatial maps of high-risk zones, and injury breakdown charts to illustrate key findings.                               

  - **Write data dictionary and codebook** (Apr 27) — *All*
                                      
    Document each variable in all three datasets including name, type, description, and known quality issues. *(Module 15: Metadata and data documentation)*
                                                         
  - **Write machine-readable metadata** (Apr 28) — *All*
    
    Create a metadata file conforming to a standard schema (DCAT or Schema.org) to support discoverability and reuse of the project datasets. *(Module 15: Metadata and data documentation)*
                                                         
  - **Develop Snakemake workflow** (Apr 29) — *All*
    
    Build an automated end-to-end Snakemake workflow covering data acquisition, cleaning, integration, and analysis so the full pipeline can be re-executed from scratch. *(Module 13: Workflow automation and provenance)*                                           
   
  - **Write requirements.txt and verify reproducibility** (Apr 30) — *All*
                                
    Record all software dependencies and verify that the full workflow runs successfully in a clean environment from data acquisition through final results. *(Module 14: Reproducibility and provenance)*                   
                                                         
  - **Write final README.md report** (May 2) — *All*
    
    Complete all required report sections including summary, data profile, data quality, data cleaning, findings, challenges, and reproduction steps.

  - **Create final-project release and submit to Canvas** (May 3) — *All*
    
    Commit all artifacts, create the final-project tag  and release on GitHub, and submit the release URL to Canvas by the deadline.

---

## Constraints:

### Different Levels of Detail Across Datasets
One challenge in this project is that the three datasets are structured at different levels. The Traffic Crashes – Crashes dataset records information about each crash event, the Traffic Crashes – People dataset records information about every individual involved in a crash, and the Speed Camera Violations dataset records the number of violations per camera on each day. Because multiple people can be involved in a single crash, the people dataset must therefore  be aggregated to the crash level using CRASH_RECORD_ID before it can be compared with crash events and enforcement data. Also, linking crashes to speed camera activity will also require matching records based on date and approximate location, since crashes are not recorded directly at camera locations.
 
### Differences in Time and Location Information
Another limitation is that the datasets record time and location in different ways; speed camera data reports the total number of violations per camera per day, while crash data includes more detailed timestamps and addresses. Thus, to make the datasets comparable, crash records may need to be grouped at the daily level, which reduces some of the detail in the crash timing. In addition, crashes and cameras do not share a common geographic identifier, so crashes will need to be matched to nearby cameras using location information; this means the relationship between enforcement zones and crashes can only be estimated.

### Data Quality and Missing Information
Some variables in the crash and people datasets contain missing or unclear values. Fields such as injury classification, safety equipment use, driver vision, and contributing factors often contain entries like “UNKNOWN” or “NOT APPLICABLE.” As a result, these values can limit certain analyses or require us to filter or group categories during data cleaning. Also, in some cases, the information in crash reports is based on the reporting officer’s assessment at the time, which may lead to inconsistencies across records.
 
### Limits of the Data for Explaining Causes
Finally, the datasets do not directly measure overall traffic exposure or driving behavior; the speed camera dataset records violations detected by cameras, but this does not necessarily reflect all speeding activity in an area. Similarly,  crash records show where crashes occurred but do not include factors like traffic volume. Because of this, the project can identify patterns and relationships between enforcement activity, crashes, and injuries, but it cannot entirely determine whether speed cameras cause changes in crash outcomes.

---

## Gaps:

### Lack of Contextual Information: 
The datasets do not include information on when speed cameras were installed or any policy changes related to enforcement and without this context, it could be difficult to evaluate whether changes in violations or crashes are linked to program implementation or external factors. While crash data includes contributing factors, it lacks deeper behavioral context such as driver intent or distraction levels beyond reported categories and real time traffic dynamics. This can limit the ability to fully assess the reason that crashes occur in certain areas with enforcement.

### Lack of baseline data for comparison purposes: 
The data is limited to Chicago, with no built in comparison to areas without speed cameras or other cities and jurisdictions. Without a benchmark, it could be difficult to assess whether observed patterns are unique to Chicago or part of broader trends.

### Visibility into overall safety is limited by assessment of actual crashes: 
While crashes are recorded and included in analysis, there is limited visibility into unreported incidents.This can potentially create a gap in understanding the full safety landscape, as only the recorded crashes would be analyzed.

