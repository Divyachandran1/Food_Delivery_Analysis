import pandas as pd
from sklearn.preprocessing import StandardScaler

# ==============================
# STEP 1: Load the dataset
# ==============================
df = pd.read_csv("Online_Food_Delivery_Analysis.csv")

print("Initial Data Preview:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# ==============================
# STEP 2: Data Understanding
# ==============================
print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# ==============================
# STEP 3: Data Cleaning
# ==============================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing numeric values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Drop rows still containing missing values (categorical)
df.dropna(inplace=True)

print("\nAfter Cleaning:")
print(df.isnull().sum())

# ==============================
# STEP 4: Save CLEANED data (for EDA)
# ==============================
# IMPORTANT: This dataset is used ONLY for Exploratory Data Analysis
df.to_csv("cleaned_food_delivery_data.csv", index=False)
print("Cleaned data saved as cleaned_food_delivery_data.csv")

# ==============================
# STEP 5: Data Preprocessing (for modeling)
# ==============================

# Encode categorical variables
df_encoded = pd.get_dummies(df, drop_first=True)

# Feature Scaling (numerical columns only)
scaler = StandardScaler()
num_cols = df_encoded.select_dtypes(include=['int64', 'float64']).columns
df_encoded[num_cols] = scaler.fit_transform(df_encoded[num_cols])

# ==============================
# STEP 6: Save PREPROCESSED data (for modeling)
# ==============================
df_encoded.to_csv("preprocessed_food_delivery_data.csv", index=False)
print("Preprocessed data saved as preprocessed_food_delivery_data.csv")

print("\nData Cleaning and Preprocessing completed successfully!")
