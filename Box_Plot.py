import matplotlib.pyplot as plt

plt.figure()
plt.boxplot(df['Token_Count'], vert=False)

plt.xlabel("Query Length (tokens)")
plt.title("")

plt.tight_layout()
plt.show()
