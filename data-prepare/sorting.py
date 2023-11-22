import pandas as pd

marketing_data = pd.read_csv("data/marketing_campaign.csv")
marketing_data = marketing_data[
    ['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income', 'Kidhome', 'Teenhome', 'Dt_Customer', 'Recency',
     'NumStorePurchases', 'NumWebVisitsMonth']]

sorted_data = marketing_data.sort_values('NumStorePurchases', ascending=False)
