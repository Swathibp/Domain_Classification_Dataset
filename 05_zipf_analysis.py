# Get all tokens
all_tokens = df['Questions'].str.lower().str.split().sum()
token_freq = Counter(all_tokens)

# Sort by frequency
freq_sorted = sorted(token_freq.values(), reverse=True)

# Plot Zipf curve
plt.figure()
plt.plot(freq_sorted)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Token Rank (log scale)")
plt.ylabel("Frequency (log scale)")
plt.title("")
plt.show()
