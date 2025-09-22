# CORD-19 Data Explorer: A Python Data Analysis & Web App Project

---

## Overview

Welcome to the **CORD-19 Data Explorer**, a Python project that showcases data analysis, visualization, and interactive web application development. This project leverages a subset of the massive **COVID-19 Open Research Dataset (CORD-19)** to demonstrate a complete data science workflow, from data cleaning to deploying a user-friendly application with **Streamlit**.

---

## About the Author

**Tijani Ridwan Oluwaseun** 👋, an ND 2 student at **PLP Academy**. This project serves as a practical demonstration of my ability to **load, clean, analyze, and visualize real-world data**, culminating in the deployment of an interactive web application.

---

## Key Features

* 📊 **Interactive Data Filtering**: Filter research publications by **year** and **journal** directly within the web app.
* 📈 **Exploratory Data Analysis**: Easily identify the **top journals** and paper sources.
* ☁️ **Word Cloud Generation**: Visualize the most frequent words in paper titles.
* 🚀 **Interactive Web Application**: A full-fledged **Streamlit** app for a seamless data exploration experience.

---

## Dataset

* **Source**: [CORD-19 Dataset - Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
* **File Used**: `metadata_subset.csv`
* **Key Columns**:
    * `title`: The paper's title.
    * `authors`: The list of authors for the publication.
    * `journal`: The name of the journal where the paper was published.
    * `year`: The year of publication.
    * `source_x`: The source of the paper (e.g., ArXiv, PMC).

---

## Project Structure

.
├── app/
│   ├── app.py                     # Streamlit web application script
│   └── metadata_subset.csv        # The subset of the CORD-19 dataset
├── notebooks/
│   └── Week8_Frameworks_Assignment.ipynb  # Jupyter notebook for data analysis and exploration
└── requirements.txt               # Project's Python dependencies

---

## Getting Started

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/yourusername/Frameworks_Assignment.git](https://github.com/yourusername/Frameworks_Assignment.git)
    cd Frameworks_Assignment
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app**:
    ```bash
    streamlit run app/app.py
    ```

    The application will automatically open in your default browser.

---

## Tools Used

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-1A1A1A?style=flat&logo=seaborn&logoColor=white)
![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![WordCloud](https://img.shields.io/badge/WordCloud-5B5B5B?style=flat)