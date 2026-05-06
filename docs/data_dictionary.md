# Data Dictionary

Note: Variable descriptions are summarized based on dataset documentation and observed usage in the dataset. For full official definitions, refer to the Chicago Data Portal dataset documentation.

This file documents the key variables used in the IS 477 final project and clarifies their role in the analysis workflow.

---

## Traffic Crashes – Crashes Dataset

| Variable | Description | Role in Project |
|---|---|---|
| CRASH_RECORD_ID | Unique identifier for each crash record. Used to link crash-level data with person-level data. | Used in Analysis |
| CRASH_DATE | Date and time when the crash occurred. | Exploratory Only |
| POSTED_SPEED_LIMIT | Posted speed limit at the crash location. | Exploratory Only |
| TRAFFIC_CONTROL_DEVICE | Type of traffic control device present at the crash location. | Exploratory Only |
| DEVICE_CONDITION | Condition of the traffic control device. | Exploratory Only |
| WEATHER_CONDITION | Weather condition at the time of the crash. Records marked UNKNOWN were removed during cleaning. | Used for Cleaning |
| LIGHTING_CONDITION | Lighting condition at the time of the crash. | Exploratory Only |
| FIRST_CRASH_TYPE | First recorded crash type (e.g., rear-end, turning, angle, pedestrian, bicyclist). | Exploratory Only |
| TRAFFICWAY_TYPE | Type of trafficway where the crash occurred. | Exploratory Only |
| ROADWAY_SURFACE_COND | Roadway surface condition at the time of the crash. | Exploratory Only |
| INJURIES_FATAL | Number of fatal injuries associated with the crash. | Exploratory Only |
| INJURIES_INCAPACITATING | Number of incapacitating injuries associated with the crash. | Exploratory Only |
| INJURIES_NON_INCAPACITATING | Number of non-incapacitating injuries associated with the crash. | Exploratory Only |
| CRASH_HOUR | Hour when the crash occurred. | Exploratory Only |
| CRASH_DAY_OF_WEEK | Day of week when the crash occurred. | Exploratory Only |
| CRASH_MONTH | Month when the crash occurred. | Exploratory Only |
| LATITUDE | Latitude of the crash location. | Exploratory Only |
| LONGITUDE | Longitude of the crash location. | Exploratory Only |
| LOCATION | Geographic coordinate of the crash location. | Exploratory Only |

---

## Traffic Crashes – People Dataset

| Variable | Description | Role in Project |
|---|---|---|
| PERSON_ID | Unique identifier for each individual involved in a crash. | Exploratory Only |
| PERSON_TYPE | Role of the individual (driver, passenger, pedestrian, bicyclist). | Used in Analysis |
| CRASH_RECORD_ID | Identifier linking the person to the corresponding crash record. | Used in Analysis |
| VEHICLE_ID | Identifier for the associated vehicle, when applicable. | Exploratory Only |
| CRASH_DATE | Date and time of the crash. | Exploratory Only |
| SEAT_NO | Seat number of the individual, when applicable. | Exploratory Only |
| CITY | City associated with the record. | Exploratory Only |
| STATE | State associated with the record. | Exploratory Only |
| ZIPCODE | ZIP code associated with the record. | Exploratory Only |
| SEX | Reported sex of the individual. | Exploratory Only |
| AGE | Reported age of the individual. | Exploratory Only |
| SAFETY_EQUIPMENT | Safety equipment usage, when applicable. | Exploratory Only |
| AIRBAG_DEPLOYED | Whether an airbag was deployed. | Exploratory Only |
| EJECTION | Whether the individual was ejected from the vehicle. | Exploratory Only |
| INJURY_CLASSIFICATION | Injury severity classification for the individual. This is the primary outcome variable used in the analysis. | Used in Analysis |
| DRIVER_ACTION | Reported driver action, when applicable. | Exploratory Only |
| DRIVER_VISION | Reported driver vision condition. | Exploratory Only |
| PHYSICAL_CONDITION | Reported physical condition of the individual. | Exploratory Only |
| BAC_RESULT | Blood alcohol test result category. | Exploratory Only |
| BAC_RESULT VALUE | Blood alcohol content value. | Exploratory Only |

---

## Dropped Variables

The following variables were removed from the dataset due to high missingness, redundancy, or lack of relevance to the research question:

- CELL_PHONE_USE
- LANE_CNT
- WORKERS_PRESENT_I
- WORK_ZONE_TYPE
- DOORING_I
- WORK_ZONE_I