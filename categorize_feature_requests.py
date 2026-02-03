#!/usr/bin/env python3
"""
Categorize sibling-related reviews to identify feature requests
"""

import pandas as pd

print("=" * 80)
print("Categorizing Sibling-Related Reviews")
print("=" * 80)

# Load the sibling mentions
sibling_mentions = pd.read_csv('data/sibling_mentions.csv')

print(f"\nTotal sibling-related reviews: {len(sibling_mentions)}")
print("\n" + "=" * 80)
print("ALL REVIEWS WITH SIBLING/FAMILY MENTIONS")
print("=" * 80)

# Display all reviews for manual categorization
for i, (idx, row) in enumerate(sibling_mentions.iterrows(), 1):
    print(f"\n{'='*80}")
    print(f"Review #{i}")
    print(f"{'='*80}")
    print(f"Date: {row['Review Submit Date and Time']}")
    print(f"Rating: {row['Star Rating']} stars")
    print(f"Language: {row['Reviewer Language']}")
    print(f"\nReview Text:")
    print(f"{row['Review Text']}")
    print()

print("\n" + "=" * 80)
print("Review complete - see all 23 reviews above")
print("=" * 80)
