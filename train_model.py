import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

# 1. Create Synthetic Training Data
print("Generating training data...")
n_rows = 10000

data = {
    'amount': np.random.uniform(10, 5000, n_rows),
    'tx_count_1m': np.random.randint(1, 10, n_rows),
    'is_weekend': np.random.randint(0, 2, n_rows),
    'is_night': np.random.randint(0, 2, n_rows),
}

df = pd.DataFrame(data)

# 2. Create a "Fraud Label" 
# (Fraud = high amount AND high frequency, or very high amount)
df['is_fraud'] = ((df['amount'] > 4000) & (df['tx_count_1m'] > 5)) | (df['amount'] > 4800)
df['is_fraud'] = df['is_fraud'].astype(int)

# 3. Train the Model
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = XGBClassifier(n_estimators=100, max_depth=5)
print("Training XGBoost model...")
model.fit(X_train, y_train)

# 4. Save the Model and the Data
with open('fraud_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'fraud_model.pkl'")
print("\nModel Performance Report:")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))