import pandas as pd

# ==============================
# STEP 1: Load cleaned data
# ==============================
df = pd.read_csv("cleaned_food_delivery_data.csv")

# ==============================
# STEP 2: Feature Engineering
# ==============================

# 1. Order Day Type
df['Order_Day_Type'] = df['Order_Day']

# 2. Peak Hour Indicator
df['Peak_Hour_Indicator'] = df['Peak_Hour'].apply(lambda x: 1 if x == True else 0)

# 3. Profit Margin Percentage
df['Profit_Margin_Percentage'] = df['Profit_Margin'] * 100

# 4. Delivery Performance Category
def delivery_performance(time):
    if time <= 45:
        return 'Fast'
    elif time <= 90:
        return 'On-Time'
    else:
        return 'Delayed'

df['Delivery_Performance'] = df['Delivery_Time_Min'].apply(delivery_performance)

# 5. Customer Age Group
def age_group(age):
    if age < 25:
        return 'Youth'
    elif age < 40:
        return 'Adult'
    elif age < 60:
        return 'Middle-Aged'
    else:
        return 'Senior'

df['Customer_Age_Group'] = df['Customer_Age'].apply(age_group)

# ==============================
# STEP 3: Save engineered data
# ==============================
df.to_csv("feature_engineered_food_delivery_data.csv", index=False)

print("Feature engineering completed successfully!")
print(df[['Order_Day_Type',
          'Peak_Hour_Indicator',
          'Profit_Margin_Percentage',
          'Delivery_Performance',
          'Customer_Age_Group']].head())
