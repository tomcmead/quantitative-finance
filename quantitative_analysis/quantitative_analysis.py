import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import yahooquery as yd
import base64
from io import BytesIO

class QuantativeAnalysis:
    def __init__(self):

        # symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']
        # faang = yd.Ticker(symbols)
        # types = ['TotalDebt', 'TotalAssets']
        
        # print(faang.get_financial_data(types, trailing=False))

        return
    
    def get_balance_sheet(self, *tickers:str) -> None:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yd.Ticker(ticker).get_financial_data('TotalAssets')
            if ticker_data.empty:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = pd.DataFrame(index=[str(ticker_data.asOfDate[i])[0:4] for i in range(len(ticker_data))],
                                               data=[str(ticker_data.TotalAssets[i]) for i in range(len(ticker_data))],
                                               columns=[ticker]).rename_axis('Year') 
                else:
                    market_data_temp = pd.DataFrame(index=[str(ticker_data.asOfDate[i])[0:4] for i in range(len(ticker_data))],
                                               data=[str(ticker_data.TotalAssets[i]) for i in range(len(ticker_data))],
                                               columns=[ticker]).rename_axis('Year') 
                    market_data = pd.concat([market_data, market_data_temp], axis=1)            
        return market_data


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

        fig, axs = plt.subplots(3, 1, constrained_layout=True, figsize=(12, 15))
        axs[0].set_title('Stock Prices')
        axs[0].set_ylabel('Stock Price ($)')
        axs[0].plot(stock_prices)

        axs[1].set_title('Stock Volumes')
        axs[1].set_ylabel('Stock Volume')
        axs[1].plot(stock_volumes)
        
        axs[2].set_title('Stock Dividends')
        axs[2].set_ylabel('Stock Dividend ($)')
        axs[2].plot(stock_dividends)

        [axs[i].set_xlabel('Year') for i in range(len(axs))]
        [axs[i].legend(list(tickers), loc='best') for i in range(len(axs))]

        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
 
        html = '<!DOCTYPE html><html><body>'
        html += '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
        html += '</body></html>'
        with open('index.html', 'w') as f:
            f.write(html)