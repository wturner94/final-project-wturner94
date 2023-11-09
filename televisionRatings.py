# read-in datasets from CSVs
import pandas as pd

monday_ratings = pd.read_excel('10_30_2023_Monday_RATINGS_Preliminary.xlsx', skipfooter=2)
monday_ratings = monday_ratings[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
monday_ratings = monday_ratings.dropna()



# print(monday_ratings.iloc[4:-2,2:8])
print(monday_ratings)

# need to set column titles
# find more xlsx from Mondays near that date and download
# tell script to fill the NaN values on TP Sh (or maybe omit???)



