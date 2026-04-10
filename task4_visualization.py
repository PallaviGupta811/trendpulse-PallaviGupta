 # task4_visualization.py
# Task 4: Data Visualization using Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Improve plot aesthetics
sns.set(style="whitegrid")

# Step 1: Load the cleaned CSV file
file_path = "data/trends_20260410.csv"

if not os.path.exists(file_path):
    print("CSV file not found! Please run Task 2 first.")
    exit()

df = pd.read_csv(file_path)

# Create a folder for visualizations
output_dir = "visualizations"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Generating visualizations...")

# ---------------------------------------------------------
# Visualization 1: Number of Stories per Category
# ---------------------------------------------------------
plt.figure()
category_counts = df["category"].value_counts()

sns.barplot(
    x=category_counts.index,
    y=category_counts.values
)

plt.title("Number of Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(f"{output_dir}/stories_per_category.png")
plt.show()

# ---------------------------------------------------------
# Visualization 2: Average Score per Category
# ---------------------------------------------------------
plt.figure()
avg_score = df.groupby("category")["score"].mean().sort_values(ascending=False)

sns.barplot(
    x=avg_score.index,
    y=avg_score.values
)

plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(f"{output_dir}/average_score_per_category.png")
plt.show()

# ---------------------------------------------------------
# Visualization 3: Average Comments per Category
# ---------------------------------------------------------
plt.figure()
avg_comments = df.groupby("category")["num_comments"].mean().sort_values(ascending=False)

sns.barplot(
    x=avg_comments.index,
    y=avg_comments.values
)

plt.title("Average Comments per Category")
plt.xlabel("Category")
plt.ylabel("Average Comments")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(f"{output_dir}/average_comments_per_category.png")
plt.show()

# ---------------------------------------------------------
# Visualization 4: Category Distribution (Pie Chart)
# ---------------------------------------------------------
plt.figure()
plt.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Category Distribution of Trending Stories")
plt.axis("equal")

plt.savefig(f"{output_dir}/category_distribution.png")
plt.show()

print("Visualizations saved in the 'visualizations' folder.")
