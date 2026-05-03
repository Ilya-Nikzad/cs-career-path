import os
import re

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
    files = count_files(path)
    return min(files * 10, 100)

def calculate_overall():
    total = 0
    for course in COURSES:
        total += get_progress(course)
    return int(total / len(COURSES))

overall = calculate_overall()

bar_len = 20
filled = int(overall / 5)
bar = "█" * filled + "░" * (bar_len - filled)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r"## 📊 Overall Progress\s*\n.*",
    f"## 📊 Overall Progress\n\n{bar} {overall}%",
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Overall progress updated:", overall)