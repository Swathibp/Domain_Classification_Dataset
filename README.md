# Institutional Query Dataset for Domain Classification

## 📌 Overview

This repository provides a domain-specific institutional query dataset designed for fine-grained intent classification in educational environments. The dataset consists of **5,210 user queries** annotated across **22 institutional service domains**, such as admission, hostel, placement, library, and transportation.

The dataset is intended to support research in **natural language processing (NLP)**, **intent detection**, and **conversational AI systems**, particularly for educational and campus-based applications.

## 📌 Dataset Version

- **Dataset Name:** Institutional Query Dataset for Domain Classification
- **Version:** 1.0
- **Total Queries:** 5,210
- **Number of Domains:** 22
- **Format:** CSV

This release provides the annotated institutional query dataset used in the associated research study.

---

## 📊 Dataset Statistics

| Metric | Value |
|---|---:|
| Total Queries | 5,210 |
| Number of Domains | 22 |
| Average Query Length (tokens) | 14.14 |
| Minimum Query Length (tokens) | 2 |
| Maximum Query Length (tokens) | 87 |
| Vocabulary Size | 5,297 |
| Lexical Diversity | 0.0719 |
| Gini Coefficient | 0.1208 |
| Shannon Entropy | 4.4056 |

---

## 🧠 Annotation Methodology

The dataset was constructed using:

- **Intent-first annotation strategy**
- **Dominant service labeling**
- Iterative refinement for semantic consistency
- Manual verification to ensure domain clarity

Each query is assigned a single dominant domain label representing the primary institutional intent.

---

## 📁 Dataset Format

The dataset is provided in CSV format with the following columns:

| Column Name | Description |
|---|---|
| Questions | User query text |
| Domain | Assigned domain label |

---

## 🏷️ Domain Label Mapping

Each query is assigned one of 22 domain labels based on its primary institutional intent. The domain labels and their corresponding descriptions are provided below to ensure consistent interpretation and facilitate reuse of the dataset.

| Domain Label | Description |
|---|---|
| Admission | Admission procedures, eligibility, applications and enrolment. |
| Placement | Campus recruitment, placement statistics and career opportunities. |
| Internship | Internship opportunities, eligibility and application processes. |
| Higher-Studies | Postgraduate education, research pathways and international study opportunities. |
| Research | Research projects, supervision, funding and innovation activities. |
| Teaching | Teaching quality, instructional methods and classroom engagement. |
| Curriculum | Course structure, subjects, academic content and programme design. |
| Grade | Grading systems, evaluation methods and academic performance. |
| Faculty | Faculty members, mentorship, expertise and academic guidance. |
| Library | Library resources, borrowing, operating hours and study facilities. |
| Hostel | Accommodation, room allocation, facilities and hostel regulations. |
| Canteen/Mess | Food services, meal plans, pricing and dining facilities. |
| Infrastructure | Campus buildings, laboratories, classrooms and utilities. |
| Transportation | Campus transport, connectivity and commuting options. |
| Sports | Sports facilities, fitness centres and athletic activities. |
| Student clubs | Club membership, activities and participation opportunities. |
| Counselling | Academic advising, career guidance and student counselling. |
| Semester abroad | Exchange programmes and international mobility opportunities. |
| Start ups | Entrepreneurship, incubation, funding and startup initiatives. |
| Multidisciplinary | Interdisciplinary learning and cross-department collaborations. |
| College | General institutional information, governance and policies. |
| About Place | Campus location, surrounding environment, climate and accessibility. |

---

## 🎯 Use Cases

This dataset can be used for:

- Fine-grained **intent classification**
- **Zero-shot and few-shot evaluation**
- **Domain-aware question answering systems**
- **Conversational chatbot development**
- **Knowledge graph-based query routing**

---

## 🤖 Applications

The dataset enables:

- Intent detection in multi-domain environments.
- Routing of queries to domain-specific knowledge graphs.
- Development of institutional chatbots and question-answering systems.

---

## 📂 Repository Structure

```text
Domain_Classification_Dataset/
│
├README.md
|LICENSE
|Domain_Classification.xlsx
│
├
│ 01_domain_distribution_analysis.py
│ 02_dataset_statistical_characteristics.py
│ 03_query_length_boxplot.py
│ 04_jaccard_similarity_heatmap.py
│ 05_zipf_analysis.py
│ 06_pca_visualization.py
│ 07_zero_shot_classification.py
│

## ⚙️ Reproducibility and Evaluation Scripts

The `scripts/` directory contains Python implementations for reproducing the dataset statistics, distribution analysis, visualizations, and classification experiments reported in the associated research study.

The scripts cover:

1. Domain-wise query distribution analysis.
2. Dataset statistical characteristics.
3. Query length distribution using box plots.
4. Pairwise domain similarity using Jaccard similarity.
5. Token frequency distribution using Zipf's law.
6. PCA visualization of query embeddings.
7. Zero-shot domain classification and evaluation.

### Requirements

Python 3.x and the following libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn transformers sentence-transformers openpyxl
```

### Execution

Navigate to the repository  and execute the required script:

```bash
python scripts/01_domain_distribution_analysis.py
```

Update the dataset file path in each script according to its location in your environment.

The zero-shot classification script uses the `facebook/bart-large-mnli` model for domain classification. Refer to the individual scripts for their respective configurations and evaluation procedures.

---

## 📜 License and Data Reuse

The dataset is made available for research and academic reference. For permissions regarding reuse, modification, or redistribution, please contact the corresponding author.

---

## 📖 Citation

If you use this dataset in your research, please cite the associated publication:

[INSERT COMPLETE PUBLICATION CITATION AND DOI, WHEN AVAILABLE]
