# How a Person's Role in a Crash Affects Injury Severity in Chicago Traffic Accidents

## Contributors
- Ethan Hung

## Summary 
This project looks at how a person’s role in a traffic crash affects the severity of injuries they experience, using traffic crash data from the City of Chicago. The idea behind this analysis is that different types of people in a crash—like drivers, passengers, pedestrians, and bicyclists—are exposed to very different levels of risk. For example, people inside a vehicle are generally more protected, while pedestrians and bicyclists are more exposed. Because of this, I wanted to see if the data actually shows meaningful differences in injury outcomes across these groups.

To explore this, I used two datasets from the Chicago Data Portal: “Traffic Crashes – Crashes” and “Traffic Crashes – People.” The Crashes dataset includes information about each crash itself (like weather, crash type, and location), while the People dataset contains information about individuals involved in each crash (like their role and injury severity). This project follows the DIKW lifecycle model, progressing from raw crash records through data integration and cleaning, toward analytical findings about injury risk across road user types. Since the research question focuses on injury outcomes at the individual level, the People dataset was the main dataset used, and the Crashes dataset was primarily merged to preserve the structure of the data and provide contextual variables, though it was not directly used in the final comparison.

The workflow followed a step-by-step process: loading the data, inspecting it, merging the datasets, cleaning the data, and then doing exploratory analysis. To keep things manageable in the notebook, I used a subset of 100,000 rows from each dataset. After loading both datasets, I merged them using a left join on CRASH_RECORD_ID. This kept all person-level records while adding crash-level information, resulting in a dataset with 100,000 rows and 76 columns before cleaning.

During the data quality step, I noticed that several variables had a lot of missing values, especially things like work zone indicators, lane count, and cell phone usage. Since these variables weren’t important for answering my research question and were mostly incomplete, I removed them. I also removed rows where WEATHER_CONDITION was listed as UNKNOWN, since those values didn’t add useful information. After cleaning, the final dataset had 91,833 rows and 70 columns.

For the analysis, I focused on four main person types: drivers, passengers, pedestrians, and bicyclists. I used the INJURY_CLASSIFICATION variable to measure injury severity, and instead of just looking at raw counts, I calculated proportions so the groups could be compared fairly.

The results showed clear differences across groups. Drivers and passengers mostly had no injury, suggesting lower overall risk inside vehicles. On the other hand, pedestrians and bicyclists had much higher proportions of injuries. Pedestrians especially stood out, as they had the highest injury severity overall and were the only group with a noticeable share of fatal injuries.

Overall, the results support the idea that people who are more exposed—like pedestrians and bicyclists—face higher risks in traffic crashes. This reinforces how important it is to consider different types of road users when thinking about traffic safety and prevention.

## Data Profile

This project uses two datasets from the Chicago Data Portal: “Traffic Crashes – Crashes” and “Traffic Crashes – People.” These datasets are publicly available and contain detailed records of traffic incidents reported in the city of Chicago. Both datasets are structured as tabular CSV files and are widely used for traffic safety analysis.

The Traffic Crashes – Crashes dataset is organized at the crash level, meaning each row represents a single crash event. This dataset includes variables that describe the conditions under which the crash occurred, such as crash date and time, weather condition, lighting condition, crash type, and geographic location. For example, variables like WEATHER_CONDITION, FIRST_CRASH_TYPE, and ROADWAY_SURFACE_COND provide insight into environmental and situational factors that may influence crash outcomes. While this dataset does not directly contain person-level injury information, it provides important context that helps explain the circumstances surrounding each crash.

The Traffic Crashes – People dataset is organized at the individual level, where each row represents a person involved in a crash. This dataset includes variables such as PERSON_TYPE, INJURY_CLASSIFICATION, age, sex, and other attributes related to the individual and their role in the crash. Since the main research question focuses on injury severity, this dataset serves as the primary source for analysis. In particular, PERSON_TYPE and INJURY_CLASSIFICATION are the most important variables, as they allow for comparison of injury outcomes across different types of road users.

To combine these datasets, a left join was performed using the shared identifier CRASH_RECORD_ID. This decision was intentional and reflects the structure of the data. Because the People dataset contains one row per individual, while the Crashes dataset contains one row per crash, there is a one-to-many relationship between crashes and people. Using a left join ensures that all person-level records are preserved, which is important because each person represents a separate observation in the analysis. The crash-level variables are then attached to each person record, allowing injury outcomes to be analyzed alongside crash conditions.

