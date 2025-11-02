# 🍔 Exploratory Data Analysis (EDA) on McDonald's Nutrition Dataset

## 📘 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the **McDonald's Nutrition Dataset** to uncover insights about the nutritional content of menu items.  
The goal is to understand calorie distribution, nutrient relationships, and identify healthier food choices based on protein, fat, and sugar levels.

---

## 📂 Dataset
**Source:** [McDonald's Nutrition Facts – Kaggle](https://www.kaggle.com/datasets/mcdonalds/nutrition-facts)

The dataset contains detailed nutritional information for McDonald's menu items, including:
- Calories  
- Protein  
- Total Fat  
- Saturated Fat  
- Carbohydrates  
- Sugars  
- Sodium  
- Category  
- Serving Size  

---

## 🧠 Objectives
- Clean and preprocess the dataset.
- Perform descriptive statistical analysis.
- Visualize nutritional distributions.
- Analyze category-wise calorie and protein trends.
- Identify high-calorie and low-calorie items.
- Explore correlations between different nutrients.
- Provide actionable recommendations for health-conscious consumers.

---

## ⚙️ Steps Performed

### 1. Data Loading & Cleaning
- Loaded dataset using `pandas`.
- Handled missing values (filled numerics with median, categoricals with mode).
- Removed duplicate records.
- Ensured column data types were correct.

### 2. Descriptive Statistics
- Generated mean, median, mode, and standard deviation for numeric columns.
- Checked overall nutritional balance.

### 3. Visualization & Insights
- **Distribution plots:** Calories, Fat, Sugar, and Protein.  
- **Boxplots:** To detect outliers and spread.  
- **Category-wise bar charts:** Average nutrient values across menu categories.  
- **Correlation heatmap:** Shows how calories relate to fat, sugar, and protein.  
- **Top 10 High/Low Calorie Items:** Highlighted most and least caloric foods.  
- **Protein-Calorie Ratio:** Identified high-protein, low-calorie options.

### 4. Recommendations
- Promote healthier, high protein-to-calorie ratio items.
- Display calorie counts prominently on menus.
- Limit high-sugar beverages and desserts.
- Add more balanced meal options for health-conscious customers.

---

## 📊 Technologies Used
| Library | Purpose |
|----------|----------|
| **Pandas** | Data manipulation & analysis |
| **NumPy** | Numerical operations |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical data visualization |
| **OS** | File path handling |

---

## 📁 Repository Structure

