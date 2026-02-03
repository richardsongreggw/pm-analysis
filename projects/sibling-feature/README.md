# Sibling Feature Analysis - Project Summary

**Last Updated**: February 3, 2026
**Status**: Analysis Complete - Ready for Stakeholder Presentation

## Project Overview
Analysis to justify adding sibling viewing affordance to mobile pedigree view, matching web functionality.

## Business Case - Three Pillars
1. **Market Standard** - All competitors (Ancestry, MyHeritage, FindMyPast) have it
2. **Customer Voice** - Android users explicitly requesting it (23 reviews over 3 years)
3. **Proven Value** - 49% of engaged web users actively use sibling toggle

## Key Findings
- **Web Usage**: 49% of engaged users (514,746 of 1,047,944 who toggled ancestors)
- **Web Baseline**: 38% of all pedigree users (593,667 of 1.56M views)
- **Mobile Demand**: 0.53% of reviews with text mention sibling/family features
- **Data Period**: Web (90 days: Nov 2025 - Feb 2026), Mobile (3 years: 2023-2025)

---

## Data Sources

### Web Analytics (Adobe)
**Location**: `data/analytics/adobe/`
- `tree_views_2025-11-05_to_2026-02-02_90day.csv` - Primary 90-day analysis
- `tree_views_2026-02-01_1day.csv` - Single day snapshot (for reference)

**Metrics Extracted**:
- Pedigree views, ancestor toggles, sibling toggles (total and sequential)

### Mobile Feedback (Google Play)
**Location**: `data/feedback/android/`
- 36 CSV files (one per month, Jan 2023 - Dec 2025)
- **Processed Output**: `data/sibling_mentions.csv` (23 relevant reviews)

**Note**: iOS App Store data not available for export/analysis

### Competitor Screenshots
**Location**: `data/screenshots/competitors/`
- `ancestry-app-sibling-view.png`
- `myheritage-app-sibling-view.png`
- `findmypast-app-sibling-view.png`

---

## Analysis Artifacts

### Jupyter Notebooks
**Location**: `notebooks/`

1. **`sibling_feature_analysis.ipynb`**
   - Initial exploratory analysis of Google Play reviews
   - Keyword search for sibling-related mentions
   - Exports: `data/sibling_mentions.csv`

2. **`sibling_feature_business_case.ipynb`** ⭐ **PRIMARY NOTEBOOK**
   - Combines web analytics + mobile feedback
   - Parses Adobe Analytics funnel data
   - Generates executive summary with three-pillar narrative
   - Exports: `data/processed/sibling_feature_business_case_summary.json`

### Presentation Materials
**Location**: `presentations/`

1. **`sibling_feature_business_case_slides.html`** ⭐ **FOR STAKEHOLDER MEETINGS**
   - 7 slides with Reveal.js framework
   - Optimized for 1680x946 browser window
   - FamilySearch branded (colors, fonts)
   - **Sections**:
     - Title (three pillars)
     - Market Standard
     - Competitor Screenshots (all 3)
     - Customer Voice (3 quotes)
     - Customer Voice continued (3 more quotes)
     - Proven Value (49% & 38% stats)
     - Recommendation

2. **`sibling_feature_business_case_report.pdf`** ⭐ **FOR DISTRIBUTION**
   - Professional report format
   - Same content as slides
   - Easy to email/print
   - FamilySearch branded

### Scripts
**Location**: `scripts/`

- **`generate_pdf_report.py`**
  - Python script using ReportLab to generate PDF
  - Run: `source venv/bin/activate && python3 scripts/generate_pdf_report.py`
  - Outputs to: `presentations/sibling_feature_business_case_report.pdf`

---

## How to Use These Artifacts

### For Stakeholder Presentations
1. Open `presentations/sibling_feature_business_case_slides.html` in browser
2. Resize browser to 1680x946 for optimal display
3. Use arrow keys to navigate slides
4. Lead with 49% stat, emphasize competitive gap

### For Email Distribution
- Share `presentations/sibling_feature_business_case_report.pdf`

### For Deep-Dive Questions
- Reference `notebooks/sibling_feature_business_case.ipynb` for methodology
- All calculations and data sources documented

### To Regenerate PDF
```bash
cd /Users/ppgreggrichardson/Dev/pm-analysis
source venv/bin/activate
python3 scripts/generate_pdf_report.py
```

### To Re-run Analysis
- Open `notebooks/sibling_feature_business_case.ipynb` in VS Code
- Run all cells (already executed, outputs saved)
- Update data sources if needed

---

## Project Context & Requirements

See `SIBLING_FEATURE_CONTEXT.md` for:
- Detailed project background
- Data source descriptions
- Business requirements
- Current state vs. proposed feature

---

## Brand Guidelines

**Location**: `~/Dev/familysearch-brand/familysearch-brand-guidelines.pdf`

Key brand elements applied:
- **Primary Color**: FamilySearch Green (#87b940)
- **Typography**: Noto Sans Light / Helvetica
- **Style**: Clean, authentic, professional

**Personal Note**: Work presentations use FamilySearch branding. Personal projects do not.
(Documented in `~/.claude.md`)

---

## Next Steps

1. ✅ Present business case to stakeholders
2. ⬜ Get approval to proceed
3. ⬜ Coordinate with mobile dev team
4. ⬜ Define acceptance criteria
5. ⬜ Plan implementation timeline

---

## File Structure
```
pm-analysis/
├── SIBLING_FEATURE_CONTEXT.md       # Project background & requirements
├── SIBLING_FEATURE_SUMMARY.md       # This file - artifact inventory
├── ANALYSIS_SUMMARY.md              # High-level findings (generated earlier)
├── data/
│   ├── analytics/adobe/             # Web usage data (Adobe Analytics)
│   ├── feedback/android/            # Mobile reviews (Google Play, 36 files)
│   ├── screenshots/competitors/     # Competitor app screenshots (3 files)
│   ├── processed/                   # Analysis outputs
│   │   └── sibling_feature_business_case_summary.json
│   └── sibling_mentions.csv         # Extracted review quotes
├── notebooks/
│   ├── sibling_feature_analysis.ipynb           # Initial review analysis
│   └── sibling_feature_business_case.ipynb      # ⭐ Primary analysis notebook
├── presentations/
│   ├── sibling_feature_business_case_slides.html  # ⭐ HTML slides (Reveal.js)
│   └── sibling_feature_business_case_report.pdf   # ⭐ PDF report
└── scripts/
    └── generate_pdf_report.py       # PDF generation script
```

---

## Dependencies

- Python 3.12 (venv)
- Jupyter / IPython
- pandas, numpy
- reportlab (for PDF generation)
- poppler-utils (for reading brand guidelines PDF)

Install: `pip install pandas numpy reportlab pillow jupyter`

---

## Questions or Updates?

When returning to this project:
1. Read this summary first
2. Check `SIBLING_FEATURE_CONTEXT.md` for business context
3. Review `notebooks/sibling_feature_business_case.ipynb` for methodology
4. Use presentations as starting point for stakeholder discussions
