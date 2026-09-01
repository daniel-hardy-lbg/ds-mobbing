#!/usr/bin/env python3
"""
CI/CD Pipeline Simulation Script
Simulates what happens when code is pushed to production.
"""

import subprocess
import sys
import time


def print_header(text):
    """Print a fancy header."""
    print("\n" + "+" + "=" * 58 + "+")
    print(f"| {text:^56} |")
    print("+" + "=" * 58 + "+")


def print_step(step_num, total_steps, name):
    """Print step header."""
    print(f"\n{'─' * 60}")
    print(f"  [{step_num}/{total_steps}] {name}")
    print("─" * 60)


def run_command(step_num, total_steps, name, command):
    """Run a command and return success status."""
    print_step(step_num, total_steps, name)
    print(f"Running: {command}\n")

    start_time = time.time()
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    elapsed = time.time() - start_time

    if result.returncode == 0:
        print(f"\n✅ {name} PASSED ({elapsed:.2f}s)")
        if result.stdout and len(result.stdout) < 500:
            print(result.stdout)
        return True
    else:
        print(f"\n❌ {name} FAILED ({elapsed:.2f}s)")
        if result.stderr:
            print("Error output:")
            print(result.stderr)
        if result.stdout:
            print(result.stdout)
        return False


def main():
    """Run all CI/CD checks."""
    print_header("LBG CI/CD Pipeline Simulation")

    # Step 0: Create and activate virtual environment
    print_step(0, 7, "Environment Setup")
    print("Creating virtual environment: ci_test_venv\n")

    venv_result = subprocess.run(
        "python3 -m venv ci_test_venv", shell=True, capture_output=True, text=True
    )

    if venv_result.returncode != 0:
        print("❌ Failed to create virtual environment")
        return 1

    print("✅ Virtual environment created")
    print("Installing dependencies...\n")

    install_result = subprocess.run(
        "ci_test_venv/bin/pip install -q -r requirements.txt",
        shell=True,
        capture_output=True,
        text=True,
    )

    if install_result.returncode != 0:
        print("❌ Failed to install dependencies")
        return 1

    print("✅ Dependencies installed")

    # Define checks with venv activation
    venv_prefix = "source ci_test_venv/bin/activate && "
    checks = [
        (1, "Install Package", f"{venv_prefix}pip install -q -e ."),
        (2, "Ruff Linting", f"{venv_prefix}ruff check src/ tests/"),
        (3, "Black Formatting Check", f"{venv_prefix}black --check src/ tests/"),
        (4, "MyPy Type Checking", f"{venv_prefix}mypy src/ --ignore-missing-imports"),
        (5, "Run Tests", f"{venv_prefix}pytest tests/ -v"),
        (6, "Coverage Check", f"{venv_prefix}pytest --cov=src --cov-report=term-missing tests/"),
        (7, "Build Package", f"{venv_prefix}pip install -q build && python -m build"),
    ]

    results = []
    wheel_file = None

    for step_num, name, command in checks:
        success = run_command(step_num, 7, name, command)
        results.append((name, success))
        if not success and step_num <= 1:  # Stop if install fails
            break

        # Capture wheel filename if build succeeded
        if step_num == 7 and success:
            wheel_result = subprocess.run(
                "ls -1 dist/*.whl 2>/dev/null | head -1", shell=True, capture_output=True, text=True
            )
            if wheel_result.returncode == 0:
                wheel_file = wheel_result.stdout.strip()

    # Cleanup
    print_step("Cleanup", "7", "Cleanup")
    print("Removing test environment\n")
    subprocess.run("rm -rf ci_test_venv", shell=True)
    print("✅ Cleanup complete")

    # Summary
    print_header("CI/CD PIPELINE SUMMARY")

    all_passed = True
    for name, success in results:
        if success:
            print(f"  ✅ {name:<30} PASS")
        else:
            print(f"  ❌ {name:<30} FAIL")
            all_passed = False

    print("\n" + "=" * 60)

    if all_passed:
        print("\n[SUCCESS] ALL CHECKS PASSED!")
        print("\n" + "=" * 60)
        print("  DEPLOYMENT SIMULATION")
        print("=" * 60)

        if wheel_file:
            print(f"\nPackage built successfully: {wheel_file}")

        print("\nIn a real production environment, this would trigger:")
        print("  1. Pull Request merged to 'main' branch")
        print("  2. Automated deployment to artifact repository")
        print("  3. SRE team deploys to production servers")
        print("\nYour package is ready for deployment!")
        print("\n" + "=" * 60 + "\n")
        return 0
    else:
        print("\n[FAILED] CHECKS FAILED! Fix the issues before deploying.")
        print("\nPipeline blocked - cannot merge to main branch.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())