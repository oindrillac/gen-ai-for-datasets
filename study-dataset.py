# This script has been written with the help of GitHub CoPilot
# I am using the free Beta version
# One can use this script as a template to explore their own dataset or
# Use this as an example to construct their own script for understanding the underlying patterns of a dataset
# with the help of GitHub CoPilot

# Read datasets/kaggle-us-population/data.csv and explore the dataset

import pandas as pd

# Read the dataset
df = pd.read_csv('datasets/kaggle-us-population/data.csv')
metadata = pd.read_csv('datasets/kaggle-us-population/metadata.csv')


# Write a function that takes in the dataset and explores columns in the dataset, 
# explores the shape of the dataset, and explores the first 5 rows of the dataset, 
# and also explores the datatypes of the columns of the dataframe

def explore_dataset(df):
    print(df.columns)
    print(df.shape)
    print(df.head())
    print(df.dtypes)

explore_dataset(df)

# View all reports in the metadata
print(metadata.report.value_counts())

time_series_codes = metadata[metadata.report == 'Housing Vacancies and Homeownership'].time_series_code.tolist()
time_series_code_dict = {}

# Save all the time_series_codes and dt_desc in form of a dictionary for report 'Housing Vacancies and Homeownership' from metadata
time_series_code_dict = {time_series_code: metadata[metadata.time_series_code == time_series_code].dt_desc.tolist()[0] for time_series_code in time_series_codes}
print(time_series_code_dict)
