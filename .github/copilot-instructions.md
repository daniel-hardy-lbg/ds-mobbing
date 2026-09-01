GitHub Copilot Instructions - Session 2: Risk Assessment & Deployment

🎯 Session Overview
Session Title: Your First Production Ticket - Risk Assessment Implementation & Deployment

JIRA Ticket: JIRA-2024 - Implement Risk Assessment & Prepare for Deployment
Priority: High | Sprint: Current

📋 What Students Are Building
The Scenario
Students have received their first production ticket. While they were in bootcamp (Session 1), the Platform Team took their loan calculation functions and built them into a production CLI tool. Now students need to:

- Implement business logic: Two risk assessment functions
- Write comprehensive tests: Unit tests with boundary cases
- Configure the project: Prepare for production deployment
- Deploy the package: Build and validate in production-like environment

Key Learning Objectives
- Modern Python packaging with pyproject.toml
- Pre-commit hooks for code quality automation
- Unit testing with pytest and coverage
- CI/CD pipeline workflow
- Git branching strategy (feature → dev → main)
- Building and deploying Python packages

🏗️ Project Structure
lbg_bootcamp/
├── src/
│   ├── main.py                      ✅ PROVIDED - CLI with user prompts
│   ├── config.py                    ✅ PROVIDED - Configuration system
│   ├── loan_calculations.py         ✅ FROM SESSION 1 - Interest calculations
│   ├── credit_tools.py              ✅ FROM SESSION 1 - Credit scoring
│   └── risk_thresholds.py           🔨 STUDENTS IMPLEMENT - Risk assessment
├── tests/
│   ├── test_loan_calculations.py    ✅ FROM SESSION 1
│   ├── test_credit_tools.py         ✅ FROM SESSION 1
│   └── test_risk_thresholds.py      🔨 STUDENTS IMPLEMENT - Risk tests
├── data/
│   └── sample_applications.csv      ✅ PROVIDED - 1000 test applications
├── pyproject.toml                   📝 STUDENTS CONFIGURE - Modern packaging
├── .gitignore                       📝 STUDENTS COMPLETE - Git ignore patterns
├── .pre-commit-config.yaml          📝 STUDENTS CONFIGURE - Quality hooks
├── requirements.txt                 ✅ PROVIDED - Old style (for comparison)
├── setup.py                         ✅ PROVIDED - Old style (for comparison)
└── run_ci_checks.py                 ✅ PROVIDED - CI/CD simulator

🔨 Student Implementation Tasks
Part 1: Project Configuration (45 min)
Task 1.1: Configure pyproject.toml
Students fill in the modern Python packaging configuration:

What they configure:

[project] section:
name: Creative package name (e.g., "totally-fair-loans")
version: "2.0.0" (since this is Session 2)
authors: Their name and email
dependencies: Production packages (pandas, click, openpyxl)
[project.optional-dependencies] dev: Development tools (pytest, black, ruff, mypy, pre-commit)
[project.scripts]: CLI entry points

Why this matters:

- Replaces multiple old-style files (setup.py, requirements.txt, MANIFEST.in)
- Standard for modern Python projects
- Required for deployment to production systems
- Separates production vs development dependencies

Task 1.2: Complete .gitignore
Students add patterns to prevent committing sensitive or unnecessary files:

Patterns to add:

