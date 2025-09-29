# Heart Disease Prediction Using Model Evaluation & Cross-Validation

A comprehensive machine learning project for predicting heart disease using the UCI Heart Disease Dataset. This project implements binary classification using logistic regression and decision tree models, with extensive evaluation using multiple metrics and k-fold cross-validation.

## 📋 Project Overview

This project develops and evaluates binary classification models to predict heart disease using medical indicators such as:

- Age, sex, chest pain type
- Resting blood pressure, cholesterol levels
- Fasting blood sugar, resting ECG results
- Maximum heart rate achieved, exercise-induced angina
- ST depression, slope of peak exercise ST segment
- Number of major vessels, thalassemia type

## 🎯 Objectives

1. **Data Analysis**: Comprehensive exploratory data analysis of medical indicators
2. **Model Development**: Train and compare logistic regression and decision tree classifiers
3. **Robust Evaluation**: Apply multiple metrics (accuracy, precision, recall, F1-score, ROC-AUC)
4. **Cross-Validation**: Implement k-fold cross-validation for reliable performance assessment
5. **Clinical Interpretability**: Analyze feature importance and model coefficients for medical relevance

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

### Required Packages

```bash
pip install ucimlrepo pandas numpy scikit-learn matplotlib seaborn jupyter
```

### Quick Setup

```bash
# Clone or download the project files
cd heart_disease_prediction

# Install dependencies
pip install -r requirements.txt  # If you have a requirements file
# OR install individually:
pip install ucimlrepo pandas numpy scikit-learn matplotlib seaborn jupyter
```

## 🚀 Usage

### Option 1: Jupyter Notebook (Recommended)

```bash
jupyter notebook heart_disease_prediction.ipynb
```

### Option 2: Python Script Demo

```bash
python heart_disease_demo.py
```

## 📊 Dataset Information

- **Source**: UCI Heart Disease Dataset (ID: 45)
- **Samples**: 303 patient records
- **Features**: 13 medical indicators
- **Target**: Binary classification (0: No heart disease, 1: Heart disease present)
- **Balance**: ~54% no disease, ~46% disease

### Features Description

- `age`: Age in years
- `sex`: Gender (1 = male, 0 = female)
- `cp`: Chest pain type (1-4)
- `trestbps`: Resting blood pressure (mm Hg)
- `chol`: Serum cholesterol (mg/dl)
- `fbs`: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- `restecg`: Resting ECG results (0-2)
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise induced angina (1 = yes, 0 = no)
- `oldpeak`: ST depression induced by exercise
- `slope`: Slope of peak exercise ST segment (1-3)
- `ca`: Number of major vessels colored by fluoroscopy (0-3)
- `thal`: Thalassemia type (3 = normal, 6 = fixed defect, 7 = reversible defect)

## 🔍 Methodology

### 1. Exploratory Data Analysis

- Data structure examination
- Missing value analysis
- Statistical summaries and distributions
- Correlation analysis
- Target variable distribution

### 2. Data Preprocessing

- Missing value imputation
- Feature scaling (for logistic regression)
- Train-test split with stratification

### 3. Model Training

- **Logistic Regression**: Linear classifier with probabilistic output
- **Decision Tree**: Non-linear classifier with interpretable rules

### 4. Model Evaluation

- Multiple metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- Confusion matrices
- ROC curves
- Classification reports

### 5. Cross-Validation

- 5-fold and 10-fold cross-validation
- Performance consistency analysis
- Mean and standard deviation of metrics

## 📈 Results Summary

Based on the comprehensive evaluation:

### Logistic Regression Performance

- **Accuracy**: ~87% (Test), ~83% (10-fold CV)
- **Precision**: ~81% (Test), ~84% (10-fold CV)
- **Recall**: ~93% (Test), ~78% (10-fold CV)
- **F1-Score**: ~87% (Test), ~81% (10-fold CV)
- **ROC-AUC**: ~95% (Test), ~90% (10-fold CV)

### Decision Tree Performance

- **Accuracy**: ~79% (Test), ~75% (10-fold CV)
- **Precision**: ~71% (Test), ~72% (10-fold CV)
- **Recall**: ~89% (Test), ~74% (10-fold CV)
- **F1-Score**: ~79% (Test), ~72% (10-fold CV)
- **ROC-AUC**: ~81% (Test), ~75% (10-fold CV)

### Model Selection

**Recommended Model**: Logistic Regression

**Reasons**:

- Higher overall performance across all metrics
- Better clinical interpretability through coefficients
- More stable performance (lower variance)
- Excellent recall for disease detection
- Strong precision for minimizing false positives

## 🏥 Clinical Interpretability

### Logistic Regression Insights

- **Positive Coefficients**: Increase disease probability
- **Negative Coefficients**: Decrease disease probability
- **High-Impact Features**: Identified through coefficient magnitude
- **Probabilistic Output**: Provides confidence estimates

### Decision Tree Insights

- **Feature Importance**: Ranking of predictive features
- **Decision Rules**: Easy-to-follow if-then conditions
- **Non-linear Relationships**: Captures complex feature interactions
- **Visual Interpretation**: Tree structure shows decision paths

## 📝 Project Structure

```
heart_disease_prediction/
│
├── heart_disease_prediction.ipynb    # Main analysis notebook
├── heart_disease_demo.py            # Quick demo script
├── README.md                        # This file
└── requirements.txt                 # Dependencies (if created)
```

## 🔬 Key Features

### Comprehensive Analysis

- ✅ Complete EDA with visualizations
- ✅ Multiple model comparison
- ✅ Robust cross-validation
- ✅ Clinical interpretability focus
- ✅ Statistical significance testing

### Medical Context

- ✅ Healthcare-appropriate metrics (high recall priority)
- ✅ Feature importance for clinical decisions
- ✅ Interpretable model recommendations
- ✅ Ethical AI considerations

### Technical Excellence

- ✅ Proper data preprocessing
- ✅ Stratified sampling for class balance
- ✅ Multiple evaluation metrics
- ✅ Cross-validation for robustness
- ✅ Visualization of results

## ⚠️ Important Considerations

### Medical Disclaimer

- This model is for **educational and research purposes only**
- **Not intended for actual medical diagnosis**
- Always consult qualified medical professionals
- Consider patient-specific factors not in dataset
- Validate on diverse patient populations

### Technical Limitations

- Dataset size: 303 samples (relatively small)
- Temporal considerations: Data may not reflect current medical practices
- Feature limitations: Many relevant factors not included
- Generalizability: Performance may vary across populations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper documentation
4. Add tests if applicable
5. Submit a pull request

## 📜 License

This project is for educational purposes. Please respect the UCI dataset licensing terms and medical data ethics guidelines.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Heart Disease Dataset
- Creators of the original Cleveland Heart Disease Database
- Contributors to scikit-learn, pandas, and visualization libraries
- Medical professionals who contribute to open health data

## 📚 References

1. Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. University of California, Irvine, School of Information and Computer Sciences.
2. Cleveland Clinic Foundation Heart Disease Database
3. Scikit-learn: Machine Learning in Python documentation
4. Healthcare AI ethics and interpretability guidelines

---

**Contact**: For questions or suggestions about this project, please open an issue in the repository.

**Last Updated**: September 2025