The datasets are quite large, so to keep the analysis manageable within the notebook environment, a subset of 100,000 rows from each dataset was used. This was not meant to bias the results, but rather to ensure that computations could be performed efficiently while still maintaining a large enough sample to observe meaningful patterns. After merging the datasets, the combined dataset contained 100,000 rows and 76 columns. Following data cleaning, this was reduced to 91,833 rows and 70 columns.

In terms of data characteristics, both datasets include a mix of categorical and numerical variables. A key observation during initial inspection was that many variables, especially in the People dataset, contained a high proportion of missing values. Variables related to work zones, lane counts, and cell phone usage were often incomplete and not directly relevant to the research question. Identifying these issues early helped guide the cleaning process and ensured that the final analysis focused only on meaningful variables.

Both datasets are published under the City of Chicago's standard open data license, which is based on the Open Data Commons Public Domain Dedication and License (PDDL), permitting free use, distribution, and analysis without restriction. From an ethical and legal perspective, both datasets are publicly available and do not contain personally identifiable information. The data is anonymized and intended for public use, making it appropriate for academic analysis. However, there are still some limitations to consider. The datasets only include reported crashes, meaning that unreported incidents are not captured. Additionally, injury classifications are based on reported assessments at the time of the crash and may not perfectly reflect the true severity of injuries in all cases. These limitations are important to acknowledge when interpreting the results.

Finally, these two datasets are well-suited to the research question because they provide complementary information. The People dataset allows for analysis of injury outcomes at the individual level, while the Crashes dataset adds context about the conditions under which those injuries occurred. By integrating the two, the project is able to move beyond simple counts and instead analyze how injury severity varies across different types of road users in a more complete and meaningful way.

## Data Quality

Before doing any cleaning, I spent time going through the data to understand what kinds of issues were present and how they might affect the analysis. I didn’t want to immediately start removing things without first seeing what was actually wrong, since that could lead to losing useful information or missing important patterns.

One of the biggest issues I found was the amount of missing data in certain columns. After checking the number of null values in each column, it became clear that some variables were almost entirely empty. For example, columns like CELL_PHONE_USE, LANE_CNT, WORKERS_PRESENT_I, WORK_ZONE_TYPE, and DOORING_I had missing values in nearly every row. At that point, those variables aren’t really usable because there isn’t enough information to analyze or draw any conclusions from them. Keeping them would just add noise to the dataset and make it harder to focus on variables that actually matter.

Another issue showed up when looking at categorical variables, especially WEATHER_CONDITION. Most of the values were straightforward, like “CLEAR,” “RAIN,” or “SNOW,” but there was also a noticeable number of entries labeled as UNKNOWN. That category doesn’t give any real information about the crash, so it makes comparisons less meaningful. I also noticed that some weather categories appeared very rarely. While those values are still technically valid, they highlight how uneven the data is across categories, which is something to keep in mind when interpreting results.

I also explored the FIRST_CRASH_TYPE variable to get a sense of what types of crashes were most common. Some types, like rear-end and turning crashes, appeared much more frequently than others. This doesn’t necessarily indicate a problem with the data, but it does show that the dataset is not evenly distributed across all categories. That kind of imbalance can influence how patterns show up in the analysis.

Another important thing to consider was the structure of the dataset after merging. The People dataset has one row per person, while the Crashes dataset has one row per crash. When these are merged, a single crash can appear multiple times, once for each person involved. This means the final dataset has multiple rows per crash. At first this might look like duplication, but it’s actually expected given how the data is organized. Since the goal of the project is to analyze injury outcomes at the individual level, this structure is appropriate and doesn’t need to be changed.

Another thing I considered was how these data quality issues might affect the interpretation of the results. For example, if variables with a high amount of missing data were kept, they could create misleading patterns or make certain categories appear less important than they actually are. Similarly, including ambiguous categories like UNKNOWN could weaken comparisons across groups because those observations do not clearly belong to any meaningful category. By identifying these issues early, it became easier to decide what needed to be removed in order to keep the analysis focused and interpretable. This step helped ensure that the results were based on reliable and relevant data rather than incomplete or unclear information.

Overall, the main issues I found were high levels of missing data, some unclear or unhelpful categorical values, and the structure of the merged dataset. These didn’t make the data unusable, but they did require careful decisions about what to keep and what to remove. This process made it easier to move into the cleaning step with a clear understanding of what needed to be addressed.


## Data Cleaning

After identifying the main issues during the data quality step, I moved on to cleaning the dataset in a way that would make the analysis more reliable while still keeping the process simple. The goal wasn’t to overcomplicate things, but rather to remove clearly problematic parts of the data and focus on what was actually relevant to the research question.

