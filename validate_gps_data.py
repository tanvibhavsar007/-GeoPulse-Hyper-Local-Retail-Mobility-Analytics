import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# =====================================
# 1. PROJECT PATHS
# =====================================

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"

DOCS.mkdir(exist_ok=True)

# =====================================
# 2. READ CSV DATASETS
# =====================================

gps = pd.read_csv(DATA / "gps_pings.csv")
stores = pd.read_csv(DATA / "stores.csv")

print("GPS Dataset:", gps.shape)
print("Stores Dataset:", stores.shape)

# Convert timestamp
gps["Timestamp"] = pd.to_datetime(
    gps["Timestamp"], errors="coerce"
)

# =====================================
# 3. DATA QUALITY VALIDATION
# =====================================

results = []

def add_check(name, status, details):
    results.append({
        "Validation_Check": name,
        "Status": status,
        "Details": details
    })

# Missing values
add_check(
    "Missing Values",
    "PASS" if gps.isna().sum().sum() == 0 else "REVIEW",
    str(gps.isna().sum().sum())
)

# Duplicate PingID
duplicate_ids = gps["PingID"].duplicated().sum()

add_check(
    "Duplicate PingID",
    "PASS" if duplicate_ids == 0 else "REVIEW",
    str(duplicate_ids)
)

# Duplicate GPS events
duplicate_events = gps.duplicated(
    subset=[
        "DeviceID", "SessionID",
        "Timestamp", "Latitude", "Longitude"
    ]
).sum()

add_check(
    "Duplicate GPS Events",
    "PASS" if duplicate_events == 0 else "REVIEW",
    str(duplicate_events)
)

# Latitude and Longitude
valid_lat = gps["Latitude"].between(-90, 90)
valid_lon = gps["Longitude"].between(-180, 180)

add_check(
    "Latitude Range",
    "PASS" if valid_lat.all() else "REVIEW",
    f"{gps['Latitude'].min()} to {gps['Latitude'].max()}"
)

add_check(
    "Longitude Range",
    "PASS" if valid_lon.all() else "REVIEW",
    f"{gps['Longitude'].min()} to {gps['Longitude'].max()}"
)

# Speed validation
valid_speed = gps["SpeedKmh"].ge(0)

add_check(
    "Speed Validation",
    "PASS" if valid_speed.all() else "REVIEW",
    f"Minimum speed: {gps['SpeedKmh'].min()}"
)

# Heading validation
valid_heading = gps["HeadingDegrees"].between(0, 360)

add_check(
    "Heading Validation",
    "PASS" if valid_heading.all() else "REVIEW",
    f"Heading range: {gps['HeadingDegrees'].min()} to "
    f"{gps['HeadingDegrees'].max()}"
)

# Timestamp validation
valid_timestamps = gps["Timestamp"].notna()

add_check(
    "Timestamp Validation",
    "PASS" if valid_timestamps.all() else "REVIEW",
    f"Invalid timestamps: {(~valid_timestamps).sum()}"
)

# Check chronological order in original file order
order_check = (
    gps.groupby(["DeviceID", "SessionID"])["Timestamp"]
    .apply(lambda x: x.is_monotonic_increasing)
)

add_check(
    "Chronological Ordering",
    "PASS" if order_check.all() else "REVIEW",
    f"Sessions with ordering issues: {(~order_check).sum()}"
)

# Stores validation
add_check(
    "Duplicate StoreID",
    "PASS" if not stores["StoreID"].duplicated().any()
    else "REVIEW",
    str(stores["StoreID"].duplicated().sum())
)

add_check(
    "Stores Coordinate Range",
    "PASS" if (
        stores["Latitude"].between(-90, 90).all()
        and stores["Longitude"].between(-180, 180).all()
    ) else "REVIEW",
    "Stores latitude and longitude checked"
)

# City boundary values must be confirmed by Member 1
CITY_MIN_LAT = None
CITY_MAX_LAT = None
CITY_MIN_LON = None
CITY_MAX_LON = None

if all(v is not None for v in [
    CITY_MIN_LAT, CITY_MAX_LAT,
    CITY_MIN_LON, CITY_MAX_LON
]):
    inside = (
        gps["Latitude"].between(CITY_MIN_LAT, CITY_MAX_LAT)
        & gps["Longitude"].between(CITY_MIN_LON, CITY_MAX_LON)
    )

    add_check(
        "City Boundary",
        "PASS" if inside.all() else "REVIEW",
        f"Points outside boundary: {(~inside).sum()}"
    )
else:
    add_check(
        "City Boundary",
        "NOT_CHECKED",
        "Waiting for confirmed coordinates from Member 1"
    )

# =====================================
# 4. MOVEMENT TIME ANALYSIS
# =====================================

gps["HourOfDay"] = gps["Timestamp"].dt.hour

