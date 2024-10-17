import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the app
st.title('Bank Fraud Detection Dashboard')

# Loading the dataset 
@st.cache
def load_data():
    return pd.read_csv('train.csv')

train = load_data()

# Converting 'transaction time' to datetime
train['transaction time'] = pd.to_datetime(train['transaction time'])

# Creating new columns for hour and day_of_week
train['hour'] = train['transaction time'].dt.hour
train['day_of_week'] = train['transaction time'].dt.day_name()

# Sidebar filters (optional, for more interaction)
st.sidebar.header("Filter by:")
selected_day = st.sidebar.selectbox("Select Day of the Week:", train['day_of_week'].unique())

# Filtering data based on sidebar input
filtered_data = train[train['day_of_week'] == selected_day]

# Show filtered dataset
st.subheader(f"Filtered Data for {selected_day}")
st.write(filtered_data)

### PLOTS

# --- Plot 1: Transactions Count by Day of the Week ---
st.subheader("Transaction Count by Day of the Week")
plt.figure(figsize=(10, 6))
sns.countplot(data=train, x='day_of_week', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.xticks(rotation=45)
st.pyplot()

# --- Plot 2: Fraudulent vs Non-Fraudulent Transactions per Hour ---
st.subheader("Fraudulent vs Non-Fraudulent Transactions per Hour")
plt.figure(figsize=(12, 6))
sns.countplot(data=train, x='hour', hue='fradulent')
plt.title('Fraudulent vs Non-Fraudulent Transactions per Hour')
st.pyplot()

# --- Plot 3: Fraud Rate by Day of the Week ---
st.subheader("Fraud Rate by Day of the Week")
fraud_per_day = train.groupby('day_of_week')['fradulent'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
fraud_per_day.plot(kind='bar', color='coral')
plt.title('Fraudulent Transactions by Day')
plt.xticks(rotation=45)
st.pyplot()

# --- Plot 4: Distribution of Current Bank Amounts ---
st.subheader("Distribution of Current Bank Amounts")
plt.figure(figsize=(10, 6))
sns.histplot(train['current bank amount'], kde=True, color='blue')
plt.title('Distribution of Current Bank Amounts')
st.pyplot()

# --- Plot 5: Distribution of Age of Customers ---
st.subheader("Distribution of Customer Age")
plt.figure(figsize=(10, 6))
sns.histplot(train['age'], kde=True, color='green')
plt.title('Distribution of Customer Age')
st.pyplot()

# --- Plot 6: Fraud by Account Type ---
st.subheader("Fraud by Account Type")
plt.figure(figsize=(10, 6))
sns.countplot(data=train, x='Account type', hue='fradulent', palette='coolwarm')
plt.title('Fraudulent Transactions by Account Type')
st.pyplot()

# --- Plot 7: Fraud by Credit Card Type ---
st.subheader("Fraud by Credit Card Type")
plt.figure(figsize=(10, 6))
sns.countplot(data=train, x='credit card type', hue='fradulent', palette='viridis')
plt.title('Fraudulent Transactions by Credit Card Type')
st.pyplot()

# --- Plot 8: Fraud by Occupation ---
st.subheader("Fraud by Occupation")
plt.figure(figsize=(12, 6))
sns.countplot(data=train, y='occupation', hue='fradulent', palette='magma', order=train['occupation'].value_counts().index)
plt.title('Fraudulent Transactions by Occupation')
st.pyplot()

# --- Plot 9: Relationship Between Current and Last Bank Amounts ---
st.subheader("Relationship Between Current and Last Bank Amounts")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_train, x='last bank amount', y='current bank amount', hue='fradulent', palette='coolwarm')
plt.title('Current vs Last Bank Amount (Fraud Indicator)')
st.pyplot()

# --- Plot 10: Time Taken for Transactions (Fraud vs Non-Fraud) ---
st.subheader("Transaction Time Taken (Fraud vs Non-Fraud)")
plt.figure(figsize=(10, 6))
sns.boxplot(data=train, x='fradulent', y='time taken', palette='Set2')
plt.title('Time Taken for Transactions (Fraudulent vs Non-Fraudulent)')
st.pyplot()

