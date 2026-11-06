# Step 1: Clean Domain column (remove ' related query')
df['Domain_clean'] = df['Domain'].str.replace(" related query", "", regex=False)

# Step 2: Define descriptive mapping
domain_descriptions = {
    "Hostel": "questions about hostel facilities and accommodation",
    "Admission": "questions about admission process and eligibility",
    "Placement": "questions about campus placement opportunities",
    "Library": "questions about library services and resources",
    "Sports": "questions about sports activities and facilities",
    "Research": "questions about research programs and activities",
    "Grade": "questions about grading and academic performance",
    "Faculty": "questions about faculty members and teaching staff",
    "Internship": "questions about internship opportunities",
    "Transportation": "questions about campus transportation services",
    "Infrastructure": "questions about campus infrastructure and facilities",
    "Counselling": "questions about student counselling services",
    "Teaching": "questions about teaching methods and classes",
    "College": "questions about general college information",
    "Canteen/Mess": "questions about canteen and mess facilities",
    "Higher-Studies": "questions about higher studies and postgraduate options",
    "Semester abroad": "questions about semester abroad programs",
    "Student clubs": "questions about student clubs and extracurricular activities",
    "Start ups": "questions about startup and entrepreneurship support",
    "Curricullum": "questions about curriculum and course structure",
    "About Place": "questions about campus location and surroundings",
    "Multidisciplinary": "questions involving multiple institutional services"
}

# Step 3: Replace with descriptive text
df['Domain_descriptive'] = df['Domain_clean'].map(domain_descriptions)

# ✅ Step 3.1: Save updated dataframe
df.to_excel("/content/drive/MyDrive/Dataset/Domain_classes_with_descriptive_labels.xlsx", index=False)

print("File saved as: Domain_classes_with_descriptive_labels.xlsx")

# Step 4: Create candidate label list
candidate_labels = sorted(df['Domain_descriptive'].dropna().unique())

print("\nZero-shot Candidate Labels:\n")
for label in candidate_labels:
    print("-", label)
