import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm

from tsdata import generate_sample_data

sample_ts, test_ts = generate_sample_data(undiff=True, seasonal=True)

ts_fig, ts_ax = plt.subplots(tight_layout=True)

sample_ts.plot(ax=ts_ax, title="Time series", label="Observed")
ts_ax.set_xlabel("Date")
ts_ax.set_ylabel("Value")


ts_fig.savefig("sarima-ts-plot.png", dpi=300)

ap_fig, (acf_ax, pacf_ax) = plt.subplots(2, 1, sharex=True, tight_layout=True)
sm.graphics.tsa.plot_acf(sample_ts, ax=acf_ax)
sm.graphics.tsa.plot_pacf(sample_ts, ax=pacf_ax)
pacf_ax.set_xlabel("Lag")
acf_ax.set_ylabel("Value")
pacf_ax.set_ylabel("Value")

ap_fig.savefig("sarima-acf-pacf.png", dpi=300)

diffs = sample_ts.diff().dropna()
dap_fig, (dacf_ax, dpacf_ax) = plt.subplots(2, 1, sharex=True, tight_layout=True)
sm.graphics.tsa.plot_acf(diffs, ax=dacf_ax, title="Differenced ACF")
sm.graphics.tsa.plot_pacf(diffs, ax=dpacf_ax, title="Differenced PACF")
dpacf_ax.set_xlabel("Lag")
dacf_ax.set_ylabel("Value")
dpacf_ax.set_ylabel("Value")

dap_fig.savefig("sarima-r-acf-pacf.png", dpi=300)


model = sm.tsa.SARIMAX(sample_ts, order=(1, 1, 1), seasonal_order=(1, 0, 0, 7))
fitted_seasonal = model.fit()
print(fitted_seasonal.summary())

residuals = fitted_seasonal.resid
fitted_seasonal.fittedvalues.plot(ax=ts_ax, c="r", label="Predicted")

rap_fig, (racf_ax, rpacf_ax) = plt.subplots(2, 1, sharex=True, tight_layout=True)
sm.graphics.tsa.plot_acf(residuals, ax=racf_ax, title="Residual ACF")
sm.graphics.tsa.plot_pacf(residuals, ax=rpacf_ax, title="Residual PACF")
rpacf_ax.set_xlabel("Lag")
racf_ax.set_ylabel("Value")
rpacf_ax.set_ylabel("Value")

forecast_result = fitted_seasonal.get_forecast(steps=50)

forecast_index = pd.date_range("2021-01-01", periods=50)
forecast = forecast_result.predicted_mean

forecast.plot(ax=ts_ax, c="g", label="Forecasts")
conf = forecast_result.conf_int()
ts_ax.fill_between(forecast_index, conf["lower y"], conf["upper y"], color="r", alpha=0.4)
test_ts.plot(ax=ts_ax, color="k", label="Actual future")
ts_ax.legend()

ts_fig.savefig("sarima-ts-predicted.png", dpi=300)


plt.show()

