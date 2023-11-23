import pandas as pd

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[['ID', 'Year_Birth', 'Education', 'Income']]

# Drop missing values using the dropna method

marketing_data_withoutna = marketing_data.dropna(how='any')
