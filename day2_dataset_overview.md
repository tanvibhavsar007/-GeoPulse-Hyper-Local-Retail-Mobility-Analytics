GeoPulse – Dataset Overview

1. Project Information

Project Name: GeoPulse – Hyper-Local Retail Mobility Analytics

Role: Member 2 – GPS Movement Simulation & Validation

Tools: Python, Pandas, NumPy, Matplotlib, Microsoft Excel

2. Dataset Description

GPS Pings Dataset

- File Name: gps_pings.csv
- Records: 100,000
- Columns: 18
- Unique Devices: 1,000

Stores Dataset

- File Name: stores.csv
- Records: 20
- Columns: 12

3. GPS Dataset Columns

Important columns identified:

- PingID
- DeviceID
- SessionID
- Timestamp
- Latitude
- Longitude
- SpeedKmh
- HeadingDegrees
- MovementMode
- IsWeekend

4. Initial GPS Coordinate Inspection

Latitude

- Minimum: 17.6468
- Maximum: 17.7268

Longitude

- Minimum: 83.1785
- Maximum: 83.2585

Note: City boundary verification requires confirmation of the simulated boundary coordinates.

5. Initial Data Inspection

- Reviewed the GPS Pings dataset.
- Reviewed the Stores dataset.
- Identified important GPS-related columns.
- Checked latitude and longitude ranges.
- Reviewed movement mode and timestamp information.
- Started initial data quality validation.

6. Planned Movement Analysis

- Morning, Afternoon and Evening movement patterns.
- Weekday versus Weekend distribution.
- Movement mode distribution.
- Consecutive movement mode transition analysis.
- Identification of potentially unrealistic movement transitions.

7. Coordination with Member 1

- Discussed GPS movement generation logic.
- Discussed weekday and weekend analysis.
- Discussed randomly generated movement modes.
- Requested city boundary coordinates.
- Discussed reviewing sudden movement mode changes.

8. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Microsoft Excel
- GitHub

9. Next Steps

- Complete GPS data validation.
- Verify city boundary coordinates.
- Analyse movement patterns.
- Identify suspicious movement transitions.
- Generate validation reports and visualizations.

Day 1 Summary

Completed initial dataset inspection and GPS coordinate range checks. Prepared the Python validation script and identified additional movement analysis requirements.