import pandas as pd
import matplotlib as style
import matplotlib.pyplot as plt

aggregated_csvs = ["SampleData/0Tweets/0TweetsAggregationPrep.csv",
                   "SampleData/10Tweets/10TweetsAggregationPrep.csv", "SampleData/20Tweets/20TweetsAggregationPrep.csv"]

aggregated_dfs = [pd.read_csv(x) for x in aggregated_csvs]
y_vals = []
x_vals = [0, 10, 20]

for df in aggregated_dfs:
    y_vals.append(df["Average Rating"].mean())

style.use("MacOSX")
plt.plot(x_vals, y_vals)
plt.show()






