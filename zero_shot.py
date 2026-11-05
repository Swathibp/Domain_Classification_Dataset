from sklearn.metrics import classification_report, accuracy_score

# Sample size
sample_size = 5210

# Use descriptive labels as ground truth
sample_questions = df['Questions'][:sample_size].tolist()
sample_true = df['Domain_descriptive'][:sample_size].tolist()

# Candidate labels must also be descriptive
candidate_labels = sorted(df['Domain_descriptive'].dropna().unique())

# Run zero-shot classification (batch mode — important)
results = classifier(sample_questions, candidate_labels)

# Extract predictions
predictions = [res["labels"][0] for res in results]

# Sanity check
print("True labels:", len(sample_true))
print("Predictions:", len(predictions))

# Accuracy
print("Zero-shot Accuracy:",
      round(accuracy_score(sample_true, predictions), 4))

# Full classification report
print(classification_report(sample_true, predictions))
