# Cognifyz Data Analysis Internship — Level 3 Report

Dataset: `Dataset (1).csv`  
Records: 9,551  
Columns: 22

## Task 1 — Restaurant Reviews
The dataset does **not** contain customer review text. It contains a `Rating text` category, so text keyword analysis, actual review length, and review-length/rating relationship cannot be calculated from this file.

As a clearly labelled proxy only, `Rating text` was mapped as:
- Positive: Excellent, Very Good, Good
- Neutral: Average
- Negative: Poor
- Unrated / other: remaining categories (including Not rated)

The proxy counts and percentages are in `task1_sentiment_proxy.csv`; the original category distribution is in `task1_rating_text_distribution.csv`. This is not sentiment analysis of written reviews.

## Task 2 — Votes Analysis
- Highest votes: Toit (Bangalore), 10,934 votes, rating 4.8.
- Lowest votes: Cantinho da Gula (S��o Paulo), 0 votes, rating 0.0.
- Pearson correlation between Votes and Aggregate rating: **0.314** (positive, modest association).

The top and lowest vote tables are included as CSV files. The lowest-vote table may contain multiple restaurants tied at zero votes.

## Task 3 — Price Range vs Online Delivery and Table Booking
Percentages are calculated within each price-range group.

### Online delivery availability
|   Price range |    No |   Yes |
|--------------:|------:|------:|
|             1 | 84.23 | 15.77 |
|             2 | 58.69 | 41.31 |
|             3 | 70.81 | 29.19 |
|             4 | 90.96 |  9.04 |

### Table booking availability
|   Price range |    No |   Yes |
|--------------:|------:|------:|
|             1 | 99.98 |  0.02 |
|             2 | 92.32 |  7.68 |
|             3 | 54.26 | 45.74 |
|             4 | 53.24 | 46.76 |

The charts and detailed counts are included in this ZIP. Results describe association in this dataset; they do not prove that price causes service availability.

## Included files
- Python analysis script
- Dataset copy
- Task result CSVs
- Four charts
- This report
