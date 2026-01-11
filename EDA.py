import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# Load CLEANED data
# ==============================
df = pd.read_csv("cleaned_food_delivery_data.csv")

print(df.head())
print(df.info())

# ==============================
# 1. Delivery Time Distribution
# ==============================
plt.figure()
sns.histplot(df['Delivery_Time_Min'], kde=True)
plt.title("Distribution of Delivery Time (Minutes)")
plt.show()

# ==============================
# 2. Order Value Distribution
# ==============================
plt.figure()
sns.histplot(df['Order_Value'], kde=True)
plt.title("Distribution of Order Value")
plt.show()

# ==============================
# 3. City-wise Order Analysis
# ==============================
plt.figure(figsize=(8,5))
df['City'].value_counts().plot(kind='bar')
plt.title("City-wise Order Count")
plt.xlabel("City")
plt.ylabel("Number of Orders")
plt.show()

# ==============================
# 4. Cuisine-wise Order Analysis
# ==============================
plt.figure(figsize=(8,5))
df['Cuisine_Type'].value_counts().plot(kind='bar')
plt.title("Cuisine-wise Order Count")
plt.xlabel("Cuisine")
plt.ylabel("Number of Orders")
plt.show()

# ==============================
# 5. Weekend vs Weekday Demand
# ==============================
plt.figure()
df['Order_Day'].value_counts().plot(kind='bar')
plt.title("Weekend vs Weekday Orders")
plt.xlabel("Order Day")
plt.ylabel("Order Count")
plt.show()

# ==============================
# 6. Distance vs Delivery Time
# ==============================
plt.figure()
sns.scatterplot(
    x=df['Distance_km'],
    y=df['Delivery_Time_Min']
)
plt.title("Distance vs Delivery Time")
plt.xlabel("Distance (km)")
plt.ylabel("Delivery Time (minutes)")
plt.show()

# ==============================
# 7. Cancellation Reasons
# ==============================
plt.figure(figsize=(8,5))
df['Cancellation_Reason'].value_counts().plot(kind='bar')
plt.title("Cancellation Reasons Analysis")
plt.xlabel("Reason")
plt.ylabel("Count")
plt.show()

# ==============================
# 8. Correlation Analysis
# ==============================
plt.figure(figsize=(10,6))
sns.heatmap(
    df.select_dtypes(include=['int64', 'float64']).corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.show()

print("EDA completed successfully!")
