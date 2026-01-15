# 🧪 1-Hour Data Analysis Quiz

Welcome! In this quiz, you’ll review:
- Forking a GitHub repository
- Using a provided Python function
- Performing a simple data transformation
- Creating a basic plot
- Committing your work back to GitHub

You have **60 minutes** to complete all tasks. Good luck!

---

## 📁 Repository Files (Available together with this README)

- `sales.csv` — A small dataset of product sales
- `helpers.py` — Contains add_revenue function to help with your analysis

> ❗ Do **not** modify these files. Create new files for your work.

---

## 📋 Your Tasks

1. **Fork this repository** to your GitHub account.
2. **Clone your fork** to your local machine.
3. **Create a new Python script** called `run_analysis.py` that does the following:
   - Loads `sales.csv` using `pandas`
   - Columns: `product`,`units`,`price`
   - **Task**: Add a `total_revenue` column (`units * price`).
   - Imports and uses the `add_revenue()` function from `helpers.py`
   - Saves the updated data as `sales_with_revenue.csv`
   - Creates a simple bar plot of `product` vs `revenue` and saves it as `revenue_plot.png`
4. **Run your script** to generate the output files.
5. **Deliverables** (Must Be in Your Fork by Deadline):
   - Python script: `run_analysis.py`
   - Updated CSV: `sales_with_revenue.csv` with `total_revenue` column
   - Plot image: `revenue_plot.png`

---

## 💡 Starter Code (Put this in `run_analysis.py`)

```python
# You can modify this file if you want
import pandas as pd
import matplotlib.pyplot as plt
from helpers import add_revenue

# Load data
df = pd.read_csv('sales.csv')

# Add revenue column using the provided function
df = add_revenue(df)

# Save updated CSV
df.to_csv('sales_with_revenue.csv', index=False)

# Create and save a simple bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['revenue'])
plt.title('Revenue by Product')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_plot.png')

print("✅ Done! Check for sales_with_revenue.csv and revenue_plot.png")
