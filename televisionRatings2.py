import os
import pandas as pd

# read-in ratings report XLSXs if they contain certain characters in the filename
# rename that first columns to 'TIME SLOT' because that column title is always different
def read_ratings_reports(filename):
    if "day_ratings" in filename.lower():
        # Get the full path of the file
        filepath = os.path.abspath(filename)
        rough_ratings = pd.read_excel(filepath, skipfooter=2)
        rough_ratings.rename(columns={c: 'TIME SLOT' for c in rough_ratings.columns if 'All Day, All Week, All Hours' in c}, inplace=True)
        return rough_ratings
    else:
        print(f"The file {filename} does not exist or is not in the correct format.")
        return None

# Get the current working directory
directory_path = os.getcwd()

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Iterate through each file in the directory
for filename in files:
    # Call the function and assign the result to 'rough_ratings'
    rough_ratings = read_ratings_reports(os.path.join(directory_path, filename))

    # check if rough_ratings is not None before proceeding
    if rough_ratings is not None:
        # constrain dataframe to the 3 pertinent columns
        rough_ratings = rough_ratings[['TIME SLOT', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
        
        # rename columns
        ratings = rough_ratings.rename(columns={'Unnamed: 2':'PROGRAM', 'Unnamed: 3':'RATING', 'Unnamed: 4':'SHARE'})
        
        # remove NaN values
        ratings = ratings.dropna()
        
        # remove unwanted characters from the "Program" column (data always has 13)
        ratings['PROGRAM'] = ratings['PROGRAM'].str[:-13].str.strip()
        
        # convert RATING/SHARE columns to numeric
        ratings['RATING'] = pd.to_numeric(ratings['RATING'], errors='coerce')
        ratings['SHARE'] = pd.to_numeric(ratings['SHARE'], errors='coerce')
        
        # round RATING/SHARE columns to two decimal places for easier viewing
        ratings['RATING'] = ratings['RATING'].round(2)
        ratings['SHARE'] = ratings['SHARE'].round(2)
        
        # exclude the first row containing unwanted information when printing using iloc
        print(ratings.iloc[1:].to_string(index=False))