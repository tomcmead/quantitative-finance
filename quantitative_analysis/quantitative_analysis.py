import yfinance as yf
import pandas as pd
import yahooquery as yd

def yahoo_query_handler(ticker_data, target_data):
    market_data = pd.Series([])
    min_year = 3000
    max_year = 0
    for idx, data in enumerate(ticker_data):
        if(type(data) == str):
            print(f"Error: ticker {idx} not found and excluded")
        else:
            min_year = min(min_year, int(str(data.asOfDate[0])[0:4]))
            max_year = max(max_year, int(str(data.asOfDate[len(data)-1])[0:4]))        
        
    for idx,data in enumerate(ticker_data):
        years = []
        data_temp = []
        for date in data.asOfDate:
            years.append(int(str(date)[0:4]))
        year = min_year
        while(year<years[0]):
            data_temp.append(0)
            year += 1
        for val in target_data[idx]:
            data_temp.append(val)
            year += 1
        while(year<=max_year):
            data_temp.append(data_temp[len(data)-1])
            year += 1

        market_data_temp = pd.DataFrame(index=[year for year in range(min_year, max_year+1, 1)],
                                            data=[val for val in data_temp],
                                            columns=[ticker_data[idx].head().index.values[0]]).rename_axis('Year')
        if idx==0:
            market_data = market_data_temp                
        else:
            market_data = pd.concat([market_data, market_data_temp], axis=1)
    return market_data

class QuantativeAnalysis:    
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

    def get_total_revenue(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        total_revenue = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('TotalRevenue', trailing=False)
            if(type(data) == str):
                print(f"Error: total revenue for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].TotalRevenue[row] for row in range(len(data))]
                total_revenue.append(data)
        return yahoo_query_handler(ticker_data, total_revenue)
    
    def get_net_income(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        net_income = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('NetIncome', trailing=False)
            if(type(data) == str):
                print(f"Error: net income for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].NetIncome[row] for row in range(len(data))]
                net_income.append(data)
        return yahoo_query_handler(ticker_data, net_income)

    def get_earnings_per_share(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        eps_data = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('BasicEPS', trailing=False)
            if(type(data) == str):
                print(f"Error: earnings per share for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].BasicEPS[row] for row in range(len(data))]
                eps_data.append(data)
        return yahoo_query_handler(ticker_data, eps_data)
    
    def get_total_assets(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        total_assets = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('TotalAssets', trailing=False)
            if(type(data) == str):
                print(f"Error: total assets for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].TotalAssets[row] for row in range(len(data))]
                total_assets.append(data)
        return yahoo_query_handler(ticker_data, total_assets)
    
    def get_total_liability(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        total_liability = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('TotalLiabilitiesNetMinorityInterest', trailing=False)
            if(type(data) == str):
                print(f"Error: total liability for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].TotalLiabilitiesNetMinorityInterest[row] for row in range(len(data))]
                total_liability.append(data)
        return yahoo_query_handler(ticker_data, total_liability)
    
    def get_total_debt(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        total_debt = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('TotalDebt', trailing=False)
            if(type(data) == str):
                print(f"Error: total debt for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].TotalDebt[row] for row in range(len(data))]
                total_debt.append(data)
        return yahoo_query_handler(ticker_data, total_debt)
    
    def get_free_cash_flow(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        free_cash_flow = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('FreeCashFlow', trailing=False)
            if(type(data) == str):
                print(f"Error: free cash flow for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].FreeCashFlow[row] for row in range(len(data))]
                free_cash_flow.append(data)
        return yahoo_query_handler(ticker_data, free_cash_flow)

    def get_change_in_cash(self, *tickers:str) -> pd.DataFrame:
        ticker_data = []
        change_in_cash = []
        for idx, ticker in enumerate(tickers):
            data = yd.Ticker(ticker).get_financial_data('ChangeInCashSupplementalAsReported', trailing=False)
            if(type(data) == str):
                print(f"Error: change in cash for ticker {ticker} not found and excluded")
            else:
                ticker_data.append(data)
                data = [ticker_data[idx].ChangeInCashSupplementalAsReported[row] for row in range(len(data))]
                change_in_cash.append(data)
        return yahoo_query_handler(ticker_data, change_in_cash)