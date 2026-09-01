"""
Setup script for LBG Loan Calculator
This is the OLD WAY of packaging Python projects (before pyproject.toml)
Students will learn why pyproject.toml is better!
"""

from setuptools import setup, find_packages

setup(
    name="loan-calculator",
    version="1.0.0",
    description="LBG Loan Processing System",
    author="LBG Data Science Graduates",
    author_email="ds-grads@lbg.com",
    packages=find_packages(),
    install_requires=[
        "pandas==2.0.3",
        "click==8.1.7",
        "openpyxl==3.1.2",
        "python-dotenv==1.0.0",
    ],
    python_requires=">=3.9",
)