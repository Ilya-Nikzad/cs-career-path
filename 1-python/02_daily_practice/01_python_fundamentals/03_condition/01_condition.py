# Project: Earthquake Event Triage Reporter
# Task: Build a small Python utility that reads earthquake records and assigns a simple category based on earthquake magnitude,
# then progressively adds depth and nested decision logic.
import csv

# Website: USGS Earthquake Catalog
# Dataset: USGS Earthquake Catalog CSV data
# Data: real earthquake records including time, depth, mag, place, and other fields

# Level 1: Opens the earthquake CSV.
# Loops through every record.
# Reads the mag value.
# Classifies each earthquake:
# >= 6.0 → "Major"
# >= 5.0 → "Strong"
# >= 4.5 → "Moderate"
# otherwise → "Lower"
# Counts how many earthquakes fall into each category.
# Prints the totals.

# Level 2: Build directly on Level 1.
# Add: A depth classification:
# < 70 km → "Shallow"
# 70–300 km → "Intermediate"
# > 300 km → "Deep"
# Count each depth category.
# Print both the magnitude and depth summaries.

# Build on Levels 1–2. Add nested conditions to create a simple "Priority" classification:
# First determine whether the earthquake is Major, Strong, Moderate, or Lower.
# Inside that decision, use depth to determine the priority.
# For example, a stronger earthquake can receive a higher priority than a lower-magnitude one, while depth can further change the result.
# Count the resulting priority categories.
# Print a final report containing:
# total earthquakes
# magnitude categories
# depth categories
# priority categories


file_name = "USGS_Earthquake_4.5_month.csv"

first_line = None

total_earthquakes = 0

major_list = []
strong_list = []
moderate_list = []
lower_list = []

shallow_count = 0
intermediate_count = 0
deep_count = 0

high_alert_count = 0
low_alert_count = 0


with open(file_name, encoding= "utf-8") as file:

    for line in file:
        line = line.strip()
        parts = []
        current = ""
        inside_quotes = False

        for char in line:
            if char == '"':
                inside_quotes = not inside_quotes

            elif char == ',' and not inside_quotes:
                parts.append(current )
                current = ""

            else:
                current += char

        parts.append(current)

        if first_line == None:
            first_line = parts
            continue
        total_earthquakes += 1


        mag = float(parts[4])
        if mag >= 6:
            major_list.append(mag)
        elif mag >= 5:
            strong_list.append(mag)
        elif mag >= 4.5:
            moderate_list.append(mag)
        else:
            lower_list.append(mag)


        depth = float(parts[3])
        if depth < 70:
            shallow_count += 1
        elif depth >= 70 and depth < 300:
            intermediate_count += 1
        else:
            deep_count += 1

        # Priority classification
        if mag >= 6:
            if depth >= 300:
                high_alert_count += 1
            else:
                low_alert_count += 1
        elif mag >= 5:
            if depth >= 70 and depth < 300:
                high_alert_count += 1
            else:
                low_alert_count += 1
        elif mag >= 4.5:
            if depth < 70:
                high_alert_count += 1
            else:
                low_alert_count += 1
        else:
            low_alert_count += 1


header = []
for index, part in enumerate(first_line):
    header.append(f"index: {index}, part: {part}")

print("\n\nHerder:")
print(header)
print(f"Total earthquakes: {total_earthquakes}")
print()
print(f"Major Magnitude Earthquake Total: {len(major_list)}")
print(f"Strong Magnitude Earthquake Total: {len(strong_list)}")
print(f"Moderate Magnitude Earthquake Total: {len(moderate_list)}")
print(f"Lower Magnitude Earthquake Total: {len(lower_list)}")
print(f"Shallow Depth Earthquake Total: {shallow_count}")
print(f"Intermediate Depth Earthquake Total: {intermediate_count}")
print(f"Deep Depth Earthquake Total: {deep_count}")
print(f"High Alert Earthquake: {high_alert_count}, Lower Alert Earthquake: {low_alert_count}")