- Virtual environments: lbg_venv/, test_venv/, ci_test_venv/
- Python artifacts: __pycache__/, *.pyc, *.egg-info/
- Build artifacts: dist/, build/
- Data files (may contain PII): data/*.csv, data/*.xlsx
- Environment files: .env
- Testing: .pytest_cache/, .coverage, htmlcov/

Why this matters:

- Prevents accidentally committing 10,000+ virtual environment files
- Protects sensitive customer data (loan applications, credit scores)
- Keeps repository clean and professional

Task 1.3: Configure .pre-commit-config.yaml
Students set up automated quality checks that run before every commit:

Hooks to configure:

repos:
  # Basic file checks
  - pre-commit-hooks (end-of-file-fixer, trailing-whitespace, check-yaml)
  
  # Ruff - Fast linter with auto-fix
  - ruff (catches code quality issues)
  
  # Black - Code formatter
  - black (enforces consistent style)
  
  # MyPy - Type checker
  - mypy (catches type errors)
  
  # Nbstripout - Clears Jupyter notebook outputs
  - nbstripout (prevents data leaks in notebooks)

Why this matters:

- Catches issues BEFORE they reach code review
- Ensures consistent code quality across team
- Prevents deployment of poorly formatted code
- Nbstripout prevents accidental data leaks in notebooks (critical for capstone)
Demo file: messy_example.py is provided to show pre-commit in action

Part 2: Business Logic Implementation (45 min)
Function 1: check_debt_to_income() in src/risk_thresholds.py
What it does: Calculates the debt-to-income ratio and validates against a threshold.

Function signature:

def check_debt_to_income(
    monthly_payment: float,
    monthly_income: float,
    max_dti_ratio: float
) -> tuple[bool, float]:

Business logic:

DTI = monthly_payment / monthly_income
Pass if DTI <= max_dti_ratio
Return: (passes_check, actual_dti)

Examples:

Payment 1500, Income 5000, Max 0.43 → (True, 0.30)
Payment 2500, Income 5000, Max 0.43 → (False, 0.50)

Teaching focus:

This is SIMPLE on purpose - emphasize they're implementing real banking logic
Focus is on deployment workflow, not complex algorithms

Function 2: check_min_credit_score() in src/risk_thresholds.py
What it does: Checks if credit score meets minimum requirement.

Function signature:

def check_min_credit_score(
    credit_score: int,
    min_credit_score: int
) -> tuple[bool, str]:

Business logic:

Compare credit_score >= min_credit_score
Return: (passes_check, informative_message)

Examples:

Score 720, Min 650 → (True, "Credit score 720 meets minimum of 650")
Score 600, Min 650 → (False, "Credit score 600 below minimum of 650")

Teaching focus:

Practice returning tuples
Creating user-friendly messages
Boundary testing (exactly at minimum)

Part 3: Testing & Quality (40 min)
Tests in tests/test_risk_thresholds.py
Test structure (AAA pattern):

def test_something():
    # Arrange: Set up test data
    # Act: Call the function
    # Assert: Check the result

Required tests for check_debt_to_income():

test_dti_under_threshold() - Normal case (30% < 43%)
test_dti_exactly_at_threshold() - Boundary case (43% = 43%)
test_dti_over_threshold() - Rejection case (50% > 43%)

Required tests for check_min_credit_score():

test_credit_score_above_minimum() - Normal pass (720 > 650)
test_credit_score_exactly_at_minimum() - Boundary case (650 = 650)
test_credit_score_below_minimum() - Rejection case (600 < 650)

Coverage expectations:

Run: pytest --cov=src --cov-report=term-missing
Target: 70%+ coverage on business logic (main.py excluded)
Should achieve: ~87-100% coverage on implemented functions

Why boundary testing matters:

Bugs hide at boundaries (=, <, <=)
Real-world loans get rejected/approved at exact thresholds
Professional testing requires edge case coverage

Part 4: Deployment Workflow (30 min)
Git Branching Strategy
feature/risk-assessment (student work)
    ↓ merge
dev (team testing)
    ↓ merge
main (production-ready)
    ↓ deploy
🚀 PRODUCTION SERVERS

Commands students use:

# Start: Create feature branch
git checkout -b feature/risk-assessment

# Work: Commit with pre-commit checks
git add .
git commit -m "Implement risk assessment functions"

# Merge to dev
git checkout dev
git merge feature/risk-assessment

# CI/CD simulation
python run_ci_checks.py

# Merge to main (in real workflow)
git checkout main
git merge dev

CI/CD Pipeline Simulation
File: run_ci_checks.py simulates automated deployment pipeline

Pipeline steps:

- Create clean virtual environment (simulates new VM)
- Install dependencies from pyproject.toml
- Run Ruff linting
- Run Black formatting check
- Run MyPy type checking
- Run pytest with coverage
- Build wheel package (.whl)
- Report success/failure

Success output:

✅ ALL CHECKS PASSED!
Package built: dist/totally-fair-loans-2.0.0-py3-none-any.whl
Ready for deployment!

If any step fails: Pipeline stops, student must fix and retry

Part 5: Victory Lap (10 min)
Testing in Production-Like Environment
Simulation:

# Clean slate
deactivate
rm -rf lbg_venv

# Fresh "production" environment
python -m venv prod_test
source prod_test/bin/activate

# Install the built package
pip install dist/totally-fair-loans-2.0.0-py3-none-any.whl

# Test CLI with different threshold scenarios
loan-calculator single

Test scenarios:

Strict policy: min_credit_score=750, max_dti=0.30
Lenient policy: min_credit_score=600, max_dti=0.50
Standard policy: min_credit_score=650, max_dti=0.43

Key insight: Same code, different results based on configurable thresholds!

🎓 Teaching Philosophy
What Students Should Focus On
- Modern Python packaging - pyproject.toml is standard
- Quality automation - Pre-commit hooks prevent bad code
- Testing discipline - Can't deploy without tests
- Deployment workflow - Feature → Dev → Main → Production
- Clean repositories - Gitignore protects sensitive data

What Students Should NOT Worry About
- Complex algorithms (functions are intentionally simple)
- CLI implementation (already provided by Platform Team)
- Advanced Git workflows (basic merge is fine)
- Perfect code on first try (pre-commit fixes it!)

Common Struggles & Solutions
Issue: "Import error when running tests"

Cause: Missing tests/__init__.py
Solution: Create empty tests/__init__.py file

Issue: "Pre-commit blocking my commit"

Cause: Code quality issues detected
Solution: Let pre-commit auto-fix, or read error messages

Issue: "CI/CD pipeline failing"

Cause: Tests failing, linting errors, or type issues
Solution: Run checks locally first: pytest -v, ruff check src/, black --check src/

Issue: "Package name already exists"

Cause: Reusing common name in pyproject.toml
Solution: Be creative! "totally-fair-loans", "lbg-loan-analyzer", etc.

🔍 Key Files to Review When Helping Students
If student has implementation issues:
src/risk_thresholds.py - Check function logic, return tuples
tests/test_risk_thresholds.py - Check AAA pattern, assertions
src/main.py - See how CLI calls their functions

If student has configuration issues:
pyproject.toml - Check dependencies, package name, version
.pre-commit-config.yaml - Check hook configurations
.gitignore - Check patterns include venv and data files

If student has testing issues:
Run: pytest -v to see which tests fail
Run: pytest --cov=src --cov-report=term-missing for coverage
Check: tests/__init__.py exists

If student has deployment issues:
Check: Virtual environment activated
Check: pip install -e ".[dev]" ran successfully
Check: run_ci_checks.py output for specific failure

🚀 Expected Deliverables
By end of session, students should have:

Configured project:

✅ pyproject.toml with package name, version, dependencies
✅ .gitignore with comprehensive patterns
✅ .pre-commit-config.yaml with all hooks

Implemented functions:

✅ check_debt_to_income() with proper logic
✅ check_min_credit_score() with informative messages

Comprehensive tests:

✅ 6+ unit tests covering normal and boundary cases
✅ 70%+ code coverage on business logic

Working deployment:

✅ Pre-commit hooks passing
✅ CI/CD simulation passing
✅ .whl package built in dist/
✅ Tested in clean environment

Git workflow:

✅ Feature branch created
✅ Commits with pre-commit checks
✅ Merged to dev branch

📚 Session-Specific Context
Session 1 Context (What They Already Know)
Basic Python functions
Git basics (commit, push, pull)
Simple calculations (interest, credit scoring)
Files already implemented: loan_calculations.py, credit_tools.py

Session 2 New Concepts
Python packaging (pyproject.toml)
Pre-commit hooks
Unit testing with pytest
CI/CD pipelines
Git branching strategies
Building distributable packages

Session 3 Preview (What's Coming)
Students will apply these concepts to a capstone project with real-world complexity.

🎯 When Helping Students, Remember:
- Functions are intentionally simple - Focus is on workflow, not algorithms
- Pre-commit is your friend - Let it fix formatting automatically
- Tests prove the code works - Essential for production deployment
- pyproject.toml is modern standard - setup.py is legacy
- Boundary cases matter - Professional testing requires edge cases
- Clean repos matter - Gitignore prevents data leaks and bloat

🆘 Quick Reference Commands
# Environment setup
python -m venv lbg_venv
source lbg_venv/bin/activate
pip install -e ".[dev]"
