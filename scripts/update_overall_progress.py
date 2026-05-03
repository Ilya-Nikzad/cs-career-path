import os

COURSES = [
    "1-python/01_p4e_course",
    "1-python/03_problem_solving/python_data_structures",
    "1-python/03_problem_solving/problems_algorithms_flowcharts",
]

def count_files(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".py") or f.endswith(".ipynb"):
                total += 1
    return total

def get_progress(path):
    return min(count_files(path) * 10, 100)

def calculate_overall():
    total = sum(get_progress(c) for c in COURSES)
    return int(total / len(COURSES))

overall = calculate_overall()

bar_len = 20
filled = int(overall / 5)
bar = "█" * filled + "░" * (bar_len - filled)

print("OVERALL:", overall)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- PROGRESS_START -->"
end = "<!-- PROGRESS_END -->"

if start not in content or end not in content:
    print("ERROR: progress markers missing in README")
    exit(1)

new_section = f"""<!-- PROGRESS_START -->
## 📊 Overall Progress

{bar} {overall}%
<!-- PROGRESS_END -->"""

updated = content.split(start)[0] + new_section + content.split(end)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)

print("README updated successfully")