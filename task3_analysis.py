# task3_analysis.py
# Task 3: Data Analysis using Pandas and NumPy

import pandas as pd
import numpy as np
import os

# Step 1: Load the cleaned CSV file
file_path = "data/trends_20260410.csv"

if not os.path.exists(file_path):
    print("CSV file not found! Please run Task 2 first.")
    exit()

df = pd.read_csv(file_path)

print("\nTrendPulse Data Analysis")
print("=" * 40)

# Step 2: Display basic information
print("\nTotal Number of Stories:", len(df))

# Step 3: Count stories per category
print("\nStories per Category:")
category_counts = df["category"].value_counts()
print(category_counts)

# Step 4: Average score per category
print("\nAverage Score per Category:")
avg_score = df.groupby("category")["score"].mean().sort_values(ascending=False)
print(avg_score)

# Step 5: Average comments per category
print("\nAverage Comments per Category:")
avg_comments = df.groupby("category")["num_comments"].mean().sort_values(ascending=False)
print(avg_comments)

# Step 6: Top 5 stories by score
print("\nTop 5 Stories by Score:")
top_score = df.nlargest(5, "score")[["title", "category", "score"]]
print(top_score)

# Step 7: Top 5 stories by number of comments
print("\nTop 5 Stories by Comments:")
top_comments = df.nlargest(5, "num_comments")[["title", "category", "num_comments"]]
print(top_comments)

# Step 8: Most active authors
print("\nTop 5 Most Active Authors:")
top_authors = df["author"].value_counts().head(5)
print(top_authors)

# Step 9: Save analysis results to a text file
if not os.path.exists("data"):
    os.makedirs("data")

output_file = "data/task3_analysis_results.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("TrendPulse Data Analysis\n")
    f.write("=" * 40 + "\n\n")

    f.write("Total Number of Stories:\n")
    f.write(str(len(df)) + "\n\n")

    f.write("Stories per Category:\n")
    f.write(category_counts.to_string() + "\n\n")

    f.write("Average Score per Category:\n")
    f.write(avg_score.to_string() + "\n\n")

    f.write("Average Comments per Category:\n")
    f.write(avg_comments.to_string() + "\n\n")

    f.write("Top 5 Stories by Score:\n")
    f.write(top_score.to_string(index=False) + "\n\n")

    f.write("Top 5 Stories by Comments:\n")
    f.write(top_comments.to_string(index=False) + "\n\n")

    f.write("Top 5 Most Active Authors:\n")
    f.write(top_authors.to_string() + "\n")

print("\nAnalysis results saved to:", output_file)