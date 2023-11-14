
import pandas as pd
from numpy import int64, array
from scipy import stats
from scipy.stats._mstats_basic import ModeResult

covid_data = pd.read_csv("covid-data.csv")
covid_data = covid_data[['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases']]

data_mode = stats.mode(covid_data["new_cases"])

data_mode = ModeResult(mode=array([0], dtype=int64) ,count=array([805]))

data_mode[0] = array([0], dtype=int64)

data_mode[0][0]
