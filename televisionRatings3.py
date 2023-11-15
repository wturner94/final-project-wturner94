import os
import pandas as pd

# read-in ratings report XLSXs if they contain certain characters in the filename
# rename that first column to 'TIME SLOT' because that column title is always different
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

# List to store DataFrames for each file
results_list = []

# Iterate through each file in the directory
for filename in files:
    # c33333all the function and assign the result to 'rough_ratings'
    rough_ratings = read_ratings_reports(os.path.join(directory_path, filename))

    # check if rough_ratings is not None before proceeding
    if rough_ratings is not None:
        # continue to process the ratings DataFrame
        rough_ratings = rough_ratings[['TIME SLOT', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
        ratings = rough_ratings.rename(columns={'Unnamed: 2':'PROGRAM', 'Unnamed: 3':'RATING', 'Unnamed: 4':'SHARE'})
        ratings = ratings.dropna()
        ratings['PROGRAM'] = ratings['PROGRAM'].str[:-13].str.strip()
        ratings['RATING'] = pd.to_numeric(ratings['RATING'], errors='coerce')
        ratings['SHARE'] = pd.to_numeric(ratings['SHARE'], errors='coerce')
        ratings['RATING'] = ratings['RATING'].round(2)
        ratings['SHARE'] = ratings['SHARE'].round(2)
        
        # append the result to the list
        results_list.append(ratings.iloc[1:])

# Concatenate DataFrames along columns after resetting the index for each DataFrame
merged_results = pd.concat([df.reset_index(drop=True) for df in results_list], axis=1)

# Reset the index of the merged DataFrame
merged_results.reset_index(drop=True, inplace=True)

merged_results = merged_results.fillna('---')

# Display the merged results
# print(merged_results.to_string(index=False))