The first step I took was removing columns that had extremely high levels of missing data. Based on the earlier inspection, columns like CELL_PHONE_USE, LANE_CNT, WORKERS_PRESENT_I, WORK_ZONE_TYPE, DOORING_I, and WORK_ZONE_I were missing values in nearly every row. Since these variables were both incomplete and not directly related to injury severity, they weren’t useful for the analysis. Keeping them would have added unnecessary noise and made the dataset harder to work with, so I dropped them entirely. This decision also helped reduce the dimensionality of the dataset, making it easier to focus on a smaller set of meaningful variables. After this step, the number of columns was reduced from 76 to 70, while still keeping all of the variables that were relevant to the research question.

The next step was handling the WEATHER_CONDITION variable. As observed earlier, there were a number of rows where the value was listed as UNKNOWN. Since this category doesn’t provide any meaningful information about the crash conditions, I decided to remove those rows instead of trying to keep or reclassify them. Keeping those rows would have made comparisons less clear, since “UNKNOWN” doesn’t represent an actual condition. Removing them ensured that all remaining rows had interpretable values for weather, which makes the dataset more consistent overall. After applying this filter, the dataset size decreased from 100,000 rows to 91,833 rows.

Beyond the columns dropped in the first step, several other columns in the merged dataset still contained high proportions of missing values — including PEDPEDAL_LOCATION, PEDPEDAL_VISIBILITY, PEDPEDAL_ACTION, EMS_AGENCY, HOSPITAL, and SEAT_NO. Rather than dropping these columns, I made a deliberate decision to retain them. Since the analysis focuses exclusively on PERSON_TYPE and INJURY_CLASSIFICATION, these variables play no role in the final comparison. Removing them would not improve the results and would reduce the dataset's potential utility for future analysis. To confirm the analysis was not affected, I verified that PERSON_TYPE and INJURY_CLASSIFICATION were complete for all four groups of interest — drivers, passengers, pedestrians, and bicyclists — with no missing values in either column. This gave me confidence that the remaining nulls elsewhere in the dataset posed no threat to the validity of the findings.

I also made sure to avoid making unnecessary changes to key variables used in the analysis. In particular, I did not modify the INJURY_CLASSIFICATION variable, since it represents the main outcome of interest. Changing or imputing values in this column could have introduced bias or distorted the results, so it was important to leave it as originally recorded. Similarly, I avoided applying transformations to other variables unless there was a clear reason to do so, since unnecessary changes can sometimes create more problems than they solve.

Another thing I was careful about during cleaning was preserving the structure of the merged dataset. Since each row represents an individual, and multiple individuals can be associated with the same crash, it was important not to accidentally remove rows in a way that would distort the person-level analysis. The cleaning steps were limited to removing unreliable columns and filtering out uninformative values, while keeping the overall structure intact. This ensured that each person remained a valid observation in the dataset.

I also kept the cleaning process intentionally minimal in terms of complexity. Instead of trying to impute missing values or engineer new features, I focused on removing clearly unusable data. This approach made the results easier to interpret and avoided introducing additional assumptions into the analysis. Given the scope of the project, this level of cleaning was sufficient to produce a dataset that was both manageable and reliable.

Overall, the cleaning process focused on simplifying the dataset by removing clearly unusable or irrelevant information rather than applying complex transformations. Each step was directly tied to a specific issue identified earlier, which helped ensure that the final dataset was both cleaner and more appropriate for the analysis. After cleaning, the dataset contained 91,833 rows and 70 columns, which were then used for the final injury severity analysis.

## Findings

The goal of this analysis was to understand how a person’s role in a crash relates to the severity of injuries they experience. To answer this, I focused on four main groups in the data: drivers, passengers, pedestrians, and bicyclists, and used the INJURY_CLASSIFICATION variable as the measure of injury severity.

A key decision in the analysis was to compare proportions rather than raw counts. This matters because the dataset is heavily skewed toward drivers, meaning there are far more driver records than any other group. If I had used raw counts, the results would mostly reflect how common each group is in the dataset rather than how injury severity is distributed within each group. By normalizing the counts, I was able to compare groups on a relative basis, which makes the differences in injury outcomes more meaningful.

Looking at the results, there are clear and fairly large differences across groups. Drivers have the highest proportion of “no indication of injury” outcomes at about 92.7%, and passengers are similar at about 85.6%. This suggests that the majority of individuals inside vehicles are not seriously injured in crashes, at least within this dataset. The remaining categories for these groups are relatively small, with non-incapacitating injuries making up around 3.6% for drivers and 7.0% for passengers, and fatal injuries being extremely rare for both groups.

