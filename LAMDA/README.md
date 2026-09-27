---
license: mit
size_categories:
- 1M<n<10M
tags:
- android
- malware
- cybersecurity
- concept-drift
- longitudinal
- security
- classification
- benchmark
configs:
  - config_name: Baseline
    data_files:
      - split: train
        path: Baseline/*/*_train.parquet
      - split: test
        path: Baseline/*/*_test.parquet

  # - config_name: var_thresh_0.0001
  #   data_files:
  #     - split: train
  #       path: var_thresh_0.0001/*/*_train.parquet
  
  #     - split: test
  #       path: var_thresh_0.0001/*/*_test.parquet
  - config_name: var_thresh_0.01
    data_files:
      - split: train
        path: var_thresh_0.01/*/*_train.parquet
      - split: test
        path: var_thresh_0.01/*/*_test.parquet

language:
- en
pretty_name: LAMDA
---

# LAMDA: A Longitudinal Android Malware Dataset for Drift Analysis

This dataset contains a longitudinal benchmark for Android malware detection designed to analyze and evaluate concept drift in machine learning models. It includes labeled and feature-engineered Android APK data from 2013 to 2025 (excluding 2015), with over 1 million samples collected from real-world sources.

## Dataset Details

### Dataset Description

- **Curated by:** IQSeC Lab, The University of Texas at El Paso
- **Shared by:** IQSeC Lab
- **Language(s):** Not applicable
- **License:** MIT

LAMDA is the largest and most temporally diverse Android malware dataset to date. It enables studies in concept drift, temporal generalization, family classification, and robust malware detection over time. Each sample includes static features (from `.data` files), metadata (VirusTotal detections, family name, timestamp), and binary labels.

The dataset was created using ~1M APKs from [AndroZoo](https://androzoo.uni.lu/), with additional metadata and labels derived via VirusTotal and AVClass2. Labels are assigned using a 4+ AV detection threshold to reduce noise.

### Dataset Sources

- **Repository:** https://huggingface.co/datasets/IQSeC-Lab/LAMDA
- **Project Website:** https://iqsec-lab.github.io/LAMDA/
- **Paper:** https://arxiv.org/abs/2505.18551

## Uses

### Direct Use

- Malware classification
- Family prediction
- Concept drift analysis
- Temporal generalization benchmarks
- SHAP-based feature attribution drift analysis
- Continual learning evaluation (e.g., class-IL, replay)

### Out-of-Scope Use

- Dynamic behavior analysis (no runtime traces)
- On-device malware detection (model integration not provided)

## Dataset Structure

Each year is stored in a subdirectory:

```
2013/
├── 2013_train.parquet
├── 2013_test.parquet
...
2025/
├── 2025_train.parquet
├── 2025_test.parquet
```


Each `.parquet` contains:

| Column        | Description                                         |
|---------------|-----------------------------------------------------|
| `label`       | 0 = benign, 1 = malware                             |
| `family`      | Malware family name (via AVClass2)                  |
| `vt_count`    | VirusTotal vendor detection count                   |
| `year_month`  | Timestamp in YYYY-MM format                         |
| `feat_0 ... feat_4560` | Static bag-of-words features (int8)        |
| `hash`        | Sample SHA256 hash (used as index)                  |

A `feature_mapping.csv` maps each `feat_i` to its original static token.

## Dataset Creation

### Curation Rationale

To enable longitudinal and realistic evaluation of ML-based malware detection systems that must remain effective in the face of temporal and adversarial drift.

### Source Data

APK samples were downloaded from AndroZoo and processed using static analysis to extract `.data` files. Metadata was merged from a curated CSV containing VirusTotal counts and family assignments via AVClass2.

#### Data Collection and Processing

- Extracted feature vectors from `.data` files (comma-separated tokens)
- Labeled malware if `vt_detection ≥ 4`
- Assigned families via AVClass2
- Feature vectors vectorized using bag-of-words (sparse)
- Feature selection via `VarianceThreshold=0.001` → 4,561 features
- Train/test split (80/20) stratified by label, year-wise

#### Who are the source data producers?

Original APKs are from AndroZoo. Annotations and processing were conducted by IQSeC Lab at the University of Texas at El Paso.

### Annotations

#### Annotation Process

- Malware/benign labels based on AV vendor threshold (≥4)
- Family labels from AVClass2
- All annotations generated using automated pipelines

#### Who are the annotators?

Researchers at IQSeC Lab via static tooling and AVClass2

#### Personal and Sensitive Information

No PII or private user data is included. APKs are anonymized binaries.

## Bias, Risks, and Limitations

- Biased toward highly detected malware (AV-centric labeling)
- No dynamic/runtime behavior
- Concept drift is dataset-driven, not simulation-based

### Recommendations

- Normalize class balance before training
- Use continual or time-aware validation schemes
- SHAP explanations should be anchored year-wise

## Citation

**BibTeX:**
```bibtex
@inproceedings{haque2026lamda,
  title     = {LAMDA: A Longitudinal Android Malware Benchmark for Concept Drift Analysis},
  author    = {Haque, Md Ahsanul and
               Hossain, Ismail and
               Kamol, Md Mahmuduzzaman and
               Alam, Md Jahangir and
               Amalapuram, Suresh Kumar and
               Talukder, Sajedul and
               Rahman, Mohammad Saidur},
  booktitle = {The 14th International Conference on Learning Representations (ICLR)},
  year      = {2026},
  url       = {https://openreview.net/forum?id=1FnCrZtBNQ}
}