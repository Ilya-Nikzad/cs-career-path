# Project — Track Status Reporter
# Purpose: Analyze real music-track data and classify tracks into simple two-way statuses.
# Website: Python for Everybody (PY4E)
# Dataset: tracks.csv
# Data: Music track records containing information about individual tracks.

# Level 1: Load a real music-track dataset.
# Calculate the required track measurement.
# Assign one of two statuses based on a chosen condition.
# Count each status.
# Display the results.

# Level 2: Add another two-way classification.
# Count its two outcomes.
# Keep Level 1.
#
# Level 3: Create a final summary.
# Calculate percentages.
# Keep Levels 1–2.

# Header:
# parts[0] → title
# parts[1] → artist
# parts[2] → album
# parts[3] → count playing times
# parts[4] → rating
# parts[5] → length

file_name = "tracks.csv"

high_rate = 0
low_rate = 0
long_length = 0
short_length = 0
total_tracks = 0

with open(file_name) as file:
    for line in file:
        line = line.strip()

        total_tracks += 1

        parts = line.split(',')
        rating_num = int(parts[4])
        length_num = int(parts[5])

        rate_status = "High" if rating_num > 50 else "Low"
        high_rate += rate_status == "High"
        low_rate += rate_status == "Low"

        length_status = "Long" if length_num > 180000 else "Short"
        long_length += length_status == "Long"
        short_length += length_status == "Short"

high_rate_percentage = high_rate / total_tracks * 100
long_length_percentage = long_length / total_tracks * 100

print(f"Rating higher than 50: {high_rate}")
print(f"Rating 50 or lower: {low_rate}")
print(f"Long track: {long_length}")
print(f"Short track: {short_length}")
print(f"High rating percentage: {high_rate_percentage}")
print(f"Long length percentage: {long_length_percentage}")
print(f"Total tracks: {total_tracks}")

