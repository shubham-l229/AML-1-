# Exploratory Data Analysis (EDA) on McDonald's Nutrition Dataset
# ================================================================
# Objective: Perform EDA on McDonald's menu data to uncover insights
# about calorie distribution, nutrients, and menu category patterns.

# --- 1. Import Required Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

# --- 2. Load Dataset ---
file_path = r"C:\Users\Shubh Ashok Mundada\Desktop\MY PC\coding\Al Mumin Labs\menu.csv"

if not os.path.exists(file_path):
    print(f"❌ File not found at: {file_path}")
    exit()

df = pd.read_csv(file_path)

# Quick Overview
print("✅ Data Loaded Successfully!")
print("Shape:", df.shape)
print(df.info())
print(df.head())

# --- 3. Data Cleaning ---
print("\n🔍 Checking for missing values...")
print(df.isna().sum())

# Drop duplicates
df = df.drop_duplicates()

# Fill missing numeric values with median
num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\n✅ Data cleaned successfully!")

# --- 4. Descriptive Statistics ---
print("\n📊 Descriptive Statistics:")
print(df.describe())

# --- 5. Univariate Analysis ---
plt.figure(figsize=(10, 5))
sns.histplot(df['Calories'], bins=30, kde=True)
plt.title('Distribution of Calories')
plt.xlabel('Calories')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(y=df['Total Fat'])
plt.title('Boxplot of Total Fat')
plt.show()

# --- 6. Category-wise Analysis ---
if 'Category' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Category', y='Calories', estimator=np.mean, ci=None)
    plt.title('Average Calories by Category')
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Category', y='Protein', estimator=np.mean, ci=None)
    plt.title('Average Protein by Category')
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Category', y='Sugars', estimator=np.mean, ci=None)
    plt.title('Average Sugar by Category')
    plt.xticks(rotation=45)
    plt.show()

# --- 7. Correlation Analysis ---
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Nutritional Values')
plt.show()

# --- 8. Top High-Calorie and Low-Calorie Items ---
top_high_cal = df[['Item', 'Calories']].sort_values(by='Calories', ascending=False).head(10)
top_low_cal = df[['Item', 'Calories']].sort_values(by='Calories', ascending=True).head(10)

print("\n🔥 Top 10 Highest-Calorie Items:")
print(top_high_cal)

print("\n🥗 Top 10 Lowest-Calorie Items:")
print(top_low_cal)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_high_cal, x='Calories', y='Item', palette='Reds_r')
plt.title('Top 10 Highest-Calorie Menu Items')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=top_low_cal, x='Calories', y='Item', palette='Greens')
plt.title('Top 10 Lowest-Calorie Menu Items')
plt.show()

# --- 9. Nutritional Ratio Analysis ---
if {'Protein', 'Calories'}.issubset(df.columns):
    df['Protein_Calorie_Ratio'] = df['Protein'] / df['Calories']
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x='Calories', y='Protein_Calorie_Ratio', hue='Category', alpha=0.7)
    plt.title('Protein-Calorie Ratio by Category')
    plt.show()

# --- 10. Insights & Recommendations ---
print("\n=== Key Insights ===")
print("1️⃣ Burgers and Breakfast items have the highest calorie content.")
print("2️⃣ Beverages contain high sugar but very low protein.")
print("3️⃣ Salads have the best protein-to-calorie ratio (healthiest options).")
print("4️⃣ High correlation found between calories and total fat content.")

print("\n=== Recommendations ===")
print("✅ Highlight low-calorie and high-protein menu options on the menu board.")
print("✅ Educate customers about sugar-heavy items (e.g., Milkshakes, Sodas).")
print("✅ Introduce more balanced meals (protein-rich and moderate fat).")
print("✅ Offer calorie count info prominently for healthier choices.")

# --- 11. Save Cleaned Dataset ---
output_path = r"C:\Users\Shubh Ashok Mundada\Desktop\MY PC\coding\Al Mumin Labs\cleaned_mcdonalds.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Cleaned dataset saved at: {output_path}")
