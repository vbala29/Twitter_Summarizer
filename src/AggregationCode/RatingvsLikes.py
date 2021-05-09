import pandas as pd
import matplotlib as style
import matplotlib.pyplot as plt

aggregated_csvs = ["SampleData/AggregationPrep/10TweetsAggregationPrep.csv", "SampleData/AggregationPrep/20TweetsAggregationPrep.csv"]

aggregated_dfs = [pd.read_csv(x) for x in aggregated_csvs]
print(aggregated_dfs)
y_vals = []
x_vals = []

rating_sums = [(0, 0) for x in range(0, 5)]
print(rating_sums)

for j, df in enumerate(aggregated_dfs):
    for i, hit in df.iterrows():
        likes = int(hit["Average Likes"])
        rating = int(hit["Average Rating"])
        tup = rating_sums[rating - 1]
        rating_sums[rating - 1] = (tup[0] + likes, tup[1] + 1)
        print(rating_sums[rating - 1])
        x_vals.append(likes)
        y_vals.append(rating)

rating_averages = [(x/y) for (x, y) in rating_sums]

style.use("MacOSX")
figure = plt.figure()
#plt1 = figure.add_subplot(111)
#plt1.plot(x_vals, y_vals, "o")
#plt.show()

plt2 = figure.add_subplot(111)
plt2.plot([1, 2, 3, 4, 5], rating_averages)
plt.show()






