import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Run from this folder; expects Dataset (1).csv
df = pd.read_csv("Dataset (1).csv")
for col in ["Aggregate rating", "Votes", "Price range"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Task 1: rating-text proxy only; actual review text is not in this dataset.
rating_counts = df["Rating text"].fillna("Missing").value_counts()
rating_counts.to_csv("task1_rating_text_counts.csv")

# Task 2
valid = df.dropna(subset=["Votes", "Aggregate rating"])
valid.nlargest(10, "Votes")[["Restaurant Name", "City", "Votes", "Aggregate rating"]].to_csv("task2_top_votes.csv", index=False)
valid.nsmallest(10, "Votes")[["Restaurant Name", "City", "Votes", "Aggregate rating"]].to_csv("task2_lowest_votes.csv", index=False)
print("Votes-rating correlation:", valid["Votes"].corr(valid["Aggregate rating"]))

# Task 3: within-price-range service percentages
for col, filename in [("Has Online delivery", "task3_delivery_by_price.csv"),
                       ("Has Table booking", "task3_booking_by_price.csv")]:
    pd.crosstab(df["Price range"], df[col], normalize="index").mul(100).to_csv(filename)
