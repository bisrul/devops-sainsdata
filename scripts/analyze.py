import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/sales_clean.csv")

# Revenue by category
summary = df.groupby("category")["revenue"].sum().sort_values()

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
summary.plot(kind="barh", ax=ax, color="steelblue")
ax.set_title("Total Revenue by Category")
ax.set_xlabel("Revenue ($)")
plt.tight_layout()
plt.savefig("reports/revenue_by_category.png")
print("✅ Report saved to reports/revenue_by_category.png")