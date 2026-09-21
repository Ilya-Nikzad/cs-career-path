# Project: Bike-Share Operations Reporter
# Client Request
# A city bike-share operator wants a small internal report to help,
# its operations team understand historical periods of unusually low or high rental demand.

# The team records hourly rental activity together with weather and operating conditions.
# They want a report that classifies demand, summarizes the conditions surrounding that demand,
# and identifies records that deserve operational review.

# The team does not want a prediction system.
# They want a transparent historical report,
# based only on the recorded data and their operational rules.

# Website: UCI Machine Learning Repository
# Dataset: Bike Sharing Dataset
# Data: 17,389 hourly observations from the Capital Bikeshare system covering 2011–2012.
# The records include rental counts, season, weather situation, temperature, humidity,
# wind speed, and date/time information.

# Business Rules
# The operations team has established these rules:
# Fewer than 100 rentals in an hour is considered low demand.
# 100 through 500 rentals is considered normal demand.
# More than 500 rentals is considered high demand.
# The recorded weather situation must be included as context when reviewing demand.
# Clear or partly cloudy conditions are considered normal operating conditions.
# Light precipitation or similar conditions should be identified separately.
# More severe weather conditions should receive additional attention.
# A high-demand period occurring during unfavorable weather conditions should be identified for operational review.
# A low-demand period should not automatically be treated as a problem; the surrounding recorded conditions matter.
# The different weather categories in the source data should remain distinguishable in the report.
# Information that is genuinely absent or unusable should not silently be treated as an ordinary measurement.
# The report must use only information contained in the dataset.

file_name = 'hour.csv'

first_line = None

# Classifies rental
low_count = 0
normal_count = 0
high_count = 0

# Demand distribution across weather
weather1_low = 0
weather1_normal = 0
weather1_high = 0

weather2_low = 0
weather2_normal = 0
weather2_high = 0

weather3_low = 0
weather3_normal = 0
weather3_high = 0

# Operational review
op_review_count = 0

# Total processed records
total_processed = 0

with open(file_name) as file:
    for line in file:
        line = line.strip()

        if first_line is None:
            first_line = line
            continue

        inside_quote = False
        parts = []
        current = ""

        for char in line:
            if char == '"':
                inside_quote = not inside_quote
            elif char == ',' and not inside_quote:
                parts.append(current)
                current = ''
            else:
                current += char

        parts.append(current)

        total_processed += 1

        # Classifies rental
        rental_count = int(parts[16])

        if rental_count < 100:
            low_count += 1
            demand_category = "low"
        elif rental_count <= 500:
            normal_count += 1
            demand_category = "normal"
        else:
            high_count += 1
            demand_category = "high"

        # Demand distribution across weather
        weather = int(parts[9])

        if weather == 1:
            if rental_count < 100:
                weather1_low += 1
            elif rental_count <= 500:
                weather1_normal += 1
            else:
                weather1_high += 1

        elif weather == 2:
            if rental_count < 100:
                weather2_low += 1
            elif rental_count <= 500:
                weather2_normal += 1
            else:
                weather2_high += 1

        elif weather == 3:
            if rental_count < 100:
                weather3_low += 1
            elif rental_count <= 500:
                weather3_normal += 1
            else:
                weather3_high += 1

        # Operational review
        status = "Unfavorable" if weather == 3 and rental_count > 500 else "Favorable"

        if status == "Unfavorable":
            op_review_count += 1

# Report
print("Low demand:", low_count)
print("Normal demand:", normal_count)
print("High demand:", high_count)

print("Weather 1 - Low:", weather1_low)
print("Weather 1 - Normal:", weather1_normal)
print("Weather 1 - High:", weather1_high)

print("Weather 2 - Low:", weather2_low)
print("Weather 2 - Normal:", weather2_normal)
print("Weather 2 - High:", weather2_high)

print("Weather 3 - Low:", weather3_low)
print("Weather 3 - Normal:", weather3_normal)
print("Weather 3 - High:", weather3_high)

print("Operational review:", op_review_count)

print("Total processed:", total_processed)
print("Totals match:", low_count + normal_count + high_count == total_processed)
