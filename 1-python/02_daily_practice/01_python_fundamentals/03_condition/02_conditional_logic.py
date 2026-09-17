# Project: Air Quality Condition Reporter
# Task: Build a utility that classifies real air-quality measurements.

# Website: U.S. EPA AirData
# Dataset: Daily Air Quality Index (AQI) by County
# Data: real public measurements including AQI and pollutant information.
# Why appropriate: AQI values naturally support multiple ordered categories and combined conditions.

# Level 1: Opens the AQI CSV.
# Reads the AQI value.
# Classifies each record:
# < 50 → "Good"
# 50–99 → "Moderate"
# 100–149 → "Unhealthy for Sensitive Groups"
# 150–199 → "Unhealthy"
# 200–299 → "Very Unhealthy"
# >= 300 → "Hazardous"
# Counts each category.
# Prints the totals.
# Test: All category counts should add up to the number of valid AQI records.

# Level 2: Create a "Review" classification when the AQI meets a selected threshold and another relevant data condition is satisfied.
# Use and for requirements that must both be true.
# Use or when either of two conditions qualifies.
# Use not for one inverted condition.
# Test: Each valid record should receive the intended classification according to your conditions.

# Level 3: A more complex condition involving multiple logical operators.
# Carefully order your if/elif branches so specific cases are checked before broader cases.
# Use a conditional expression for one simple two-way value.
# Print a final report containing:
# total records
# AQI category totals
# review totals
# your additional classification
# Test: The results should be consistent with the actual AQI values in the CSV,
# and every valid record should be accounted for.


file_name = "daily_aqi_by_county_2025.csv"

first_line = None
total_count = 0
# # Classifies count
good_count = 0
moderate_count = 0
unhealthy_for_some_count = 0
unhealthy_count = 0
very_unhealthy_count = 0
hazardous_count = 0
# Review count
pm25_count = 0
ozone_count = 0
other_count = 0
# Monitoring coverage
sufficient_count = 0
insufficient_count = 0

with open(file_name) as file:
    for line in file:
        line = line.strip()

        if first_line is None:
            first_line = line
            continue

        total_count += 1
        inside_quote = False
        parts = []
        current = ""
        for char in line:
            if char == '"':
                inside_quote = not inside_quote
            elif char == ',' and not inside_quote:
                parts.append(current)
                current = ""
            else:
                current += char
        parts.append(current)

        # Classifies
        aqi = int(parts[5])
        if aqi < 50:
            good_count += 1
        elif aqi < 100:
            moderate_count += 1
        elif aqi < 150:
            unhealthy_for_some_count += 1
        elif aqi < 200:
            unhealthy_count += 1
        elif aqi < 300:
            very_unhealthy_count += 1
        else:
            hazardous_count += 1

        # Review
        pollutant = parts[7]
        if aqi > 100 and pollutant == 'PM2.5':
            pm25_count += 1
        elif aqi > 100 and pollutant == 'Ozone':
            ozone_count += 1
        elif aqi > 100 and pollutant != 'PM2.5' and pollutant != 'Ozone':
            other_count += 1

        # Monitoring coverage
        sites_number = int(parts[9])
        if aqi > 100 and (pollutant == 'Ozone' or pollutant == 'PM2.5'):
            monitoring = "Sufficient" if sites_number >= 2 else "Insufficient"
            if monitoring == "Sufficient":
                sufficient_count += 1
            else:
                insufficient_count += 1
        else:
            monitoring = "Not Applicable"

total_check = (good_count
               + moderate_count
               + unhealthy_for_some_count
               + unhealthy_count
               + very_unhealthy_count
               + hazardous_count)

print("===== FINAL REPORT =====")

# Level 1: Total records
print("Total records:", total_count)

# Level 1: AQI category totals
print("\nAQI Categories:")
print("Good:", good_count)
print("Moderate:", moderate_count)
print("Unhealthy for Sensitive Groups:", unhealthy_for_some_count)
print("Unhealthy:", unhealthy_count)
print("Very Unhealthy:", very_unhealthy_count)
print("Hazardous:", hazardous_count)

# Level 2: Review totals
print("\nReview Totals:")
print("PM2.5:", pm25_count)
print("Ozone:", ozone_count)
print("Other:", other_count)

# Level 3: Monitoring coverage
print("\nMonitoring Coverage:")
print("Sufficient:", sufficient_count)
print("Insufficient:", insufficient_count)

# Check that every record was classified
print("\nRecord Check:")
print("Total records:", total_count)
print("Total AQI classifications:", total_check)
