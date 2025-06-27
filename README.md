# 🌍 Global Air Pollution Dashboard using Preswald

An interactive, visual data dashboard built with **Preswald** and **Plotly** to explore global PM2.5 air pollution data. This tool allows users to analyze pollution levels by country and city, visualize year-wise and geographic trends, and filter the data using sliders and SQL-like queries.

---

## 📽️ Demo Video

🎥 [Click to Watch Demo](assets/demo.mp4)

> If video doesn't autoplay, download and watch from the `assets/` folder.

---

## 🖼️ Screenshots

### 🏠 Dashboard Home
![Dashboard Home](assets/dashboard_home.png)

### 🎛️ PM2.5 Filter Using Slider
![Filter Slider](assets/filter_slider.png)

### 🌍 Geo Map of Pollution Points
![Map View](assets/map_view.png)

---

## 📦 Features

- ✅ Interactive slider to filter data based on PM2.5 levels
- 📊 Summary tables grouped by country
- 🧮 SQL-like querying (e.g., filter for PM2.5 > 100)
- 🌍 World map plotting PM2.5 values with city-level details
- 📈 Year-wise trend line (if year data exists)
- 📥 Export your dashboard as a static **PDF or HTML report**

---

## 🔧 Tech Stack

- [Preswald](https://preswald.ai) – for building interactive data apps
- [Plotly Express](https://plotly.com/python/plotly-express/) – for charts and maps
- [Pandas](https://pandas.pydata.org/) – data manipulation
- Python 3.10+

---

## 📁 Dataset Used

## Cleaned version of air pollution dataset with the following columns:
Country, City, AQI Value, AQI Category,
CO AQI Value, Ozone AQI Value, NO2 AQI Value,
PM2.5 AQI Value, Latitude, Longitude, Year

## install Preswald manually:
pip install preswald

## Run the app locally
preswald run
Open http://localhost:8501 in your browser.

##  Export as PDF/HTML report

preswald export --format pdf
# or
preswald export --format html

## ⚠️ Ensure playwright is installed:
pip install playwright && playwright install

## 📜 Project Structure

├── assets/
│   ├── dashboard_home.png
│   ├── filter_slider.png
│   ├── map_view.png
│   └── demo.mp4
├── hello.py              # Main Preswald app
├── preswald.toml         # App config
├── data/
│   └── air_pollution.csv
├── requirements.txt
└── README.md


## 🙋‍♀️ Author
Amritanshu Sinha
B.Tech, Computer Engineering
National Institute of Technology, Kurukshetra
GitHub

## ⭐️ Give a Star
If you found this project useful, consider giving it a ⭐️ to support the work.






