# -*- coding: utf-8 -*-
"""Data Clean - Missing Value Imputation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yQc1GzHI6MOcPJJID9MH-KYZDL9svHtP

# Data Cleaning
## Missing value imputation by Mean, Median
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
dataset_path = r"K:\KaustavR25\SKILLZ\Data Science & Analysis, ML\Data-Science_ML----Projects-Resources-main\Study & Resource\Data Cleaning\train.csv"
df = pd.read_csv(dataset_path)
df

df.shape

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.head()

df.info()

df.isnull().sum()

missing_val_per = df.isnull().sum() / df.shape[0] * 100
missing_val_per

missing_val_col_20 = missing_val_per[missing_val_per > 20].keys()
missing_val_col_20

df2_drop_clm = df.drop(columns=missing_val_col_20)
df2_drop_clm.shape

df3_num = df2_drop_clm.select_dtypes(include=['int64', 'float64'])
df3_num.head()

plt.figure(figsize=(16, 9))
sns.heatmap(df3_num.isnull())

df3_num[df3_num.isnull().any(axis=1)]

df3_num.isnull().sum()

missing_num_var = [
    var for var in df3_num.columns if df3_num[var].isnull().sum() > 0
]
missing_num_var

plt.figure(figsize=(16, 9))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df3_num[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 5,
                     'color': '#DC143C'
                 })

df4_num_mean = df3_num.fillna(df3_num.mean())
df4_num_mean.isnull().sum().sum()

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df3_num[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 8,
                     'color': 'red'
                 },
                 label="Original")
    sns.distplot(df4_num_mean[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 8,
                     'color': 'blue'
                 },
                 label='Mean')
    plt.legend()

df5_num_median = df3_num.fillna(df3_num.median())
df5_num_median.isnull().sum().sum()

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df3_num[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 8,
                     'color': 'red'
                 },
                 label="Original")
    sns.distplot(df5_num_median[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 8,
                     'color': 'blue'
                 },
                 label='Mean')
    plt.legend()

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df3_num[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 5,
                     'color': 'red'
                 },
                 label="Original")
    sns.distplot(df4_num_mean[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 5,
                     'color': 'green'
                 },
                 label='Mean')
    sns.distplot(df5_num_median[var],
                 bins=20,
                 kde_kws={
                     'linewidth': 5,
                     'color': 'blue'
                 },
                 label='Median')
    plt.legend()

for i, var in enumerate(missing_num_var):
    plt.figure(figsize=(10, 10))
    plt.subplot(3, 1, 1)
    sns.boxplot(df[var])
    plt.subplot(3, 1, 2)
    sns.boxplot(df4_num_mean[var])
    plt.subplot(3, 1, 3)
    sns.boxplot(df5_num_median[var])

df_concat = pd.concat([
    df3_num[missing_num_var], df4_num_mean[missing_num_var],
    df5_num_median[missing_num_var]
])

df_concat[df_concat.isnull().any(axis=1)]

"""# Missing Value Imputation - Categorical Variables"""

cat_vars = df.select_dtypes(include='object')
cat_vars.head()

miss_val_cat = cat_vars.isnull().mean()*100
miss_val_cat

drop_vars = ['Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']
cat_vars.drop(columns=drop_vars, axis=1, inplace=True)
cat_vars.shape

isnull_per = cat_vars.isnull().mean()*100
miss_vars = isnull_per[isnull_per> 0].keys()
miss_vars

cat_vars['MasVnrType'].fillna("Missing")

cat_vars['MasVnrType'].mode()

cat_vars['MasVnrType'].value_counts()

cat_vars['MasVnrType'].fillna(cat_vars['MasVnrType'].mode()[0])

for var in miss_vars:
    cat_vars[var].fillna(cat_vars[var].mode()[0], inplace=True)
    print(var, "=", cat_vars[var].mode()[0])

cat_vars.isnull().sum()

plt.figure(figsize=(16,9))
for i,var in enumerate(miss_vars):
    plt.subplot(4,3,i+1)
    plt.hist(cat_vars[var], label='Imput')
    plt.hist(df[var].dropna(), label='Original')
    plt.legend()

df.update(cat_vars)
df.drop(columns=drop_vars, inplace=True)

df.select_dtypes(include='object').isnull().sum()

