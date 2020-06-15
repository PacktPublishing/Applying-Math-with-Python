
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

from tsdata import generate_sample_data


sample_ts, test_ts = generate_sample_data(undiff=True, trend=0.2)


df_for_prophet = pd.DataFrame({
    "ds": sample_ts.index,   # dates
    "y": sample_ts.values    # values
})

model = Prophet()
model.fit(df_for_prophet)


forecast_df = model.make_future_dataframe(periods=50)


forecast = model.predict(forecast_df)


fig, ax = plt.subplots(tight_layout=True)
sample_ts.plot(ax=ax, label="Observed", title="Forecasts")
forecast.plot(x="ds", y="yhat", ax=ax, c="r", label="Predicted")
ax.fill_between(forecast["ds"].values, forecast["yhat_lower"].values, 
                forecast["yhat_upper"].values, color="r", alpha=0.4)
test_ts.plot(ax=ax, c="k", label="Future")
ax.legend()
ax.set_xlabel("Date")
ax.set_ylabel("Value")


plt.show()
