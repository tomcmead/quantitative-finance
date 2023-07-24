import quantitative_analysis.quantitative_analysis as qa
import matplotlib.pyplot as plt
import matplotlib.figure
import pandas as pd
from scipy.interpolate import make_interp_spline
import numpy as np
import base64
from io import BytesIO

class GenerateMarketReports:
    def __init__(self):
        self.quant_analysis = qa.QuantativeAnalysis

    def __smooth_data(self, market_data:pd.DataFrame, *tickers:str) -> tuple[np.ndarray, list[np.ndarray]]:
        index=[i for i in market_data.index]
        index_new = np.linspace(max(index), min(index), 300)
        smooth_data = []
        for ticker in tickers:
            data = [i for i in market_data[ticker].values]
            spl = make_interp_spline(index, data, k=3)
            smooth_data.append(spl(index_new))
        return index_new, smooth_data
    
    def __generate_chart_image(self, fig:matplotlib.figure.Figure, axs:np.ndarray, *tickers:str) -> str:
        [axs[i].set_xlabel('Year') for i in range(len(axs))]
        [axs[i].legend(list(tickers), loc='best') for i in range(len(axs))]
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded_png = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return encoded_png
    
    def generate_market_report(self, *tickers:str) -> None:
        # Stock Data
        stock_prices = self.quant_analysis.get_hist_stock_prices(None, *tickers)
        stock_volumes = self.quant_analysis.get_hist_stock_volumes(None, *tickers)
        stock_dividends = self.quant_analysis.get_hist_stock_dividends(None, *tickers)

        fig, axs = plt.subplots(3, 1, constrained_layout=True, figsize=(12, 20))
        axs[0].set_title('Stock Prices')
        axs[0].set_ylabel('Stock Price ($)')
        axs[0].plot(stock_prices)

        axs[1].set_title('Stock Volumes')
        axs[1].set_ylabel('Stock Volume')
        axs[1].plot(stock_volumes)
        
        axs[2].set_title('Stock Dividends')
        axs[2].set_ylabel('Stock Dividend ($)')
        axs[2].plot(stock_dividends)

        stock_data_png = self.__generate_chart_image(fig, axs, *tickers)

        # Income Statement
        total_revenue = self.quant_analysis.get_total_revenue(None, *tickers)
        net_income = self.quant_analysis.get_net_income(None, *tickers)
        earnings_per_share = self.quant_analysis.get_earnings_per_share(None, *tickers)

        fig, axs = plt.subplots(3, 1, constrained_layout=True, figsize=(12, 20))

        axs[0].set_title('Net Income')
        axs[0].set_ylabel('Net Income ($)')
        x, y = self.__smooth_data(net_income, *tickers)
        [axs[0].plot(x,y_) for y_ in y]

        axs[1].set_title('Total Revenue')
        axs[1].set_ylabel('Total Revenue ($)')
        x, y = self.__smooth_data(total_revenue, *tickers)
        [axs[1].plot(x,y_) for y_ in y]

        axs[2].set_title('Earnings per Share')
        axs[2].set_ylabel('Earnings per Share')
        x, y = self.__smooth_data(earnings_per_share, *tickers)
        [axs[2].plot(x,y_) for y_ in y]

        [axs[i].set_xticks(np.arange(min(x), max(x)+1, 1)) for i in range(len(axs))]
        income_statement_png = self.__generate_chart_image(fig, axs, *tickers)

        # Balance Sheet
        total_assets = self.quant_analysis.get_total_assets(None, *tickers)
        total_liability = self.quant_analysis.get_total_liability(None, *tickers)
        total_debt = self.quant_analysis.get_total_debt(None, *tickers)
        book_value = self.quant_analysis.get_book_value(None, *tickers)

        fig, axs = plt.subplots(4, 1, constrained_layout=True, figsize=(12, 20))

        axs[0].set_title('Total Assets')
        axs[0].set_ylabel('Total Assets ($)')
        x, y = self.__smooth_data(total_assets, *tickers)
        [axs[0].plot(x,y_) for y_ in y]

        axs[1].set_title('Total Debt')
        axs[1].set_ylabel('Total Debt ($)')
        x, y = self.__smooth_data(total_debt, *tickers)
        [axs[1].plot(x,y_) for y_ in y]

        axs[2].set_title('Total Liability')
        axs[2].set_ylabel('Total Liability ($)')
        x, y = self.__smooth_data(total_liability, *tickers)
        [axs[2].plot(x,y_) for y_ in y]

        axs[3].set_title('Book Value')
        axs[3].set_ylabel('Book Value ($)')
        x, y = self.__smooth_data(book_value, *tickers)
        [axs[3].plot(x,y_) for y_ in y]

        [axs[i].set_xticks(np.arange(min(x), max(x)+1, 1)) for i in range(len(axs))]
        balance_sheet_png = self.__generate_chart_image(fig, axs, *tickers)

        # Cash Flow
        change_in_cash = self.quant_analysis.get_change_in_cash(None, *tickers)
        free_cash_flow = self.quant_analysis.get_free_cash_flow(None, *tickers) 

        fig, axs = plt.subplots(2, 1, constrained_layout=True, figsize=(12, 20))

        axs[0].set_title('Free Cash Flow')
        axs[0].set_ylabel('Free Cash Flow ($)')
        x, y = self.__smooth_data(free_cash_flow, *tickers)
        [axs[0].plot(x,y_) for y_ in y]

        axs[1].set_title('Change in Cash')
        axs[1].set_ylabel('Change in Cash ($)')
        x, y = self.__smooth_data(change_in_cash, *tickers)
        [axs[1].plot(x,y_) for y_ in y]
        
        [axs[i].set_xticks(np.arange(min(x), max(x)+1, 1)) for i in range(len(axs))]
        cash_flow_png = self.__generate_chart_image(fig, axs, *tickers)               
 
        html = '<!DOCTYPE html><html><style>h1{color: black;font-family: Tahoma, sans-serif;font-size: 2.5em;}</style>'
        html += '<h1>Stock Data</h1>'
        html += '<img src=\'data:image/png;base64,{}\'>'.format(stock_data_png)
        html += '<h1>Income Statement</h1>'
        html += '<img src=\'data:image/png;base64,{}\'>'.format(income_statement_png)
        html += '<h1>Balance Sheet</h1>'
        html += '<img src=\'data:image/png;base64,{}\'>'.format(balance_sheet_png)
        html += '<h1>Cash Flow</h1>'
        html += '<img src=\'data:image/png;base64,{}\'>'.format(cash_flow_png)
        html += '</html>'
        with open('index.html', 'w') as f:
            f.write(html)