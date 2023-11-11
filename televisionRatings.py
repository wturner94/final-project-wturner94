import pandas as pd

# read-in datasets from XLSXs
monday_ratings = pd.read_excel('10_30_2023_Monday_RATINGS_Preliminary.xlsx', skipfooter=2)

# constrain dataframe to the 3 pertinent columns
monday_ratings = monday_ratings[['10/30/2023 - 10/30/2023, All Day, All Week, All Hours', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]

# rename columns
monday_ratings = monday_ratings.rename(columns={'10/30/2023 - 10/30/2023, All Day, All Week, All Hours':'TIME SLOT', 'Unnamed: 2':'PROGRAM', 'Unnamed: 3':'RATING', 'Unnamed: 4':'SHARE'})

# remove NaN values
monday_ratings = monday_ratings.dropna()

# remove unwanted characters from the "Program" column (data always has 13)
monday_ratings['PROGRAM'] = monday_ratings['PROGRAM'].str[:-13].str.strip()

# convert RATING/SHARE columns to numeric
monday_ratings['RATING'] = pd.to_numeric(monday_ratings['RATING'], errors='coerce')
monday_ratings['SHARE'] = pd.to_numeric(monday_ratings['SHARE'], errors='coerce')

# round RATING/SHARE columns to two decimal places for easier viewing
monday_ratings['RATING'] = monday_ratings['RATING'].round(2)
monday_ratings['SHARE'] = monday_ratings['SHARE'].round(2)

# exclude the first row containing unwanted information when printing using iloc
print(monday_ratings.iloc[1:].to_string(index=False))

# import os
# contents = os.listdir(".")
# for report in contents
#   if reportName 
# write a loop to do the above for all ratings reports in the directory