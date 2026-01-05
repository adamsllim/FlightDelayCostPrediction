# Flight Delay Prediction

## Overview...
This project analyzes six years of U.S. commercial flight data (2018–2024) to model delay severity and cost‑per‑mile, providing insights into airline reliability, operational risk, and travel cost efficiency. The analysis incorporates 14 engineered features, supervised learning models, and extensive error evaluation to understand the factors that drive delays and cost variability across major airlines.

The goal of the project is to support airline reliability analysis and route risk profiling, helping travelers, analysts, and industry stakeholders identify high‑risk routes, delay‑prone carriers, and cost‑efficient travel patterns.

## Objectives..
- Predict flight delay severity using supervised classification models
- Estimate cost‑per‑mile using regression models
- Identify operational, temporal, and carrier‑specific factors that influence delays and cost efficiency
- Evaluate model performance using industry‑appropriate metrics
- Provide actionable insights for airline reliability and passenger decision‑making

## Methodology...
1. Data Cleaning & Preparation
- Removed canceled and diverted flights
- Forward‑filled missing values where appropriate
- One‑hot encoded categorical variables (airline, origin, destination)
- Engineered key features including:
- DelaySeverity (categorical)
- DelayBinary (on‑time vs delayed)
- CostPerMile (derived metric)
- Final cleaned dataset contained 14 core features supporting both classification and regression tasks

2. Exploratory Data Analysis (EDA)
- Analyzed delay distributions across airlines, seasons, and airports
- Identified high‑risk routes with above‑average delay frequency
- Examined relationships between distance, elapsed time, and cost‑per‑mile
- Visualized carrier‑specific reliability patterns

3. Modeling

**Delay Severity Prediction (Classification)**
- Models implemented:
- Support Vector Machine (SVM) with RBF kernel
- Multilayer Perceptron (MLP) classifier with dropout + early stopping

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1‑score
- Confusion matrices

Key notes:
- SVM handled class imbalance using class weights
- MLP used dropout layers to reduce overfitting

**Cost‑Per‑Mile Prediction (Regression)**
- Models implemented:
- MLPRegressor (scikit‑learn)
- Custom Keras MLP with dropout and Adam optimizer

Evaluation metrics:
- RMSE
- MAE
- R²
- Actual vs predicted scatter plots

4. Interpretation
- Ranked feature importance for both delay and cost models
- Identified operational drivers of delay severity (e.g., departure hour, distance, airline)
- Highlighted cost‑efficiency patterns across major carriers
- Summarized actionable insights for airline operations and traveler decision‑making

## Key Findings...
**Delay Prediction**
- SVM achieved ~85–92% accuracy across major airlines
- High recall (~86%) for delayed flights, meaning most delays were correctly identified
- Precision was lower, indicating some false positives
- MLP classifier underperformed (60% accuracy, low recall), struggling with class imbalance and linear patterns

Conclusion:  
- SVM outperformed MLP due to the dataset’s structure and linear separability.

**Cost‑Per‑Mile Prediction**
- MLP regression achieved strong performance with R² ≈ 0.87–0.89
- United Airlines showed the best predictive accuracy (RMSE ≈ 0.0178, R² ≈ 0.8912)
- Southwest had the highest error, likely due to greater variability in its dataset
- Scatter plots showed tight clustering around the ideal line for UA and DL

Conclusion:  
- MLP regression reliably predicts cost‑per‑mile, with performance varying by airline.

## Error Analysis...
- MLP classifier struggled due to class imbalance and limited data for severe delays
- SVM performed well because delay patterns were more linearly separable
- Cost‑per‑mile predictions were affected by:
  - Missing or approximated fields
  - Noise introduced by the proxy cost formula
- Overfitting in early MLP regressors was mitigated using dropout and early stopping

## Future Work
- Hyperparameter tuning (GridSearchCV, Bayesian optimization)
- Improved cost‑per‑mile formula and more robust imputation methods
- Addressing class imbalance using SMOTE or advanced sampling
- Building a web application for non‑technical users to explore predictions
- Expanding feature engineering (weather, airport congestion, seasonal trends)
