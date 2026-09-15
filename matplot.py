fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(
    df["time"],
    df["temperature_2m"],
    label="Temperature"
)

ax.plot(
    df["time"],
    df["temperature_moving_average"],
    label="6-hour average"
)

ax.set(
    title="Temperature Over the Next 7 Days",
    xlabel="Time",
    ylabel="Temperature (°C)"
)

ax.grid(True, alpha=0.3)
ax.legend()

fig.autofmt_xdate()
fig.tight_layout()

plt.show()


fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(
    df["time"],
    df["relative_humidity_2m"],
    label="Humidity"
)

ax.set(
    title="Relative Humidity Over Time",
    xlabel="Time",
    ylabel="Humidity (%)"
)

ax.grid(True, alpha=0.3)
ax.legend()

fig.autofmt_xdate()
fig.tight_layout()

plt.show()


fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(
    df["time"],
    df["wind_speed_10m"],
    label="Wind speed"
)

ax.set(
    title="Wind Speed Over Time",
    xlabel="Time",
    ylabel="Wind Speed (km/h)"
)

ax.grid(True, alpha=0.3)
ax.legend()

fig.autofmt_xdate()
fig.tight_layout()

plt.show()


fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(
    temperature,
    humidity,
    alpha=0.6
)

ax.set(
    title="Temperature vs Humidity",
    xlabel="Temperature (°C)",
    ylabel="Humidity (%)"
)

ax.grid(True, alpha=0.3)

fig.tight_layout()

plt.show()


df.to_csv(
    "weather_data.csv",
    index=False
)
