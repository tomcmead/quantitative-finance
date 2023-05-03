import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class QuantativeAnalysis:
    def __init__(self):
        return
     
    def get_hist_stock_prices(self, *tickers: str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yf.Ticker(ticker).history(period="1mo")
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = ticker_data.Open.rename(ticker)             
                else:
                    market_data = pd.concat([market_data, ticker_data.Open], axis=1)
                    market_data.rename(columns={"Open": ticker}, inplace=True)   
        return market_data

    def get_hist_stock_volumes(self, *tickers: str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yf.Ticker(ticker).history(period="1mo")
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = ticker_data.Volume.rename(ticker)             
                else:
                    market_data = pd.concat([market_data, ticker_data.Volume], axis=1)
                    market_data.rename(columns={"Volume": ticker}, inplace=True)   
        return market_data
    
    def get_hist_stock_dividends(self, *tickers: str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yf.Ticker(ticker).history(period="1mo")
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = ticker_data.Dividends.rename(ticker)             
                else:
                    market_data = pd.concat([market_data, ticker_data.Dividends], axis=1)
                    market_data.rename(columns={"Dividends": ticker}, inplace=True)   
        return market_data