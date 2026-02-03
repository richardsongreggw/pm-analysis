# PM Analysis Workspace

Product Management analysis projects: customer feedback analysis, usage analytics, and data-driven business case development.

## Overview

This workspace contains multiple PM analysis projects, each with their own data sources, analysis notebooks, and presentation materials. Each project is self-contained in its own directory under `projects/`.

## Projects

### 1. [Sibling Feature for Mobile Pedigree](projects/sibling-feature/)
**Status**: ✅ Complete - Ready for stakeholder presentation
**Date**: February 2026

Business case analysis for adding sibling viewing affordance to mobile pedigree view.

**Key Findings**:
- 49% of engaged web users toggle siblings (514K of 1M users)
- 38% of all web pedigree users engage with feature
- All major competitors (Ancestry, MyHeritage, FindMyPast) have this feature
- 23 Android reviews explicitly request sibling viewing

**Deliverables**:
- Jupyter notebooks with combined web analytics + mobile feedback analysis
- HTML slides (7 slides, FamilySearch branded, 1680x946 optimized)
- PDF report for distribution
- Competitor screenshots and customer quotes

[📊 View Project Details →](projects/sibling-feature/README.md)

---

## Project Structure

Each project follows this structure:

```
projects/[project-name]/
├── README.md              # Project summary, findings, and artifact inventory
├── CONTEXT.md             # Background, requirements, business context
├── data/                  # Project-specific data
│   ├── raw/              # Source data (typically excluded from git)
│   ├── processed/        # Analysis outputs
│   └── screenshots/      # Supporting visuals
├── notebooks/            # Jupyter analysis notebooks
├── presentations/        # Slides, reports, deliverables
└── scripts/              # Automation and utility scripts
```

## Workspace Resources

### Brand Guidelines
**Location**: `~/Dev/familysearch-brand/familysearch-brand-guidelines.pdf`

- Primary Color: FamilySearch Green (#87b940)
- Typography: Noto Sans Light / Helvetica
- **Note**: Work presentations use FamilySearch branding; personal projects do not

### Tools & Dependencies
- Python 3.12 (venv per project)
- Jupyter / IPython for analysis notebooks
- pandas, numpy for data analysis
- reportlab for PDF generation
- GitHub CLI for repository management

### Getting Started with a New Project

1. Create project directory: `mkdir -p projects/[project-name]/{data,notebooks,presentations,scripts}`
2. Create context file: `projects/[project-name]/CONTEXT.md`
3. Set up Python environment: `python3 -m venv projects/[project-name]/venv`
4. Start analysis in Jupyter notebook
5. Document findings in `projects/[project-name]/README.md`

---

## Repository Info

**Owner**: Gregg Richardson (@richardsongreggw)
**Created**: February 2026
**License**: Private - Internal Use

---

## Quick Links

- [Sibling Feature Project](projects/sibling-feature/README.md)
- [FamilySearch Brand Guidelines](~/Dev/familysearch-brand/)
- [GitHub Repository](https://github.com/richardsongreggw/pm-analysis)

---

_Last Updated: February 3, 2026_
