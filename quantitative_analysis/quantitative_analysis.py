import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class QuantativeAnalysis:
    def __init__(self):
        return
    
    def get_hist_stock_prices(self, *tickers: str) -> list[pd.DataFrame]:
        market_data = self.__get_stock_data(tickers)
        return [(stock.High+stock.Low)/2 for stock in market_data]
        # High, Low, Open, Close, Volume, Dividends
    
    def get_hist_stock_volumes(self, *tickers: str) -> list[pd.DataFrame]:
        market_data = self.__get_stock_data(tickers)
        return [stock.Volume for stock in market_data]
     
    def __get_stock_data(self, tickers: list[str]) -> list[pd.DataFrame]:
        market_data = []
        for ticker in tickers:
            ticker_data = yf.Ticker(ticker).history(period="1mo")
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                market_data.append(ticker_data)
        return market_data
