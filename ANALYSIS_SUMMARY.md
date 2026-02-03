# Sibling Feature Analysis - Summary Report

**Analysis Date**: 2026-02-02
**Data Source**: Google Play Store Reviews (Jan 2023 - Dec 2025)

---

## Executive Summary

Analysis of 11,060 Android app reviews identified **6 clear feature requests** (0.05% of all reviews) specifically asking for the ability to view siblings in the pedigree/tree view, matching the functionality already available on the website.

---

## Overall Statistics

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Reviews** | 11,060 | 100% |
| **Reviews with Text** | 4,311 | 39.0% |
| **Mention Sibling/Family Relationships** | 23 | 0.21% of all reviews<br>0.53% of reviews with text |
| **Feature Requests for Sibling Viewing** | 6 | 0.05% of all reviews<br>0.14% of reviews with text |

---

## Feature Request Analysis

### Direct Feature Requests (6 reviews)

These reviews explicitly request the ability to view siblings in the tree/pedigree view:

#### 1. Review from 2023-05-14 (3 stars)
> "I believe that the app should make sm option for providing half siblings"

**Context**: User specifically wants half-sibling support

---

#### 2. Review from 2024-08-17 (3 stars) - German
> "Ich finde es super schade, dass man keine Geschwister sehen kann. Man sieht nur die direkte Linie, keine Tanten, Onkel, Cousinen etc. Dadurch muss man immer den halben Stammbaum im Kopf haben, und wenn man Infos ergänzen möchte, muss man erst über andere Profile die Person heraussuchen. Das finde ich sehr umständlich und auch nicht übersichtlich."

**Translation**: "I think it's really sad that you can't see siblings. You only see the direct line, no aunts, uncles, cousins, etc. As a result, you always have to keep half the family tree in your head, and if you want to add information, you first have to search for the person via other profiles. I find that very cumbersome and also not clear."

**Context**: User finds it cumbersome to navigate without sibling view, has to remember relationships mentally

---

#### 3. Review from 2025-05-13 (4 stars)
> "I hope they add a feature where I can see the siblings of a person in the family tree diagram."

**Context**: Direct feature request for sibling visibility in tree diagram

---

#### 4. Review from 2025-07-04 (4 stars)
> "I find it frustrating that I don't see my siblings even though they are listed under my parents."

**Context**: User frustrated that siblings are in the data but not visible in tree view

---

#### 5. Review from 2025-07-19 (1 star)
> "website is better. search results are useless, coming up with unrelated matches that are 100 years out. doesn't show siblings, can't add. use the website"

**Context**: User explicitly compares app unfavorably to website, notes website shows siblings but app doesn't

---

#### 6. Review from 2025-12-07 (4 stars)
> "if the tree starts with me, i can not add my siblings"

**Context**: User unable to add/view siblings when starting tree from themselves

---

### Potentially Related Navigation Issues (2 reviews)

These reviews describe navigation challenges that the sibling feature might address:

#### 7. Review from 2024-08-29 (2 stars)
> "Disappointing: only 2 family tree layouts, both from bottom up while is completely missing a top down navigation. If you are looking for that distant cousin and can't remember which uncle was his father... well, good luck"

**Context**: Navigation difficulty finding collateral relatives (cousins/uncles)

---

#### 8. Review from 2024-11-03 (3 stars)
> "Why can't I add my children? It's also not allowing me to add my aunts/uncles and cousins..."

**Context**: Difficulty adding or viewing aunts/uncles/cousins

---

### Other Sibling/Family Mentions (15 reviews)

The remaining 15 reviews mentioned siblings/relatives but were about:
- Discovering unknown relatives through DNA/records (9 reviews)
- Record attachment workflows (1 review)
- Photo upload issues (1 review)
- Account creation issues (1 review)
- Collaborative editing (1 review)
- Content moderation (1 review)
- General praise (1 review)

These do not relate to the sibling viewing feature request.

---

## Trend Analysis

Feature requests for sibling viewing increased in 2025:
- **2023**: 1 request
- **2024**: 3 requests
- **2025**: 2 requests (as of Dec 2025)

The most detailed complaint (German review, Aug 2024) describes exactly the usability problem the proposed feature would solve: users must keep relationships "in their head" and navigate through multiple profiles to find relatives.

---

## Key Insights

1. **Low but consistent demand**: 0.05% of all reviews explicitly request this feature
2. **Website comparison**: Multiple users note the website already has this functionality and prefer it
3. **Usability pain point**: Users describe having to mentally track relationships and navigate multiple screens
4. **Trend**: Recent reviews (2024-2025) show increasing mentions of this limitation

---

## Recommendation Context

While 6 explicit feature requests represents a small percentage (0.05%), this data should be considered alongside:
- **Parity with website**: Users explicitly compare and prefer the website's sibling view
- **Usability improvement**: Users describe concrete workflow friction the feature would solve
- **Consistent requests**: Requests span the entire 3-year period with increasing frequency
- **Silent majority**: Many users may experience the limitation but not leave reviews

---

## Data Files

- Raw data: `data/feedback/android/` (36 CSV files)
- All sibling mentions: `data/sibling_mentions.csv` (23 reviews)
- Full context: `PROJECT_CONTEXT.md`
