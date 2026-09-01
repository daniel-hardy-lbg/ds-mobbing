# LBG Data Science Bootcamp - Loan Calculator

**Session 2 Starting Point**: Add Configurable Risk Thresholds

Welcome to Session 2! While you were in bootcamp, the Platform Team built your Session 1 loan calculator into a production batch processor! 🎉

Now we need YOUR help: Business wants configurable risk thresholds so loan officers can adjust approval criteria based on market conditions.

## 🎯 Your Mission (JIRA-2024)

**Task**: Implement risk threshold functions for the loan approval system.

### What You Already Have (Working Code):

✅ **Complete & Working:**
- `src/main.py` - CLI calculator + batch processor
- `src/config.py` - Configuration system
- `src/loan_calculations.py` - Interest calculations (Session 1)
- `src/credit_tools.py` - Credit scoring (Session 1)
- `data/sample_applications.csv` - 1000 test applications
- `tests/test_loan_calculations.py` - Session 1 tests
- `tests/test_credit_tools.py` - Session 1 tests
- `requirements.txt` - Old-style dependencies
- `setup.py` - Old-style packaging

### What You'll Build (Session 2):

🔨 **You Implement:**
1. `src/risk_thresholds.py` - Two functions:
   - `check_debt_to_income()` - Calculate and validate DTI ratio
   - `check_min_credit_score()` - Check if applicant meets minimum credit score

2. `tests/test_risk_thresholds.py` - Unit tests for above functions

📝 **You Configure:**
1. `pyproject.toml` - Modern Python packaging (replaces setup.py + requirements.txt)
2. `.gitignore` - Protect sensitive data and environment files
3. `.pre-commit-config.yaml` - Add quality gates (ruff, black, mypy, nbstripout)

## 🏗️ Project Structure

```
lbg_bootcamp/
├── src/
│   ├── main.py                      ✅ Complete (CLI + batch processor)
│   ├── config.py                    ✅ Complete (configuration)
│   ├── loan_calculations.py         ✅ Complete (Session 1)
│   ├── credit_tools.py              ✅ Complete (Session 1)
│   └── risk_thresholds.py           🔨 You implement this
├── tests/
│   ├── test_loan_calculations.py    ✅ Complete (Session 1)
│   ├── test_credit_tools.py         ✅ Complete (Session 1)
│   └── test_risk_thresholds.py      🔨 You implement this
├── data/
│   └── sample_applications.csv      ✅ 1000 applications
├── pyproject.toml                   � You configure this
├── .gitignore                       📝 You complete this
├── .pre-commit-config.yaml          📝 You complete this
├── requirements.txt                 ✅ Old style (for comparison)
├── setup.py                         ✅ Old style (for comparison)
└── run_ci_checks.py                 ✅ CI/CD simulator
```

## 🚀 Getting Started

### Step 1: Setup Environment
```bash
# Create virtual environment
python -m venv lbg_venv
source lbg_venv/bin/activate  # Windows: lbg_venv\Scripts\activate

# Install dependencies (old way - you'll modernize this!)
pip install -r requirements.txt
```

### Step 2: Understand What's There
```bash
# Try the CLI (it won't work yet - your functions aren't implemented!)
python -m src.main single 20000 50000 720

# Try batch processing (also won't work yet)
python -m src.main batch data/sample_applications.csv output.xlsx
```

### Step 3: Follow Session 2 Guide

Your instructor will guide you through:
1. **Project Configuration** (45 min) - pyproject.toml, gitignore, pre-commit
2. **Build the Feature** (45 min) - Implement the 2 risk threshold functions
3. **Testing & Quality** (40 min) - Write tests, check coverage
4. **Deployment Workflow** (30 min) - Git workflow, CI/CD simulation
5. **Victory Lap** (10 min) - Test your deployed package!

## 📚 Learning Objectives

By the end of Session 2, you'll understand:
- ✅ Modern Python project structure (`pyproject.toml`)
- ✅ Dependency management (production vs development)
- ✅ Git workflow (feature branches, dev, main)
- ✅ Pre-commit hooks (automated quality checks)
- ✅ Unit testing and coverage
- ✅ CI/CD pipeline basics
- ✅ Python packaging and distribution

## 🎓 Success Criteria

Your code is ready when:
- ✅ Both risk threshold functions implemented correctly
- ✅ All tests pass with >70% coverage
- ✅ Pre-commit hooks configured and passing
- ✅ Package builds successfully
- ✅ Batch processor handles 1000 applications

---

## 📖 View the Session Docs

```bash
# 1. Clone the repo
git clone git@ghe.service.group:Hamza-Albakkar/lbg-bootcamp.git
cd lbg-bootcamp

# 2. Start the docs site (venv is pre-installed — no setup needed)
source ../.venv/bin/activate && mkdocs serve
```

Then open **http://127.0.0.1:8000/lbg_bootcamp/** in your browser.

---

**Ready? Let's build something production-ready!** 🚀
- ✅ Dependency management (production vs dev)
- ✅ Pre-commit hooks (automated quality gates)
- ✅ Unit testing with pytest
- ✅ Batch processing with pandas
- ✅ CI/CD concepts and "route to live"
- ✅ Building Python packages (wheel files)

## ⚙️ Current State

This branch represents the **starting point** for Session 2:
- Session 1 code is complete ✅
- Batch processor backbone is ready ✅
- Configuration files are minimal (you'll expand them) 📝
- Decision logic is missing (you'll write it) 🔨

---

**💡 Ready?** Follow along with your instructor to complete your first production ticket!