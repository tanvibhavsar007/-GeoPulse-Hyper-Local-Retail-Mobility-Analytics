GeoPulse – Week 2, Day 1

Spatial Data Overview

1. Objective

The objective of Day 1 is to understand the GPS Pings dataset and Store Locations dataset before starting spatial data engineering using Apache Sedona.

2. GPS Pings Dataset

- File Name: "gps_pings.csv"
- Total Records: 100,000
- Total Columns: 18

Important Columns:

- PingID
- DeviceID
- SessionID
- Latitude
- Longitude
- Timestamp
- AccuracyM
- SpeedKmh
- HeadingDegrees
- AltitudeM
- DeviceType
- MovementMode
- LocationType
- EventDate
- HourOfDay
- DayOfWeek
- IsWeekend
- DataSource

Purpose:

The GPS Pings dataset contains location and movement information of devices. Latitude and Longitude are important fields used to identify the geographical positions of GPS records.

3. Store Locations Dataset

- File Name: "stores.csv"
- Total Records: 20
- Total Columns: 12

Important Columns:

- StoreID
- StoreName
- StoreCategory
- Latitude
- Longitude
- Address
- City
- Neighborhood
- OpeningTime
- ClosingTime
- StoreAreaSqFt
- IsActive

Purpose:

The Store Locations dataset contains information about different stores, including their geographical coordinates. Store Latitude and Longitude will be used to create 500-meter catchment areas around store locations.

4. Understanding Spatial Data

Spatial data represents geographical locations using coordinates.

In the GeoPulse project:

- GPS Latitude and Longitude represent device locations.
- Store Latitude and Longitude represent store locations.
- Both datasets will be used together for spatial analysis.
- Apache Sedona will help process geographical data.

5. Planned Spatial Data Engineering Tasks

The following tasks are planned for Week 2:

1. Understand GPS coordinates and store locations.
2. Explore Apache Sedona for spatial data processing.
3. Create 500-meter catchment-area polygons around store locations.
4. Intersect GPS pings with store catchment areas.
5. Prepare a spatially mapped dataset for further analysis.

6. Expected Outcome

To understand both input datasets and prepare for spatial data processing using Apache Sedona.

7. Day 1 Summary

Reviewed the GPS Pings and Store Locations datasets and identified the important geographical columns required for spatial analysis.

8. Status

Completed – Initial dataset understanding and spatial data overview documentation.