# Project Context: LBG Data Science Graduate Bootcamp

## Overview

This repository supports the Lloyds Banking Group (LBG) Data Science Graduate Bootcamp, a 2-month program for ~100 graduates. The bootcamp culminates in a hackathon project guided by `2025_DS_Graduate_Hackathon.md`.

## Supervisor Guidance

Supervisors will facilitate sessions with groups of 5-8 graduates. Their role is to:
- Guide graduates through the provided materials.
- Ensure everyone participates and understands the tasks.
- Address questions and provide clarification as needed.
- Encourage collaboration and adherence to Git workflows.

## Mobbing Sessions Structure

- **~100 graduates** split into groups of ~5
- **~20 supervisors** (1 per group)
- **3-hour sessions** with core material + optional extensions
- Focus on **Git workflows, collaboration, and practical skills**

## Session 1 Summary

**Topic:** Building Your First Collaborative Tool (Loan Calculator)

**Highlights:**
- Simple, focused code with pre-built scaffolding
- Clear Git workflow practice (branch, commit, push, PR)
- Optional extensions for advanced groups

**Structure:**
- Core: Implement simple functions (`simple_interest`, `score_category`, etc.)
- Provided: `main.py`, repo setup, pre-commit config
- Additional: Unit tests, Jupyter notebooks, PR practice

## Session 2 Goals

**Objective:** Teach graduates how to deploy a Python package following industry best practices.

**Core Learning Outcomes:**
1. Understand production deployment concepts
2. Set up a Python project structure (`pyproject.toml`, packaging)
3. Implement CI/CD checks (pre-commit, testing, build)
4. Create a deployable wheel file
5. Experience advanced Git workflows (feature → dev → main)
6. Work with real data (CSV) and ML models

**Constraints:**
- Must fit in 3-hour session format
- Core material achievable by all
- Optional extensions for advanced groups
- Align with final hackathon project

## Repository Structure

### Current State
```
lbg_bootcamp/
├── docs/                           # MkDocs documentation
├── src/                            # Source code (loan calculator)
│   ├── __init__.py
│   ├── credit_tools.py
│   ├── loan_calculations.py
│   └── main.py
├── tests/                          # Test files
├── 2025_DS_Graduate_Hackathon.md  # Hackathon guide
├── mkdocs.yml                      # Documentation config
├── pyproject.toml                  # Project config
└── README.md                       # Main readme
```

### Session 2 Additions Needed
- Extend `src/` with ML package structure
- Add data handling modules
- Create GitHub Actions workflows
- Add packaging configuration
- Add sample dataset (CSV)
- Create wheel building scripts

## Success Criteria

A successful Session 2 will:
- ✅ Take 3 hours with core + optional material
- ✅ Build on Session 1 (same repo, familiar structure)
- ✅ Provide pre-built scaffolding
- ✅ Result in a deployable wheel file
- ✅ Connect to hackathon requirements
- ✅ Be achievable by all skill levels