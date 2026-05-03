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
    print(f"[DEBUG] {path} -> {files} files")
    return min(files * 10, 100)

def calculate_overall():
    total = 0
    for course in COURSES:
        total += get_progress(course)
    overall = int(total / len(COURSES))
    print(f"[DEBUG] TOTAL OVERALL -> {overall}")
    return overall

overall = calculate_overall()

bar_len = 20
filled = int(overall / 5)
bar = "█" * filled + "░" * (bar_len - filled)

print("[DEBUG] Updating README...")

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"## 📊 Overall Progress\s*\n.*",
    f"## 📊 Overall Progress\n\n{bar} {overall}%",
    content
)

if content == new_content:
    print("[DEBUG] No change detected in README section")
else:
    print("[DEBUG] README updated")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("[SUCCESS] Overall progress updated:", overall)