import pandas as pd

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[['ID', 'Year_Birth', 'Kidhome', 'Teenhome']]

# Replace the values in Teenhome with has teen and has no teen:
marketing_data['Teenhome_replaced'] = marketing_data['Teenhome'].replace([0, 1, 2],
                                                                         ['has no teen', 'hasteen', 'has teen'])
