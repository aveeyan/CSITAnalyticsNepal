# csit_stats.py consists of data from basic_stats.ipynb, which will be used for analytics and visualization

import pandas as pd
import numpy as np
import scipy.stats as scipy_stats

CSV_PATH = "./data/college_csit.csv"
df = pd.read_csv(CSV_PATH)
TOTAL_DISTRICTS = 77

# PORTION I: Grouping of Dataframe by Type of Institute 
df_grouped_by_type = df.groupby("Type")

constituent_institutes = df_grouped_by_type.get_group("Constituent")
constituent_institutes = constituent_institutes.reset_index(drop=True)
affiliated_institutes = df_grouped_by_type.get_group("Affiliated")
affiliated_institutes = affiliated_institutes.reset_index(drop=True)

total_institutes = len(df)
total_institutes_constituent = len(constituent_institutes)
total_institutes_affiliated = len(affiliated_institutes)

# PORTION II: Number of Seats by Type of Institutes
total_seats =  df["Seats"].sum()
seats_per_institute = df["Seats"].to_numpy()

seats_constituent = constituent_institutes["Seats"].sum()
seats_affiliated = affiliated_institutes["Seats"].sum()

seats_mean = np.mean(seats_per_institute)
seats_median = np.median(seats_per_institute)
seats_min = np.min(seats_per_institute)
seats_max = np.max(seats_per_institute)
seats_q1 = np.percentile(seats_per_institute, 25)
seats_q3 = np.percentile(seats_per_institute, 75)
seats_skewness = scipy_stats.skew(seats_per_institute)
seats_kurtosis = scipy_stats.kurtosis(seats_per_institute)

# PORTION III: Number of District having institutions with CSIT
districts_csit = df["District"].unique()
districts_csit_count = len(districts_csit)


