# Tennis Data Engineering Project

This project builds a data pipeline for tennis match data using open-source tools.

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Improvements](#improvements)


## 🧠 Project Overview

This project builds a basic data pipeline for historical tennis match data from public datasets. The pipeline performs:
- Data ingestion from GitHub
- Cleaning and transformation
- Storage in local CSV format
- Simple stats like win/loss counts or surface performance


## ✨ Features
- 📥 Download ATP tennis match data from the web
- 🧹 Clean and transform raw data
- 🗃️ Save processed data for analysis
- 📊 Track player win/loss performance


## 🛠 Technologies Used

- Python
- Pandas
- Requests
- PostgreSQL (optional)
- Streamlit (for future dashboard)
- Git & GitHub


## Project Structure

tennis-data-engineering/
├── data/
│ ├── raw/ # Raw CSVs
│ └── processed/ # Cleaned CSVs
├── notebooks/ # Jupyter Notebooks (for EDA)
├── src/
│ ├── ingestion.py # Downloads raw data
│ ├── transformation.py # Cleans/transforms data
│ └── utils.py # Helper functions
├── .gitignore
├── README.md
├── requirements.txt


## Getting Started
