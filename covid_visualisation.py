import json
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the supplied JSON data.
with open("covid_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 2. Convert the list of dictionaries into a pandas DataFrame.
df = pd.DataFrame(data)

# 3. Convert Date from text into a real datetime value.
df["Date"] = pd.to_datetime(df["Date"], format="%Y/%m/%d")

# 4. Clean numeric columns.
#    Some values use a space as a thousands separator, e.g. "1 139".
numeric_columns = [column for column in df.columns if column != "Date"]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column].astype(str).str.replace(r"\s+", "", regex=True),
        errors="coerce"
    )

# 5. Create the line graph.
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    df["Date"],
    df["Total Confirmed Cases"],
    label="Total confirmed cases",
    linewidth=2
)

ax.plot(
    df["Date"],
    df["Total Deaths"],
    label="Total deaths",
    linewidth=2
)

ax.plot(
    df["Date"],
    df["Daily Confirmed Cases"],
    label="Daily confirmed cases",
    linewidth=2
)

# 6. Add labels and formatting.
ax.set_title("COVID-19 Cases and Deaths: 5 March – 12 June 2020")
ax.set_xlabel("Date")
ax.set_ylabel("Number")
ax.grid(True, alpha=0.25)
ax.legend()

# Rotate date labels so they do not overlap.
fig.autofmt_xdate()

plt.tight_layout()

# 7. Save the graph as an image and display it.
plt.savefig("covid19_visualisation.png", dpi=200, bbox_inches="tight")
plt.show()
