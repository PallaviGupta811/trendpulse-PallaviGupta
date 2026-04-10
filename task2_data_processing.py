# task2_data_processing.py
# Task 2: Clean JSON and save as CSV

import json
import pandas as pd
from datetime import datetime
import os

# Step 1: define JSON filename from Task 1
filename_json = "data/trends_20260407.json"

# Step 2: load JSON data
try:
    with open(filename_json, "r", encoding="utf-8") as f:
        stories = json.load(f)
except FileNotFoundError:
    print("JSON file not found! Make sure Task 1 has been run.")
    stories = []

# Step 3: clean data
clean_stories = []
for story in stories:
    # Ensure all required fields exist
    if all(field in story for field in ["post_id", "title", "category", "score", "num_comments", "author", "collected_at"]):
        clean_stories.append(story)

# Step 4: convert to DataFrame
df = pd.DataFrame(clean_stories)

# Optional: see first 5 rows and info
print(df.head(5))
print(df.info())

# Step 5: save as CSV
if not os.path.exists("data"):
    os.makedirs("data")

filename_csv = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".csv"
df.to_csv(filename_csv, index=False, encoding="utf-8")

print("Saved cleaned data to", filename_csv)