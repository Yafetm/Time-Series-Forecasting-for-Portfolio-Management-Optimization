# Time Series Forecasting for Portfolio Management Optimization

## Overview
This project is part of the 10 Academy Week 11 Challenge. The goal is to apply time series forecasting techniques to historical financial data to enhance portfolio management strategies for **GMF Investments**.

The project covers:
- Data extraction from Yahoo Finance using `yfinance`
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Time series forecasting with ARIMA/SARIMA and LSTM
- Portfolio optimization using Modern Portfolio Theory
- Backtesting the strategy

## Data
Assets analyzed:
- **Tesla (TSLA)** – High growth, high risk
- **Vanguard Total Bond Market ETF (BND)** – Stability, low risk
- **S&P 500 ETF (SPY)** – Diversified, moderate risk

Period: **2015-07-01 to 2025-07-31**

## Repository Structure
├── data/ # Downloaded CSV files for TSLA, BND, SPY
├── notebooks/ # Jupyter notebooks for EDA and modeling
├── scripts/ # Python scripts for data fetching and processing
├── plots/ # Generated visualizations
├── requirements.txt # Python dependencies
└── README.md # Project documentation