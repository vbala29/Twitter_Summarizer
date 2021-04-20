import pandas as pd
import matplotlib as style
import matplotlib.pyplot as plt

aggregated_csvs = ["SampleData/10Tweets/10TweetsAggregationPrep.csv", "SampleData/20Tweets/20TweetsAggregationPrep.csv"]

aggregated_dfs = [pd.read_csv(x) for x in aggregated_csvs]
print(aggregated_dfs)
y_vals = []
x_vals = []


for j, df in enumerate(aggregated_dfs):
    for i, hit in df.iterrows():
        likes = int(hit["Average Likes"])
        rating = int(hit["Average Rating"])
        print(likes)
        print(rating)
        x_vals.append(likes)
        y_vals.append(rating)


style.use("MacOSX")
plt.plot(x_vals, y_vals, "o")
plt.show()






