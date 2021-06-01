# Credit Card lead prediction

This hackathone was organized by [Analytics Vidhya](https://datahack.analyticsvidhya.com/contest/job-a-thon-2/?utm_source=datahack&utm_medium=Navbar&utm_campaign=Jobathon).

# 1. Problem statement:

Given the record of the Person you have to predict if he/she want to get a credit card or not.

# 2. Dataset:

Analytics Vidhya provided train and test dataset. You can download it from [here](https://www.kaggle.com/nextbigwhat/analytics-vidhya-job-a-thon-may-2021)

# 3. Model Training:

I achived accuracy of 74% using [roc_acc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html) metric.

**Parameters:**

    1. Algorithm: Random Forest classifier
    2. n_estimators : 100
    3. max_features : auto
    4. Criterion : gini
    5. Feature scaling algorithm : Standard Scaler