In contrast, pedestrians show a completely different distribution. Only about 11.6% of pedestrian cases fall into the “no indication of injury” category, which is significantly lower than for drivers and passengers. Instead, a much larger share is concentrated in more severe categories. Non-incapacitating injuries make up about 55.3% of pedestrian cases, incapacitating injuries about 11.2%, and fatal injuries around 1.3%. While fatal injuries are still a small proportion overall, pedestrians have the highest fatal share among all groups, which is an important distinction.

Bicyclists fall somewhere between pedestrians and vehicle occupants. About 28.6% of bicyclists have no indication of injury, which is much lower than drivers and passengers but higher than pedestrians. At the same time, bicyclists have a relatively high share of non-incapacitating injuries at about 41.9%, along with smaller but noticeable proportions of incapacitating injuries (about 9.0%) and fatal injuries (about 0.4%). This suggests that bicyclists are also more exposed to injury risk, though not to the same extent as pedestrians.

One important takeaway is that these differences are not just driven by extreme cases like fatalities. The shift in distributions is visible across all injury categories. Pedestrians and bicyclists consistently show higher proportions in both non-incapacitating and incapacitating injury categories, while drivers and passengers are heavily concentrated in the “no injury” category. This indicates that the relationship between person type and injury severity is broad and consistent, rather than being driven by a small number of severe outcomes.

At the same time, it is important to be careful about interpretation. These results show a strong association between a person’s role in a crash and injury severity, but they do not establish causation. Other variables in the dataset, such as crash type, weather conditions, or roadway characteristics, may also influence these outcomes. Because those factors were not directly controlled for in this comparison, the results should be viewed as descriptive rather than explanatory.

I also briefly explored injury severity across different crash types using the FIRST_CRASH_TYPE variable. While this provided additional context about how crashes are distributed, it was not directly incorporated into the final comparison, so the main focus remained on differences across person types.

Overall, the findings show a clear and consistent pattern: individuals inside vehicles are much more likely to experience no injury, while pedestrians and bicyclists are far more likely to experience some form of injury, including more severe outcomes. The magnitude of these differences is not small, especially for pedestrians, where the distribution shifts heavily away from “no injury” and toward more severe categories.

This suggests that injury risk in traffic crashes is not just a matter of chance, but is strongly influenced by a person’s level of physical protection. Rather than all individuals facing similar levels of risk, the results indicate a clear imbalance where more exposed road users consistently experience worse outcomes. This highlights that injury severity is not evenly distributed across all participants in a crash, and that understanding these differences is important when thinking about traffic safety and risk exposure.

## Future Work

There are several ways this project could be expanded or improved in the future, especially by going beyond the basic comparisons used in this analysis. While the current approach focuses on identifying general patterns in injury severity across different person types, it mainly answers a descriptive question rather than a deeper explanatory one. As a result, one clear direction for future work would be to move from simply observing patterns to understanding why those patterns exist.

One natural extension would be incorporating additional variables from the existing datasets that were not used in the final analysis. For example, variables such as lighting conditions, roadway surface conditions, and traffic control devices were explored during the data inspection stage but ultimately left out to keep the scope manageable. Including these variables in a more detailed analysis could help explain how environmental and situational factors influence injury severity. Instead of just comparing person types, this would allow for a more layered analysis that considers both who is involved and under what conditions the crash occurs.

Another important improvement would be using more advanced analytical methods. In this project, I relied on normalized proportions to compare injury outcomes across groups, which works well for identifying overall trends. However, this method does not measure the strength or significance of relationships between variables. Future work could involve using regression models or classification methods to estimate how different factors contribute to injury severity. This would make the results more rigorous and allow for more precise conclusions, rather than relying only on visual comparisons.

The use of a 100,000-row sample is another area that could be improved. While sampling made the dataset easier to work with and reduced computational time, it also introduces the possibility that some patterns are underrepresented or missed entirely. Running the analysis on the full dataset would remove this concern and make the results more reliable. It would also allow for more detailed subgroup analysis, especially for less frequent categories like certain crash types or severe injuries.

Another direction for future work would be incorporating additional external data sources. The current analysis is limited to the information contained within the crash and people datasets. Adding external data, such as traffic volume, road design characteristics, or speed limit data, could provide more context and help explain why certain groups are more vulnerable. This would shift the analysis from describing what is happening to better understanding the underlying causes.

