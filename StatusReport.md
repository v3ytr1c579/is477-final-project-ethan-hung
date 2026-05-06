# Interim Status Report

## 1. Progress on Project Plan Tasks

Overall, I’ve made a lot more progress on the project than I originally expected at this point. Most of the tasks from Phase 1 and Phase 2 are fully completed, and most of Phase 3 is also done.

For Phase 1, all of the planning work was completed as intended. I finalized the research question, identified datasets from the Chicago Data Portal, and set up the repository structure. This is reflected in the `ProjectPlan.md` file and how the repository is organized.

For Phase 2, I completed the full data preparation process. I downloaded both datasets (“Traffic Crashes – Crashes” and “Traffic Crashes – People”), inspected their structure, and identified key variables. Since the files are too large for GitHub, they are stored externally on Box, and the link is included in the `README.md`.

Most of the data cleaning and integration work was done inside `notebooks/analysis.ipynb`. This includes removing columns with extremely high missing values, filtering out uninformative categories like `UNKNOWN` in weather, and making sure the data was usable for analysis. I also merged the datasets using `CRASH_RECORD_ID` with a left join so that I could keep the person-level structure.

For Phase 3, the main analysis is already implemented. The notebook calculates and compares injury severity distributions across different person types (drivers, passengers, pedestrians, bicyclists). The main output visualization is saved as `outputs/injury_by_person_type.png`.

I also created the main documentation and reproducibility pieces:
- `README.md` explains the project and how to run everything
- `docs/data_dictionary.md` documents the variables used
- `requirements.txt` lists dependencies
- `run_analysis.sh` runs the notebook automatically
- `metadata.json` provides structured metadata

So at this point, the core pipeline (data → cleaning → analysis → output) is complete and reproducible.

---

## 2. Updated Timeline

Most of the planned tasks have been completed, although not exactly in the original order.

- Phase 1 (Project Planning): Completed  
  All planning tasks were finished early on, including defining the question and selecting datasets.

- Phase 2 (Data Cleaning and Integration): Completed  
  Data inspection, cleaning, and merging have all been implemented in the notebook.

- Phase 3 (Analysis and Development): Mostly completed  
  The analysis, visualization, and most documentation are done.

- Remaining tasks:  
  - Final review and small edits to documentation  
  - Completing and submitting this status report  
  - Creating the GitHub release for this milestone  

Even though this report is being written later than originally planned, most of the actual work is already finished.

---

## 3. Changes to Project Plan

There were a few important changes to the original project plan.

First, the project changed from a team-based project to an individual one. Originally, tasks were split across multiple people, but after the group split, I completed everything myself. This mainly affected how the work was structured and required simplifying the workflow.

Second, I reduced the number of datasets from three to two. The original plan included a speed camera dataset, but I decided to remove it to keep the scope manageable. The two remaining datasets (Crashes and People) were enough to answer the research question and still meet the requirement of integrating multiple datasets.

Third, I narrowed the focus of the analysis. Instead of looking at broader traffic patterns or policy-related questions, I focused specifically on how a person’s role in a crash relates to injury severity. This made the project more direct and easier to justify based on the available variables.

Finally, I had to change how the data is stored and accessed. Because the files are too large for GitHub, I used Box to host them and added clear instructions in the `README.md` on how to download and use them. I also added a `.gitignore` file to make sure large files aren’t accidentally committed.

---

## 4. Challenges and Solutions

One of the biggest challenges was understanding how the datasets were structured. The People dataset has one row per person, while the Crashes dataset has one row per crash. After merging them, the same crash shows up multiple times, once for each person involved. At first this looked like duplicated data, but I realized this was expected and actually necessary for analyzing injury outcomes at the individual level.

Another challenge was dealing with missing and messy data. A lot of variables had very high missingness or values like `UNKNOWN`. Instead of trying to fix everything, I focused on removing clearly unusable columns and filtering out uninformative values. This made the dataset cleaner without overcomplicating the process.

A major technical issue was the dataset size. Both CSV files are several hundred megabytes, which exceeds GitHub’s file size limits. To fix this, I uploaded them to Box and included a shareable link in the README. I also made sure to explain exactly where the files should go in the project folder.

I also ran into an issue with reproducibility when trying to run the notebook outside of VSCode. The `jupyter` command wasn’t recognized at first, so I switched to using `python3 -m jupyter` in the `run_analysis.sh` script. This made the workflow more reliable and easier to run in different environments.

Finally, after the project became individual, I had to adjust how I approached the work. Instead of splitting tasks, I simplified the scope and focused on finishing the full pipeline end-to-end, which ended up working better.

---

## 5. Individual Contribution

All work for this milestone was completed individually.

This includes:
- selecting and evaluating datasets  
- cleaning and integrating the data  
- writing the analysis notebook (`notebooks/analysis.ipynb`)  
- generating visualizations (`outputs/injury_by_person_type.png`)  
- writing documentation (`README.md`, data dictionary)  
- setting up reproducibility (`requirements.txt`, `run_analysis.sh`)  
- handling data storage and access (Box + `.gitignore`)  

All of this is reflected in the Git commit history.

---

## 6. Repository Artifacts

The current repository includes all major components needed to understand and reproduce the project:

- `notebooks/analysis.ipynb` → full analysis workflow  
- `outputs/injury_by_person_type.png` → final visualization  
- `docs/data_dictionary.md` → variable descriptions  
- `README.md` → project explanation and instructions  
- `requirements.txt` → dependencies  
- `run_analysis.sh` → automated execution  
- `metadata.json` → metadata  
- external Box link (documented in README.md) → dataset access

Together, these cover all parts of the pipeline from data access to final results and allow the workflow to be reproduced end-to-end.