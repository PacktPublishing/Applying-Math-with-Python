import matplotlib.pyplot as plt
import statsmodels.api as sm

from tsdata import generate_sample_data

sample_ts, _ = generate_sample_data()


ts_fig, ts_ax = plt.subplots(tight_layout=True)
sample_ts.plot(ax=ts_ax, label="Observed")
ts_ax.set_title("Time series data")
ts_ax.set_xlabel("Date")
ts_ax.set_ylabel("Value")

ts_fig.savefig("arma-time-series.png", dpi=300)



adf_results = sm.tsa.adfuller(sample_ts)
adf_pvalue = adf_results[1]
print("Augmented Dickey-Fuller test:\nP-value:", adf_pvalue)


ap_fig, (acf_ax, pacf_ax) = plt.subplots(2, 1, sharex=True, tight_layout=True)
sm.graphics.tsa.plot_acf(sample_ts, ax=acf_ax, title="Observed autocorrelation")
sm.graphics.tsa.plot_pacf(sample_ts, ax=pacf_ax, title="Observed partial autocorrelation")
pacf_ax.set_xlabel("Lags")
pacf_ax.set_ylabel("Value")
acf_ax.set_ylabel("Value")

ap_fig.savefig("arma-acf-and-pacf.png", dpi=300)


arma_model = sm.tsa.ARMA(sample_ts, order=(1, 1))

arma_results = arma_model.fit()
print(arma_results.summary())

residuals = arma_results.resid
rap_fig, (racf_ax, rpacf_ax) = plt.subplots(2, 1, sharex=True, tight_layout=True)
sm.graphics.tsa.plot_acf(residuals, ax=racf_ax, title="Residual autocorrelation")
sm.graphics.tsa.plot_pacf(residuals, ax=rpacf_ax, title="Residual partial autocorrelation")
rpacf_ax.set_xlabel("Lags")
rpacf_ax.set_ylabel("Value")
racf_ax.set_ylabel("Value")

rap_fig.savefig("arma-residual-acf-pacf.png", dpi=300)


fitted = arma_results.fittedvalues
fitted.plot(c="r", ax=ts_ax, label="Fitted")
ts_ax.legend()
ts_fig.savefig("arma-time-series-predicted.png", dpi=300)




plt.show()


