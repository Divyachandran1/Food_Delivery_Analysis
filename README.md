# 🍔 Online Food Delivery Analysis – Data-Driven Business Insights

## 📌 Project Overview
Online food delivery platforms generate large volumes of transactional and operational data.  
This project focuses on analyzing real-world online food delivery data to uncover insights related to customer behavior, delivery efficiency, restaurant performance, revenue, profit, and cancellations.

The project involves **data cleaning, exploratory data analysis (EDA), feature engineering, SQL integration, and interactive dashboard development using Power BI (or Streamlit)** to support business decision-making.

---

## 🎯 Objectives
- Understand customer ordering behavior
- Analyze delivery performance and operational inefficiencies
- Evaluate restaurant performance
- Track key business KPIs such as revenue, profit, and cancellations
- Build interactive dashboards for business stakeholders

---

## 🧠 Skills & Tools Used

### 🔹 Programming & Analytics
- Python (Pandas, NumPy)
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Cleaning & Preprocessing

### 🔹 Databases
- MySQL
- SQLAlchemy

### 🔹 Visualization & BI
- Power BI (Primary)
- Streamlit (Optional)

### 🔹 Concepts
- KPI Design
- Business Analytics
- Data Storytelling
- Real-world Noisy Data Handling

---

## 🏢 Domain
- E-Commerce
- Food & Beverage Industry
- Logistics & Supply Chain
- Customer Analytics
- Business Intelligence

---

## 📊 Dataset Information
- **Dataset Size:** 100,000 online food delivery orders  
- **Features:** 25 columns including:
  - Customer details
  - Order information
  - Restaurant attributes
  - Delivery performance
  - Financial metrics

📁 Dataset link:  
[Online Food Delivery Dataset](https://drive.google.com/file/d/1ln_YbLXHZjah8c-zgrT_zacnfSwTB9ZE/view)

---

## 🔍 Project Approach

### 1️⃣ Data Understanding
- Reviewed dataset structure and data types
- Identified missing values and inconsistencies

### 2️⃣ Data Cleaning & Preprocessing
- Handled missing values (mean / median / mode)
- Removed or capped outliers (delivery time, order value)
- Corrected invalid values (ratings > 5, negative profit)
- Standardized categorical variables
- Ensured logical consistency across fields

### 3️⃣ Exploratory Data Analysis (EDA)
- Order value and delivery time distribution
- City-wise and cuisine-wise demand
- Weekend vs weekday order trends
- Distance vs delivery delay analysis
- Cancellation reason analysis
- Correlation analysis of numerical features

### 4️⃣ Feature Engineering
- Weekday vs Weekend classification
- Peak hour indicator
- Profit margin percentage
- Delivery performance categories
- Customer age groups

### 5️⃣ Data Storage (SQL)
- Cleaned data stored in MySQL
- Structured table design with appropriate data types
- Enables scalable querying and reporting

---

## 📈 Key Analytics Performed

### 🧑 Customer & Order Analysis
- Top spending customers
- Age group vs order value
- Weekend vs weekday demand

### 💰 Revenue & Profit Analysis
- Monthly revenue trends
- Discount impact on profit
- High-revenue cities and cuisines

### 🚚 Delivery Performance
- Average delivery time by city
- Distance vs delivery delay
- Delivery rating vs delivery time

### 🍽️ Restaurant Performance
- Top-rated restaurants
- Cancellation rate by restaurant
- Cuisine-wise performance

### ⚙️ Operational Insights
- Peak hour demand analysis
- Payment mode preferences
- Cancellation reason analysis

---

## 📊 Dashboard KPIs

The Power BI / Streamlit dashboard includes the following KPIs:

- Total Orders
- Total Revenue
- Average Order Value
- Average Delivery Time
- Cancellation Rate
- Average Delivery Rating
- Profit Margin %

---

## 📌 Results & Insights
- Cleaned and normalized dataset suitable for real-world analytics
- Identified key customer behavior patterns and peak demand hours
- Highlighted delivery bottlenecks and cancellation drivers
- Evaluated restaurant and cuisine performance
- Delivered actionable insights through interactive dashboards

---

## 🗂️ Project Structure
```plaintext
📁 Online-Food-Delivery-Analysis
│── 📂 data
│   └── Online_Food_Delivery_Analysis.csv
│── 📂 notebooks
│   └── EDA_and_Data_Cleaning.ipynb
│── 📂 sql
│   └── database_schema.sql
│── 📂 powerbi
│   └── Online_Food_Delivery_Dashboard.pbix
│── 📂 streamlit
│   └── app.py
│── README.md
