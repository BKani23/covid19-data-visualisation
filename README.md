

# COVID-19 Data Visualisation
A Python data visualisation project analysing COVID-19 case and death statistics using pandas and Matplotlib.
This project uses Python, Pandas, and Matplotlib to process COVID-19 data and create a line graph showing confirmed cases, deaths, and daily confirmed cases from **5 March to 12 June 2020**.

## Project Files

```text
covid19-data-visualisation/
├── covid_data.json
├── covid_visualisation.py
├── covid19_visualisation.png
└── README.md
```

### `covid_data.json`

Contains the COVID-19 data in JSON format, including:

* Date
* Total Confirmed Cases
* Total Deaths
* Total Recovered
* Active Cases
* Daily Confirmed Cases
* Daily Deaths

### `covid_visualisation.py`

Python script that:

1. Reads the JSON data.
2. Loads the data into a Pandas DataFrame.
3. Converts the dates into datetime values.
4. Converts numerical values into numeric data types.
5. Creates a line graph using Matplotlib.
6. Adds a title, axis labels, grid, and legend.
7. Saves the graph as `covid19_visualisation.png`.

### `covid19_visualisation.png`

The generated line graph showing the COVID-19 data over time.

## Requirements

The project requires:

* Python 3
* Pandas
* Matplotlib

## Installation

Python can be checked using:

```cmd
py --version
```

Install the required Python libraries with:

```cmd
py -m pip install pandas matplotlib
```

## Running the Project

Open Command Prompt or PowerShell and navigate to the project folder.


Then run:

```cmd
py covid_visualisation.py
```

The graph will be displayed and saved as:

```text
covid19_visualisation.png
```



## Visualisation

The graph compares three measures over time:

* **Total confirmed cases**
* **Total deaths**
* **Daily confirmed cases**

Because total confirmed cases are much larger than deaths and daily cases, the graph uses a shared numerical axis. This means the smaller values may appear compressed compared with total confirmed cases.

## Date Range

The dataset covers:

**5 March 2020 – 12 June 2020**

## Technologies Used

* **Python** — programming language
* **Pandas** — data processing and analysis
* **Matplotlib** — data visualisation
* **JSON** — data storage format

## How to Reproduce

To reproduce the visualisation:

1. Install Python 3.
2. Install Pandas and Matplotlib.
3. Place `covid_data.json` and `covid_visualisation.py` in the same folder.
4. Open a terminal in that folder.
5. Run:

```cmd
py covid_visualisation.py
```

The resulting visualisation will be saved as `covid19_visualisation.png`.
