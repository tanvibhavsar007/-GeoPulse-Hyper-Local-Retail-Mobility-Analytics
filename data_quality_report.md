# GeoPulse - Data Quality Report

- GPS Records: 100000
- Unique Devices: 1000
- Store Records: 20
- Movement Transitions Flagged: 69086

## Validation Results

| Validation_Check        | Status      | Details                                         |
|:------------------------|:------------|:------------------------------------------------|
| Missing Values          | PASS        | 0                                               |
| Duplicate PingID        | PASS        | 0                                               |
| Duplicate GPS Events    | PASS        | 0                                               |
| Latitude Range          | PASS        | 17.6468 to 17.7268                              |
| Longitude Range         | PASS        | 83.1785 to 83.2585                              |
| Speed Validation        | PASS        | Minimum speed: 0.0                              |
| Heading Validation      | PASS        | Heading range: 0.01 to 360.0                    |
| Timestamp Validation    | PASS        | Invalid timestamps: 0                           |
| Chronological Ordering  | PASS        | Sessions with ordering issues: 0                |
| Duplicate StoreID       | PASS        | 0                                               |
| Stores Coordinate Range | PASS        | Stores latitude and longitude checked           |
| City Boundary           | NOT_CHECKED | Waiting for confirmed coordinates from Member 1 |

## Time Period Analysis

| TimePeriod   |   Cycling |   Driving |   Stationary |   Walking |
|:-------------|----------:|----------:|-------------:|----------:|
| Afternoon    |      4022 |     12201 |         7998 |     16066 |
| Evening      |      3238 |      9707 |         6350 |     12832 |
| Morning      |      1911 |      5620 |         3837 |      7684 |
| Night        |       894 |      2573 |         1675 |      3392 |

## Weekday vs Weekend Analysis

| IsWeekend   |   Cycling |   Driving |   Stationary |   Walking |
|:------------|----------:|----------:|-------------:|----------:|
| Weekday     |      7289 |     21472 |        14163 |     28665 |
| Weekend     |      2776 |      8629 |         5697 |     11309 |