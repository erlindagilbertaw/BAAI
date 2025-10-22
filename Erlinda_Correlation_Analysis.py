#
# Erlinda韋琳達, 2025/10/24
# File: Erlinda_Correlation_Analysis.py
# Apply correlation analysis to business problems
#

#Data manipulation and analysis
import pandas as pd
import numpy as np

#Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

#Statical analysis
from scipy import stats

# 1. Input
df = pd.read_csv('Simple_Data.csv')


# 2. Process
print(df.isnull().sum())

# 3. Output
#print("Data loaded successfully")
#print(f"Dataset shape: {df.shape}")