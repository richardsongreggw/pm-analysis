# PM Analysis: Android App Customer Feedback - Sibling Feature

## Project Overview
Analysis of customer feedback from Google Play Store reviews for the FamilySearch Tree Android app to identify demand for a sibling viewing feature.

## Data Source
- **Location**: `data/feedback/android/`
- **Files**: 36 CSV files (one per month)
- **Time Period**: January 2023 - December 2025
- **Naming Convention**: Files named by month/year
- **Content**: Customer reviews including:
  - Date
  - Rating
  - User name
  - Review/comments text
  - Multiple languages (includes non-English reviews)

## Analysis Goal
**Primary Question**: What percentage of users mention wanting to see information about siblings of ancestors, not just direct-line ancestors?

## Business Context

### Current State
- **Mobile App (Android/iOS)**: To view ancestor siblings in pedigree view:
  1. Open person detail page from pedigree view
  2. Navigate to parents and siblings section

- **Website**: Already has sibling affordance and view directly in pedigree view

### Feature Under Investigation
Add an affordance to view siblings of ancestors directly in the pedigree view on mobile apps (matching web functionality).

### Stakeholder Need
Senior leaders want market signals and justification for adding this feature to mobile platforms.

## Requirements
- All analysis output in US English
- Identify and quantify mentions of sibling viewing needs
- Provide evidence for product decision-making

## Next Steps
1. Explore CSV structure
2. Load and consolidate all 36 files
3. Analyze reviews for sibling-related mentions
4. Calculate percentage and extract relevant quotes
5. Generate summary report for leadership
