import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Remove Person ID
if "Person ID" in df.columns:
    df = df.drop("Person ID", axis=1)

# Encode ALL object columns
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

print(df.dtypes)

X = df.drop("Quality of Sleep", axis=1)
y = df["Quality of Sleep"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "sleep_quality_model.pkl")

print("SUCCESS")