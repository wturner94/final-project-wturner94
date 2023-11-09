import pandas as pd

# read-in datasets from XLSXs
monday_ratings = pd.read_excel('10_30_2023_Monday_RATINGS_Preliminary.xlsx', skipfooter=2)
# constrain dataframe to the 3 pertinent columns
monday_ratings = monday_ratings[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
# remove NaN values
monday_ratings = monday_ratings.dropna()

print(monday_ratings)

# need to set column titles from 'Unnamed : _' to ['Program', 'QH Rtg', 'QH Share']
# find more xlsx from Mondays near that date and download