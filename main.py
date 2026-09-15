import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": -23.5505,
    "longitude": -46.6333,
    "hourly": (
        "temperature_2m,"
        "relative_humidity_2m,"
        "wind_speed_10m"
    ),
    "forecast_days": 7,
    "timezone": "America/Sao_Paulo"
}


response = requests.get(url, params=params)

data = response.json()

hourly_data = data["hourly"]

df = pd.DataFrame(hourly_data)

df["time"] = pd.to_datetime(df["time"])

temperature = np.array(df["temperature_2m"])
humidity = np.array(df["relative_humidity_2m"])
wind = np.array(df["wind_speed_10m"])


average_temperature = np.mean(temperature)
maximum_temperature = np.max(temperature)
minimum_temperature = np.min(temperature)
temperature_std = np.std(temperature)

average_humidity = np.mean(humidity)
maximum_humidity = np.max(humidity)
minimum_humidity = np.min(humidity)

average_wind = np.mean(wind)
maximum_wind = np.max(wind)
minimum_wind = np.min(wind)


df["temperature_change"] = df["temperature_2m"].diff()

df["temperature_moving_average"] = (
    df["temperature_2m"]
    .rolling(6)
    .mean()
)


hottest_hour = df.loc[
    df["temperature_2m"].idxmax()
]

coldest_hour = df.loc[
    df["temperature_2m"].idxmin()
]

strongest_wind = df.loc[
    df["wind_speed_10m"].idxmax()
]


