
import dask.dataframe as dd


data = dd.read_csv("sample.csv")
print(data.head())


sum_data = data.lower + data.upper
print(sum_data)

result = sum_data.compute()
print(result.head())



means = data.loc[:, ("lower", "upper")].mean().compute()
print(means)