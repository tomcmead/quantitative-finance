import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class QuantativeAnalysis:
    def __init__(self):
        return
     
    def get_hist_stock_prices(self, *tickers:str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yf.Ticker(ticker).history(period="5y")
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = ticker_data.Open.rename(ticker)             
                else:
                    market_data = pd.concat([market_data, ticker_data.Open], axis=1)
                    market_data.rename(columns={"Open": ticker}, inplace=True)   
        return market_data

    def get_hist_stock_volumes(self, *tickers:str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yf.Ticker(ticker).history(period="5y")
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = ticker_data.Volume.rename(ticker)             
                else:
                    market_data = pd.concat([market_data, ticker_data.Volume], axis=1)
                    market_data.rename(columns={"Volume": ticker}, inplace=True)   
        return market_data
    
    def get_hist_stock_dividends(self, *tickers:str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yf.Ticker(ticker).history(period="5y")
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = ticker_data.Dividends.rename(ticker)             
                else:
                    market_data = pd.concat([market_data, ticker_data.Dividends], axis=1)
                    market_data.rename(columns={"Dividends": ticker}, inplace=True)   
        return market_data
    
    def print_market_data(self, market_data:pd.DataFrame) -> None:
        if(not market_data.empty):
            plt.plot(market_data)
            plt.show()

    def generate_market_report(self, *tickers:str) -> None:
        stock_prices = self.get_hist_stock_prices(*tickers)
        stock_volumes = self.get_hist_stock_volumes(*tickers)
        stock_dividends = self.get_hist_stock_dividends(*tickers)

        html = '<!DOCTYPE html><html><body>'
        html += '<img src=\'data:image/png;base64,{}\'>'.format(self.__generate_market_figure(stock_prices))
        html += '<img src=\'data:image/png;base64,{}\'>'.format(self.__generate_market_figure(stock_volumes))
        html += '<img src=\'data:image/png;base64,{}\'>'.format(self.__generate_market_figure(stock_dividends))
        html += '</body></html>'
        with open('index.html', 'w') as f:
            f.write(html)

    def __generate_market_figure(self, market_data:pd.DataFrame) -> str:
        fig = plt.figure()
        plt.plot(market_data)
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return encoded