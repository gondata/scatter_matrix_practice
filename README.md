# Correlation Analysis of Financial Data

This Python code analyzes financial data by calculating the correlation matrix and generating a scatter plot matrix of the returns for a set of given assets.

## Getting the Data

This code uses **`yfinance`** and **`pandas_datareader`** to retrieve financial data from Yahoo Finance. The tickers of the assets, start and end dates, and the range of data required can be customized according to the user's requirements.

## Calculating Returns

Using the data retrieved, the daily percentage change of the assets is calculated using the **`pct_change()`** method. The first row, which contains NaN values, is then removed from the dataframe.

## Generating the Scatter Plot Matrix

The correlation matrix is then calculated using the **`corr()`** method. The correlation between the returns of each asset is then plotted in the scatter plot matrix using **`scatter_matrix()`**.

## Requirements

This code requires the following Python libraries to be installed:

- pandas
- numpy
- yfinance
- matplotlib

These libraries can be installed by running the following command:

```

pip install -r requirements.txt

```

## Running the Code

To run the code, simply clone the repository and execute the script. You can customize the tickers, start date, and end date to suit your requirements.
