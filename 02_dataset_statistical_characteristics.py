
import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

file_path = ""

df = pd.read_excel(file_path)

# Remove records with missing questions or domain labels
df = df.dropna(subset=['Questions', 'Domain']).copy()

# --------------------------------------------------
# 2. Basic Dataset Statistics
# --------------------------------------------------

total_queries = len(df)
number_of_domains = df['Domain'].nunique()

# --------------------------------------------------
# 3. Query Length Statistics
# --------------------------------------------------

df['Questions'] = df['Questions'].astype(str)

df['Token_Count'] = df['Questions'].apply(
    lambda x: len(x.split())
)

avg_length = df['Token_Count'].mean()
min_length = df['Token_Count'].min()
max_length = df['Token_Count'].max()

# --------------------------------------------------
# 4. Vocabulary Size and Lexical Diversity
# --------------------------------------------------

all_tokens = df['Questions'].str.lower().str.split().sum()

unique_tokens = set(all_tokens)

vocab_size = len(unique_tokens)

lexical_diversity = (
    vocab_size / len(all_tokens) if all_tokens else 0
)

# --------------------------------------------------
# 5. Gini Coefficient
# --------------------------------------------------

def calculate_gini(array):

    array = np.array(array, dtype=float)
    array = np.sort(array)

    n = len(array)

    if np.sum(array) == 0:
        return 0.0

    index = np.arange(1, n + 1)

    return np.sum(
        (2 * index - n - 1) * array
    ) / (n * np.sum(array))


domain_counts = df['Domain'].value_counts()

gini_coefficient = calculate_gini(domain_counts.values)

# --------------------------------------------------
# 6. Shannon Entropy
# --------------------------------------------------

proportions = domain_counts / domain_counts.sum()

shannon_entropy = -np.sum(
    proportions * np.log2(proportions)
)

# --------------------------------------------------
# 7. Display All Statistical Characteristics
# --------------------------------------------------

statistics = {
    "Total Queries": total_queries,
    "Number of Domains": number_of_domains,
    "Average Query Length (tokens)": round(avg_length, 2),
    "Minimum Query Length (tokens)": min_length,
    "Maximum Query Length (tokens)": max_length,
    "Vocabulary Size": vocab_size,
    "Lexical Diversity": round(lexical_diversity, 4),
    "Gini Coefficient": round(gini_coefficient, 4),
    "Shannon Entropy": round(shannon_entropy, 4)
}

print("\nTABLE 4: STATISTICAL CHARACTERISTICS OF THE DATASET")
print("-" * 55)
print(f"{'Metric':<38} {'Value':>12}")
print("-" * 55)

for metric, value in statistics.items():
    print(f"{metric:<38} {value:>12}")

print("-" * 55)
