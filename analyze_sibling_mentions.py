#!/usr/bin/env python3
"""
Analysis of Google Play Store reviews to identify sibling-related mentions
"""

import pandas as pd
import glob
from pathlib import Path

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 150)

print("=" * 80)
print("FamilySearch Android App - Sibling Feature Analysis")
print("=" * 80)

# Load all CSV files
csv_files = sorted(glob.glob('data/feedback/android/*.csv'))
print(f"\n1. DATA LOADING")
print(f"   Found {len(csv_files)} CSV files")
print(f"   Date range: {Path(csv_files[0]).stem.split('_')[-1]} to {Path(csv_files[-1]).stem.split('_')[-1]}")

# Load all files into a single dataframe
dfs = []
for file in csv_files:
    try:
        df = pd.read_csv(file, encoding='utf-16')
        dfs.append(df)
    except Exception as e:
        print(f"   Error loading {file}: {e}")

# Combine all dataframes
all_reviews = pd.concat(dfs, ignore_index=True)
print(f"   Total reviews loaded: {len(all_reviews):,}")

# Basic statistics
print(f"\n2. REVIEW STATISTICS")
print(f"   Total reviews: {len(all_reviews):,}")
print(f"   Reviews with text: {all_reviews['Review Text'].notna().sum():,}")
print(f"   Reviews without text: {all_reviews['Review Text'].isna().sum():,}")

# Filter for reviews that have actual text content
reviews_with_text = all_reviews[all_reviews['Review Text'].notna() & (all_reviews['Review Text'].str.strip() != '')].copy()
print(f"   Reviews with text content: {len(reviews_with_text):,}")
print(f"   Percentage with text: {len(reviews_with_text)/len(all_reviews)*100:.1f}%")

print(f"\n   Top 10 Languages:")
for lang, count in all_reviews['Reviewer Language'].value_counts().head(10).items():
    print(f"      {lang}: {count:,}")

# Define search terms for sibling-related mentions
sibling_keywords = [
    'sibling', 'siblings',
    'brother', 'brothers', 'sister', 'sisters',
    'aunt', 'aunts', 'uncle', 'uncles',
    'nephew', 'nephews', 'niece', 'nieces',
    'cousin', 'cousins'
]

# Create search pattern (case insensitive)
pattern = '|'.join(sibling_keywords)

# Search for sibling mentions in review text
sibling_mentions = reviews_with_text[reviews_with_text['Review Text'].str.contains(pattern, case=False, na=False)].copy()

print(f"\n3. SIBLING RELATIONSHIP MENTIONS")
print(f"   Reviews mentioning siblings/related family: {len(sibling_mentions):,}")
print(f"   Percentage of ALL reviews: {len(sibling_mentions)/len(all_reviews)*100:.2f}%")
print(f"   Percentage of reviews WITH text: {len(sibling_mentions)/len(reviews_with_text)*100:.2f}%")

# Display sample of sibling-related reviews
print(f"\n4. SAMPLE REVIEWS (First 10)")
print("=" * 80)
for i, (idx, row) in enumerate(sibling_mentions.head(10).iterrows(), 1):
    print(f"\n   Review #{i}")
    print(f"   Date: {row['Review Submit Date and Time']}")
    print(f"   Rating: {row['Star Rating']} stars")
    print(f"   Language: {row['Reviewer Language']}")
    print(f"   Review: {row['Review Text']}")
    print("-" * 80)

# Save sibling-related reviews to CSV
output_file = 'data/sibling_mentions.csv'
sibling_mentions.to_csv(output_file, index=False, encoding='utf-8')
print(f"\n5. OUTPUT")
print(f"   Saved {len(sibling_mentions):,} reviews to {output_file}")

print("\n" + "=" * 80)
print("Analysis complete!")
print("=" * 80)
