import yfinance as yf
import pandas as pd
import yahooquery as yd

class QuantativeAnalysis:
    def get_total_assets(self, *tickers:str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yd.Ticker(ticker).get_financial_data('TotalAssets')
            if type(ticker_data)==str:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = pd.DataFrame(index=[str(ticker_data.asOfDate[i])[0:4] for i in range(len(ticker_data))],
                                               data=[ticker_data.TotalAssets[i] for i in range(len(ticker_data))],
                                               columns=[ticker]).rename_axis('Year')               
                else:
                    market_data_temp = pd.DataFrame(index=[str(ticker_data.asOfDate[i])[0:4] for i in range(len(ticker_data))],
                                                    data=[ticker_data.TotalAssets[i] for i in range(len(ticker_data))],
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

    def get_total_debt(self, *tickers:str) -> pd.DataFrame:
        market_data = pd.Series([])
        for ticker in tickers:
            ticker_data = yd.Ticker(ticker).get_financial_data('TotalDebt')
            if type(ticker_data)==str:
                print(f"Error: {ticker} not found and excluded")
            else:
                if market_data.empty:
                    market_data = pd.DataFrame(index=[str(ticker_data.asOfDate[i])[0:4] for i in range(len(ticker_data))],
                                               data=[ticker_data.TotalDebt[i] for i in range(len(ticker_data))],
                                               columns=[ticker]).rename_axis('Year')               
                else:
                    market_data_temp = pd.DataFrame(index=[str(ticker_data.asOfDate[i])[0:4] for i in range(len(ticker_data))],
                                                    data=[ticker_data.TotalDebt[i] for i in range(len(ticker_data))],
                                                    columns=[ticker]).rename_axis('Year') 
                    market_data = pd.concat([market_data, market_data_temp], axis=1)            
        return market_data