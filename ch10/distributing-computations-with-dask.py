
import dask.dataframe as dd


data = dd.read_csv("sample.csv")
print(data.head())


sum_data = data.lower + data.upper


print(sum_data)
print(sum_data.compute())



means = data.loc[:, ("lower", "upper")].mean().compute()
print(means)