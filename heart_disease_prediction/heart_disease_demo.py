#!/usr/bin/env python3
"""
Heart Disease Prediction - Quick Demo Script
This script demonstrates the core functionality of the heart disease prediction system.
"""

# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo


def load_heart_disease_data():
    """Load and preprocess the UCI Heart Disease dataset"""
    print("Loading UCI Heart Disease Dataset...")

    # Fetch dataset
    heart_disease = fetch_ucirepo(id=45)
    X = heart_disease.data.features
    y = heart_disease.data.targets

    # Handle missing values
    print(f"Missing values before preprocessing: {X.isnull().sum().sum()}")

    # For numerical columns, use median
    numerical_cols = X.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        if X[col].isnull().any():
            X[col].fillna(X[col].median(), inplace=True)

    # For categorical columns, use mode
    categorical_cols = X.select_dtypes(exclude=[np.number]).columns
    for col in categorical_cols:
        if X[col].isnull().any():
            X[col].fillna(X[col].mode()[0], inplace=True)

    print(f"Missing values after preprocessing: {X.isnull().sum().sum()}")

    # Convert target to binary (0: no disease, 1: disease)
    y_binary = (y.iloc[:, 0] > 0).astype(int)

    print(f"Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Target distribution: {y_binary.value_counts().to_dict()}")

    return X, y_binary


def train_and_evaluate_models(X, y):
    """Train and evaluate both logistic regression and decision tree models"""

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features for logistic regression
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Initialize models
    models = {
        "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42, max_depth=10),
    }

    results = {}

    for name, model in models.items():
        print(f"\nTraining {name}...")

        # Choose appropriate data (scaled for LR, original for DT)
        if name == "Logistic Regression":
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
            y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        else:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)[:, 1]

        # Calculate metrics
        metrics = {
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1-Score": f1_score(y_test, y_pred),
            "ROC-AUC": roc_auc_score(y_test, y_pred_proba),
        }

        results[name] = metrics

        print(f"{name} Results:")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")

    return results


def perform_cross_validation(X, y):
    """Perform 5-fold cross-validation for both models"""

    print("\nPerforming 5-Fold Cross-Validation...")

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Initialize models
    lr_model = LogisticRegression(random_state=42, max_iter=1000)
    dt_model = DecisionTreeClassifier(random_state=42, max_depth=10)

    # Perform cross-validation
    scoring_metrics = ["accuracy", "precision", "recall", "f1", "roc_auc"]

    cv_results = {}

    for model_name, model, data in [
        ("Logistic Regression", lr_model, X_scaled),
        ("Decision Tree", dt_model, X),
    ]:
        cv_results[model_name] = {}
        print(f"\n{model_name} Cross-Validation:")

        for metric in scoring_metrics:
            scores = cross_val_score(model, data, y, cv=5, scoring=metric)
            cv_results[model_name][metric] = {
                "mean": scores.mean(),
                "std": scores.std(),
            }
            print(f"  {metric.upper()}: {scores.mean():.4f} ± {scores.std():.4f}")

    return cv_results


def main():
    """Main function to run the heart disease prediction demo"""

    print("=" * 60)
    print("HEART DISEASE PREDICTION - DEMO")
    print("=" * 60)

    try:
        # Load data
        X, y = load_heart_disease_data()

        # Train and evaluate models
        results = train_and_evaluate_models(X, y)

        # Perform cross-validation
        cv_results = perform_cross_validation(X, y)

        # Display summary
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)

        # Find best model based on F1-score
        best_model = max(results.keys(), key=lambda x: results[x]["F1-Score"])

        print(f"Best performing model: {best_model}")
        print(f"Best F1-Score: {results[best_model]['F1-Score']:.4f}")

        print("\nModel Comparison:")
        for model_name in results.keys():
            print(f"{model_name}:")
            print(f"  Accuracy: {results[model_name]['Accuracy']:.4f}")
            print(f"  F1-Score: {results[model_name]['F1-Score']:.4f}")
            print(f"  ROC-AUC: {results[model_name]['ROC-AUC']:.4f}")

        print(f"\n✅ Demo completed successfully!")
        print(f"For detailed analysis, please run the Jupyter notebook.")

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
