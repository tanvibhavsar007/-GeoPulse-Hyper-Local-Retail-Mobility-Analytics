# -GeoPulse-Hyper-Local-Retail-Mobility-Analytics
# Project Overview:
GeoPluse is a Data analytics Project focused on understanding hyper-local retail mobility pattern using GPS Movement Data. the project Aims to analyse loaction based movement, Identify Mobility trends, Validate GPS Data, and Generate Meaningul Insights related to retail activities.
# Project Objectives:
-simulate realistic GPS movements within a defined city areas.
-analyse location based movement patterns.
-Identify Customer Mobility Trends across different time period.
-perform GPS data quality checks and validation.
-Visualise movement patterns and Mobility Insights.
-Generate Useful Insights to support retail location and Business decisions
# Tools and Technologies:
-Pyhton
-Pandas
-Matplotlib
-GPS Movement Simulation
-Data Analytics
-Data Visualization
Additional Tools and Technologies will be added as the project progress.

# Project Structure:
The project work is organised into different tasks and weekly milestones, including GPS movement simulation, data validation, mobility analysis, and insight generation.

# Team Responsibilities:
The project is developed collaboratively, with team members handling different tasks such as GPS simulation, data validation, data processing, analysis, and visualization.
# License:
This Project is License under The MIT License 

# Day 1: day1_workinglog.md
# Day 1: Project Setup and Repository initialization
Tasks Completed:
-created the GeoPluse project repository on GitHub
-Added the REDME.md file with basic project Information 
-Added the License file
-Created the Initial Project Folder structure
-Organized folders for data, documentation and Python Scripts
-Reviewed the project objectives and Team Responsibilities.
# Tools Used:
- GitHub
- Visual Studio Code
- Python
# Outcome:
Successfully completed the initial project setup and repository organization Prepared the Workspace for upcoming GPS data validation and Movement analysis tasks.

# Day 2: day2_worklog.md
# Day 2: GPS Data Validation and Movement Analysis
Tasks Completed:
- Reviwed the GPS Pings and Stores datasets.
- Devloped the Python validation script named validate_gps_data.py.
- Checked missing values and duplicate GPS records.
- Performed Latitude and longitude range validation.
- Checked timestamp validity and Chronological ordering.
- Performed speed and heading validation.
- Analysed movement patterns across different time period.
- Started Weekday vs Weekend Movement analysis.
- Generated GPS movement Visualizations.
- Analysed Consecutive Movement mode changes and flagged transitions for review.
# Files Generated:
- gps_validation_report.csv
- data_quality_report.md
- movement_transition_report.csv
- weekday_weekend_analysis.csv
- gps_movement_preview.png

# Day 3 - Weekday vs Weekend Movement Analysis
Work Completed
- Performed weekday and weekend movement analysis.
- Compared Cycling, Driving, Stationary and Walking patterns.
- Reviewed the movement transition report.
- Examined selected records using time gaps, distance and speed values.
- Reviewed GPS movement patterns and identified transitions for further investigation.

Files Created & Uploaded on GitHub:
- day3_analysis_notes.md
- weekday_weekend_analysis.csv
- movement_transition_report.csv
# Status:
Completed the initial weekday vs weekend movement analysis and reviewed movement transitions. Identified records requiring further validation of speed and distance values. Generated the analysis reports and prepared the files for GitHub Documentation.
  
- device_movement_trajectory.png
- weekday_weekend_comparison.png
# Overview:
A total of 69,086 movement mode transitions were flagged for review.These transitions required further invistigation and should not automatically be considered unrealistic.
# Outcome:
Sucessfully developed and executed the Initial GPS Validation and Movement analysis scripts and generated supporting reports and visualizations.

# Day 4: GPS Data Validtaion and Quality Review
Task Completed:
- Reviewed the GPS Validation Report.
- Reviewed the overall data quality report.
- Checked the missing values and Duplicate records.
- Verified latitude, longitude, speed and heading validation results.
- Reviewed timestamp validation and Chronological ordering.
- Checked store data validation results.
- Reviewed time-period and weekday versus weekend analysis results.
- Identified City Boundary validation from the confirmation of coordinates from Member 1

# Day 5: GPS Movement Visualizations Review
Task Completed:
- Reviewed the generated GPS movement visualizations.
- Examined device movement trajectory patterns.
- Reviewed the GPS movement preview.
- Checked the weekday versus weekend comparison visualization.
- prepared visualization outputs for GitHub documentation.
  Files created and Uploaded on GitHub:
  - device_movement_trajectory.png
  - gps_movement_preview.png
Status:
    Completed the initial review of GPS movement visualizations and uploaded two visualizations files to GitHub repository.

# Day 6: Weekday vs Weekend Comparison Visualization
Tasks Completed:
- Reviewed the generated weekday versus weekend comparison chart.
- Compared Cycling, Driving, Stationary and Wlaking movement patterns.
- Examined the differences in GPS movement records between weekdays and weekend.
- Reviewed the visual representation of movement patterns.
   Files Created & Uploaded on GitHub:
  - weekday_weekend_comparison.png
Status:
Sucessfully reviewed and uploaded the Weekday versus Weekend comparison visualization to the GitHub repository.

# Week 2 – Spatial Data Engineering
# Day 1 – Spatial Data Overview

Objective:
To understand the GPS Pings dataset and Store Locations dataset before starting spatial data engineering using Apache Sedona.

Tasks Completed:
- Reviewed the GPS Pings dataset.
- Reviewed the Store Locations dataset.
- Identified important geographical columns such as Latitude and Longitude.
- Understood how GPS locations and store locations will be used for spatial analysis.
- Reviewed the planned spatial data engineering tasks for Week 2.

Dataset Details:

- GPS Pings Dataset: 100,000 records and 18 columns.
- Store Locations Dataset: 20 records and 12 columns.

File Added and Uploaded to GitHub:
"docs/day1_spatial_data_overview.md"

Status:
Completed – Initial spatial data understanding and documentation.

# Week 2 – Day 2: Apache Sedona Setup and Validation

Task Completed:

- Installed and configured Java JDK 17 (Eclipse Temurin).
- Verified Java installation using the terminal.
- Checked Python 3.11.9 and pip installation.
- Created and activated the Python virtual environment (".venv").
- Opened and checked the GeoPulse project structure in VS Code.
- Reviewed the GPS datasets ("gps_pings.csv" and "stores.csv").
- Checked the GPS data validation script ("validate_gps_data.py").
- Reviewed the existing GPS movement visualizations.

Outcome:

Completed the basic Java and Python environment setup and validation for the GeoPulse project.
Prepared the development environment for Apache Sedona-related work.

Status: Completed

# Week 2 – Day 3: Dataset Preparation

Work Completed:

- Received six processed CSV files from Member 1.
- Created the "data/processed" folder.
- Organised GPS and store-related datasets.
- Checked the GeoPulse project structure in VS Code.
- Started preparing datasets for Apache Sedona spatial data processing.

Current Status: Initial dataset organisation completed. Data inspection and spatial processing are pending.
