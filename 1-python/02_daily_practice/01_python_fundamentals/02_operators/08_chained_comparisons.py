# Project: Track Rating Validator
# Task: Build a utility that analyzes real music tracks and validates their ratings and lengths using range checks.

# Website: Python for Everybody Code Samples
# Dataset: tracks.csv
# Data: Real music-track records containing title, artist, album, playing count, rating, and length.

# Header:
# parts[0] → title
# parts[1] → artist
# parts[2] → album
# parts[3] → count playing times
# parts[4] → rating
# parts[5] → length

# Level 1: Read the track data.
# Check whether each rating falls within a valid range.
# Count valid and invalid ratings.
# Display the results.
# Keep the existing track-analysis functionality you completed previously where useful

# Level 2: Add a valid track-length range.
# Count tracks inside and outside that range.
# Add the results to the report.
# Keep Level 1.

# Level 3: Create a final validation summary.
# Show total tracks, valid/invalid ratings, and valid/invalid lengths.
# Calculate the percentage of tracks passing each validation.
# Keep Levels 1–2.

file_name = "tracks.csv"

total_tracks = 0

count_valid_rate = 0
invalid_rate = 0

count_valid_length = 0
invalid_length = 0

with open(file_name) as file:
    for line in file:
        line = line.strip()
        total_tracks += 1
        parts = line.split(',')

        if 0 <= int(parts[4]) <= 100:
            count_valid_rate += 1
        else:
            invalid_rate += 1

        if 100000 <= int(parts[5]) <= 800000:
            count_valid_length += 1
        else:
            invalid_length += 1

percentage_valid_rate = count_valid_rate / total_tracks * 100
percentage_valid_length = count_valid_length / total_tracks * 100

if count_valid_rate + invalid_rate == total_tracks:
    percentage_valid_rate = count_valid_rate / total_tracks * 100
else:
    print("ERROR: Rating count doesn't match total tracks.")

if count_valid_length + invalid_length == total_tracks:
    percentage_valid_length = count_valid_length / total_tracks * 100
else:
    print("ERROR: Length count doesn't match total tracks.")

print(f"Total tracks: {total_tracks}")
print(f"Number of valid rates: {count_valid_rate}")
print(f"Number of invalid rates: {invalid_rate}")
print(f"Number of valid lengths: {count_valid_length}")
print(f"Number of invalid lengths: {invalid_length}")
print(f"Percentage of valid rates: {percentage_valid_rate}")
print(f"Percentage of valid lengths: {percentage_valid_length}")