There is also potential to explore spatial and temporal trends in more detail. Since the dataset includes date and location variables, it would be possible to analyze how injury severity changes over time or varies across different parts of the city. For example, certain areas might have higher rates of pedestrian injuries, or certain times of day might be associated with more severe crashes. These types of patterns could provide more practical insights, especially from a policy or planning perspective.

Overall, while the current project answers the main research question at a basic level, there are many opportunities to make the analysis more detailed, more rigorous, and more explanatory by expanding both the variables used and the methods applied.

## Challenges

There were several challenges throughout this project, most of which were not necessarily technical, but related to understanding the data and making decisions about how to approach the analysis in a way that was both correct and manageable.

One of the first challenges was understanding how the two datasets relate to each other. The People dataset is structured at the individual level, while the Crashes dataset is structured at the event level. When these are merged, each crash can appear multiple times, once for each person involved. At first, this made the dataset look like it had duplicate rows, and it was not immediately clear whether this was a problem that needed to be fixed. After taking a step back and thinking about the structure more carefully, it became clear that this was expected and actually necessary for the analysis. Since the goal was to study injury outcomes at the person level, keeping multiple rows per crash was the correct approach. Understanding this early on was important, because misinterpreting it could have led to incorrect aggregation or loss of information.

Another challenge was dealing with the large number of variables and deciding which ones were actually useful. The datasets include many columns, but not all of them are relevant to the research question. Some variables had extremely high missingness, while others were simply not related to injury severity. The difficult part was not identifying these issues, but deciding what to do about them. Dropping variables is straightforward, but it requires confidence that they are not contributing meaningful information. This forced me to think more carefully about the purpose of the analysis and focus only on variables that directly supported the research question.

Handling categorical variables also required some thought. Variables like WEATHER_CONDITION and FIRST_CRASH_TYPE contain many different categories, some of which appear very rarely. This makes it harder to summarize the data and can make patterns less obvious. Deciding how to handle categories like UNKNOWN was not completely straightforward, since those values are part of the dataset but do not provide useful information. Removing them simplifies the analysis, but it also means losing some observations. This required weighing the tradeoff between completeness and interpretability.

Another challenge was managing the size of the datasets and keeping the workflow efficient. The full datasets are quite large, and working with them directly can slow down processing and make the notebook harder to run smoothly. Using a sample of 100,000 rows made the analysis much more manageable, but it also introduced some uncertainty about whether the sample fully represents the overall data. This required balancing performance with reliability, which is something that comes up often when working with real-world data.

Finally, one of the more general challenges was deciding how complex the analysis needed to be. There are many possible ways to approach a dataset like this, and it can be tempting to apply more advanced techniques or add more variables. However, not all of these would necessarily improve the quality of the analysis. In this project, I focused on keeping the workflow relatively simple and directly tied to the research question. This made the results easier to interpret and the process easier to explain, but it also required being intentional about what not to include.

Overall, the main challenge was making thoughtful decisions at each step of the process, rather than just applying techniques without clear reasoning.

## Reproducing

The dataset files exceed GitHub’s size limits and are hosted externally on Box using public download links.

To fully reproduce the analysis workflow from a fresh environment:

1. Clone this repository to your local machine.

2. Navigate to the project directory:

```bash
cd is477-final-project-ethan-hung
```

3. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

4. Run the full workflow pipeline:

```bash
bash run_analysis.sh
```

The workflow performs the following steps automatically:

- Downloads the required datasets from public Box links into the `data/` directory
- Verifies dataset integrity using SHA-256 checksums
- Executes the Jupyter notebook non-interactively using `nbconvert`
- Regenerates the executed notebook and analysis outputs

The workflow uses the following scripts:

- `scripts/acquire_data.py`
  - Downloads the datasets from Box into the `data/` folder

- `scripts/verify_data.py`
  - Verifies dataset integrity using SHA-256 hashes

- `run_analysis.sh`
  - Executes the full reproducible workflow pipeline

The dataset integrity hashes are stored in:

```text
checksums.txt
```

The executed notebook generated by the workflow will appear at:

```text
notebooks/analysis_executed.ipynb
```

The final visualization generated by the analysis is saved in:

```text
outputs/injury_by_person_type.png
```

This project was developed using:

- pandas 2.1.4
- matplotlib 3.8.2
- jupyter 1.1.1
- notebook 7.3.2
- ipykernel 6.29.0

## References 

Chicago Data Portal – Traffic Crashes – Crashes  
https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if  

Chicago Data Portal – Traffic Crashes – People  
https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d

McKinney, W. et al. (2022). pandas. Zenodo. https://doi.org/10.5281/zenodo.3509134

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55