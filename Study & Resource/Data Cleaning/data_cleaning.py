# -*- coding: utf-8 -*-
"""Data Cleaning.ipynb
# Data Cleaning
## Method - Delete Rows & Columns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"K:\KaustavR25\SKILLZ\Data Science & Analysis, ML\Data-Science_ML----Projects-Resources-main\Study & Resource\Data Cleaning\train.csv")
df

df.shape

df.head(6)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.head(6)

df.tail(6)

df.info()

#df.isnull()

df.isnull().sum()

plt.figure(figsize=(25,25))

sns.heatmap(df.isnull())

null_var = df.isnull().sum()/df.shape[0] * 100
null_var

drop_columns = null_var[null_var>17].keys()
drop_columns

df2_drop_clm = df.drop(columns=drop_columns)

df2_drop_clm.shape

sns.heatmap(df2_drop_clm.isnull())

df3_drop_rows = df2_drop_clm.dropna()

df3_drop_rows.shape

plt.figure(figsize=(25,25))
sns.heatmap(df3_drop_rows.isnull())

df3_drop_rows.isnull().sum()

df3_drop_rows.isnull().sum().sum()

df3_drop_rows.select_dtypes(include=['int64','float64']).columns

sns.distplot(df['MSSubClass'])

sns.distplot(df3_drop_rows['MSSubClass'])

sns.distplot(df['MSSubClass'])
sns.distplot(df3_drop_rows['MSSubClass'])

num_vars = ['MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
       'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
       'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
       'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
       'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
       'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
       'MoSold', 'YrSold', 'SalePrice']

plt.figure(figsize=(25,25))
for i, var in enumerate(num_vars):
    plt.subplot(9,4,i+1)
    sns.distplot(df[var], bins=20)
    sns.distplot(df3_drop_rows[var], bins=20)

cat_var = df3_drop_rows.select_dtypes(include=['object']).columns

pd.concat([df['MSZoning'].value_counts()/df.shape[0] * 100, df3_drop_rows['MSZoning'].value_counts()/df3_drop_rows.shape[0] * 100], axis=1, keys=['MSZoning_org', 'MSZoning_clean'])

def cat_var_dist(var):
    return pd.concat([df[var].value_counts()/df.shape[0] * 100, df3_drop_rows[var].value_counts()/df3_drop_rows.shape[0] * 100], axis=1, keys=[var+'_org', var+'_clean'])

cat_var_dist('MSZoning')
