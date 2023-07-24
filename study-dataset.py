# This script has been written with the help of GitHub CoPilot
# I am using the free Beta version
# One can use this script as a template to explore their own dataset or
# Use this as an example to construct their own script for understanding the underlying patterns of a dataset
# with the help of GitHub CoPilot

# Read datasets/kaggle-us-population/data.csv and explore the dataset

import pandas as pd

# Read the dataset
df = pd.read_csv('datasets/kaggle-us-population/data.csv')

# Write a function that takes in the dataset and explores columns in the dataset, 
# explores the shape of the dataset, and explores the first 5 rows of the dataset, 
# and also explores the datatypes of the columns of the dataframe

def explore_dataset(df):
    print(df.columns)
    print(df.shape)
    print(df.head())
    print(df.dtypes)

explore_dataset(df)