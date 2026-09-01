"""
Generate sample loan applications CSV for testing.
This script creates realistic loan application data for the batch processor.
"""

import csv
import random

# Set seed for reproducibility
random.seed(42)

# Generate 1000 sample applications
applications = []

for i in range(1, 1001):
    app = {
        "id": f"APP-{i:03d}",
        "amount": random.choice([5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]),
        "income": random.choice([25000, 30000, 35000, 40000, 45000, 50000, 60000, 70000, 80000]),
        "credit_score": random.choice([580, 620, 650, 680, 700, 720, 750, 780, 800, 820]),
        "years": random.choice([3, 5, 7, 10]),
    }
    applications.append(app)

# Write to CSV
output_file = "data/sample_applications.csv"
with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "amount", "income", "credit_score", "years"])
    writer.writeheader()
    writer.writerows(applications)

print(f"✅ Created {len(applications)} sample applications in {output_file}")
print("\nSample of data:")
for app in applications[:3]:
    print(f"  {app}")