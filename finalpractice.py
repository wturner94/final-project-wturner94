# imports the pandas library
import pandas as pd

# reads-in the datasets from CSVs
demographics = pd.read_csv('RCS_Households_Demographics.csv')
infrastructure = pd.read_csv('Jefferson_County_KY_Bikeways.csv')

# removes households from the dataset without reported income
demographics = demographics.dropna()

# converts zip codes to integer to remove the decimal <--------------- this isn't working 
# demographics['ZIP_Code'] = demographics['ZIP_Code'].astype(str)

# creates variables to extract the columns we want to include
demographics_sorted = demographics.loc[:, ['Annual_Income', 'ZIP_Code']]
infrastructure_sorted = infrastructure.loc[:, ['ROADNAME', 'SHAPELEN']]

mainframe = pd.merge(demographics, infrastructure, on='ROADNAME')
print(mainframe)

# print(demographics_sorted)
# print(infrastructure_sorted)

# print(demographics.loc[demographics.ZIP_Code == 40218.0])
# print(infrastructure.head(), infrastructure.tail())