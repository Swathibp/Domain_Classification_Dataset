
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Load the dataset
# --------------------------------------------------

file_path = ""

df = pd.read_excel(file_path)

# Display dataset column names
print("Columns in dataset:", df.columns.tolist())

# --------------------------------------------------
# 2. Calculate domain-wise query counts
# --------------------------------------------------

domain_counts = df['Domain'].value_counts().sort_values()

print("\nDomain-wise Query Counts:")
print(domain_counts)

# Display total number of queries and domains
print("\nTotal number of queries:", len(df))
print("Total number of domains:", df['Domain'].nunique())

# --------------------------------------------------
# 3. Plot domain-wise distribution
# --------------------------------------------------

plt.figure(figsize=(10, 8))

plt.barh(
    domain_counts.index,
    domain_counts.values
)

plt.xlabel("Number of Queries", fontsize=12)
plt.ylabel("Domain", fontsize=12)
plt.title("Domain-wise Distribution of Queries", fontsize=14)

plt.tight_layout()

# Display graph
plt.show()
