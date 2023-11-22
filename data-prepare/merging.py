import pandas as pd

marketing_sample1 = pd.read_csv("data/marketing_campaign_merge1.csv")

marketing_sample2 = pd.read_csv("data/marketing_campaign_merge2.csv")

merged_data = pd.merge(marketing_sample1, marketing_sample2, on="ID")