def get_time_period(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 22:
        return "Evening"
    else:
        return "Night"

gps["TimePeriod"] = gps["HourOfDay"].apply(
    get_time_period
)

time_analysis = pd.crosstab(
    gps["TimePeriod"],
    gps["MovementMode"]
)

print("\nTime Period Analysis:")
print(time_analysis)

# =====================================
# 5. WEEKDAY VS WEEKEND ANALYSIS
# =====================================

gps["IsWeekend"] = (
    gps["IsWeekend"].astype(str).str.lower() == "true"
)

weekday_weekend = pd.crosstab(
    gps["IsWeekend"],
    gps["MovementMode"]
)

weekday_weekend = weekday_weekend.rename(
    index={False: "Weekday", True: "Weekend"}
)

print("\nWeekday vs Weekend:")
print(weekday_weekend)

weekday_weekend.to_csv(
    DOCS / "weekday_weekend_analysis.csv"
)

# Comparison chart
weekday_weekend.plot(
    kind="bar",
    figsize=(9, 6)
)

plt.title("Weekday vs Weekend Movement")
plt.xlabel("Day Type")
plt.ylabel("GPS Ping Count")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    ROOT / "weekday_weekend_comparison.png",
    dpi=200
)

plt.close()

# =====================================
# 6. MOVEMENT TRANSITION ANALYSIS
# =====================================

gps = gps.sort_values(
    ["DeviceID", "SessionID", "Timestamp"]
).copy()

group = gps.groupby(["DeviceID", "SessionID"])

gps["PreviousMovementMode"] = (
    group["MovementMode"].shift(1)
)

gps["PreviousTimestamp"] = (
    group["Timestamp"].shift(1)
)

gps["PreviousLatitude"] = (
    group["Latitude"].shift(1)
)

gps["PreviousLongitude"] = (
    group["Longitude"].shift(1)
)

gps["ModeChanged"] = (
    gps["MovementMode"] != gps["PreviousMovementMode"]
)

# Time gap in minutes
gps["TimeGapMinutes"] = (
    gps["Timestamp"] - gps["PreviousTimestamp"]
).dt.total_seconds() / 60

# Calculate distance between consecutive pings
lat1 = np.radians(gps["PreviousLatitude"])
lat2 = np.radians(gps["Latitude"])

lon1 = np.radians(gps["PreviousLongitude"])
lon2 = np.radians(gps["Longitude"])

a = (
    np.sin((lat2 - lat1) / 2) ** 2
    + np.cos(lat1) * np.cos(lat2)
    * np.sin((lon2 - lon1) / 2) ** 2
)

gps["DistanceKm"] = (
    6371 * 2 * np.arcsin(np.sqrt(a.clip(0, 1)))
)

# Derived speed between pings
gps["DerivedSpeedKmh"] = np.where(
    gps["TimeGapMinutes"] > 0,
    gps["DistanceKm"] * 60 / gps["TimeGapMinutes"],
    np.nan
)

# Flag movement mode changes for review
transitions = gps[
    gps["ModeChanged"]
    & gps["PreviousMovementMode"].notna()
].copy()

transitions["TransitionStatus"] = "REVIEW"

transition_report = transitions[[
    "DeviceID",
    "SessionID",
    "Timestamp",
    "PreviousMovementMode",
    "MovementMode",
    "TimeGapMinutes",
    "DistanceKm",
    "DerivedSpeedKmh",
    "SpeedKmh",
    "TransitionStatus"
]]

transition_report.to_csv(
    DOCS / "movement_transition_report.csv",
    index=False
)

print("\nMovement Transitions:")
print("Transitions flagged:", len(transitions))

# =====================================
# 7. GPS MOVEMENT VISUALIZATION
# =====================================

plt.figure(figsize=(10, 7))

for mode, group_data in gps.groupby("MovementMode"):
    plt.scatter(
        group_data["Longitude"],
        group_data["Latitude"],
        s=3,
        alpha=0.4,
        label=mode
    )

plt.scatter(
    stores["Longitude"],
    stores["Latitude"],
    marker="^",
    s=70,
    label="Stores"
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("GeoPulse GPS Movement Preview")
plt.legend()
plt.tight_layout()

plt.savefig(
    ROOT / "gps_movement_preview.png",
    dpi=200
)

plt.close()

# =====================================
# 8. DEVICE MOVEMENT TRAJECTORY
# =====================================

device = gps["DeviceID"].iloc[0]

trajectory = gps[
    gps["DeviceID"] == device
].sort_values("Timestamp")

plt.figure(figsize=(10, 7))

plt.plot(
    trajectory["Longitude"],
    trajectory["Latitude"],
    marker="o",
    markersize=3
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title(f"Movement Trajectory - {device}")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    ROOT / "device_movement_trajectory.png",
    dpi=200
)

plt.close()

# =====================================
# 9. SAVE VALIDATION REPORT
# =====================================

report = pd.DataFrame(results)

report.to_csv(
    DOCS / "gps_validation_report.csv",
    index=False
)

# =====================================
# 10. DATA QUALITY REPORT
# =====================================

with open(
    DOCS / "data_quality_report.md",
    "w",
    encoding="utf-8"
) as file:

    file.write("# GeoPulse - Data Quality Report\n\n")

    file.write(f"- GPS Records: {len(gps)}\n")
    file.write(f"- Unique Devices: {gps['DeviceID'].nunique()}\n")
    file.write(f"- Store Records: {len(stores)}\n")
    file.write(f"- Movement Transitions Flagged: {len(transitions)}\n\n")

    file.write("## Validation Results\n\n")
    file.write(report.to_markdown(index=False))

    file.write("\n\n## Time Period Analysis\n\n")
    file.write(time_analysis.to_markdown())

    file.write("\n\n## Weekday vs Weekend Analysis\n\n")
    file.write(weekday_weekend.to_markdown())

print("\nAll validation and analysis tasks completed!")
print("Reports and visualizations generated successfully.")