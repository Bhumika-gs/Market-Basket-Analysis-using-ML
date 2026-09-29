# 🛒 Market Basket Analysis & Product Recommendation System

## 📌 Project Overview

This project analyzes customer purchasing patterns using Market Basket Analysis and Association Rule Mining.

The project uses the Apriori algorithm to identify products that are frequently purchased together and generates product recommendations based on association rules.

## 📌 Deployed Website
https://market-basket-analysis-using-ml-6au47xnipxsgvohfvnaoaz.streamlit.app/

## 🎯 Objectives

- Analyze customer purchasing behavior
- Identify frequently purchased products
- Discover relationships between products
- Generate association rules
- Build a product recommendation system
- Deploy the recommendation system using Streamlit

## 📊 Dataset

The project uses the Online Retail dataset.

The dataset contains transactional information including:

- Invoice Number
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed cancelled transactions
- Removed missing product descriptions
- Removed negative quantities
- Removed zero/negative prices
- Filtered transactions for the United Kingdom
- Converted transactions into a basket format
- Converted quantities into binary purchase indicators

## 🤖 Methodology

The project follows this workflow:

Raw Transaction Data  
↓  
Data Cleaning  
↓  
Transaction Basket Creation  
↓  
Frequent Itemset Mining  
↓  
Apriori Algorithm  
↓  
Association Rules  
↓  
Support, Confidence & Lift  
↓  
Product Recommendations  
↓  
Streamlit Application

## 📈 Association Rule Metrics

### Support

Measures how frequently an item or itemset appears in all transactions.

### Confidence

Measures how often the consequent is purchased when the antecedent is purchased.

### Lift

Measures the strength of association between products.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MLxtend
- Apriori Algorithm
- Association Rule Mining
- Streamlit
- Jupyter Notebook

## 🌐 Application

The Streamlit application allows users to select a product and receive related product recommendations based on the discovered association rules.

## 👩‍💻 Author

Bhumika G S
