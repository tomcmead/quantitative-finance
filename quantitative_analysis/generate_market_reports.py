import quantitative_analysis.quantitative_analysis as qa
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import make_interp_spline
import numpy as np
import base64
from io import BytesIO

class GenerateMarketReports:
    def __init__(self):
        self.quant_analysis = qa.QuantativeAnalysis

    def __smooth_data(self, market_data:pd.DataFrame, *tickers:str):
        index=[i for i in market_data.index]
        index_new = np.linspace(max(index), min(index), 300)
        smooth_data = []
        for ticker in tickers:
            data = [i for i in market_data[ticker].values]
            spl = make_interp_spline(index, data, k=3)
            smooth_data.append(spl(index_new))
        return index_new, smooth_data
    
    def generate_market_report(self, *tickers:str) -> None:
        stock_prices = self.quant_analysis.get_hist_stock_prices(None, *tickers)
        stock_volumes = self.quant_analysis.get_hist_stock_volumes(None, *tickers)
        stock_dividends = self.quant_analysis.get_hist_stock_dividends(None, *tickers)
        total_assets = self.quant_analysis.get_total_assets(None, *tickers)
        total_debt = self.quant_analysis.get_total_debt(None, *tickers)
        net_income = self.quant_analysis.get_net_income(None, *tickers)
        total_revenue = self.quant_analysis.get_total_revenue(None, *tickers)
        earnings_per_share = self.quant_analysis.get_earnings_per_share(None, *tickers)
        total_liability = self.quant_analysis.get_total_liability(None, *tickers)
        free_cash_flow = self.quant_analysis.get_free_cash_flow(None, *tickers)

        fig, axs = plt.subplots(10, 1, constrained_layout=True, figsize=(12, 26))
        axs[0].set_title('Stock Prices')
        axs[0].set_ylabel('Stock Price ($)')
        axs[0].plot(stock_prices)

        axs[1].set_title('Stock Volumes')
        axs[1].set_ylabel('Stock Volume')
        axs[1].plot(stock_volumes)
        
        axs[2].set_title('Stock Dividends')
        axs[2].set_ylabel('Stock Dividend ($)')
        axs[2].plot(stock_dividends)

        axs[3].set_title('Total Assets')
        axs[3].set_ylabel('Total Assets ($)')
        x, y = self.__smooth_data(total_assets, *tickers)
        [axs[3].plot(x,data) for data in y]

        axs[4].set_title('Total Debt')
        axs[4].set_ylabel('Total Debt ($)')
        x, y = self.__smooth_data(total_debt, *tickers)
        [axs[4].plot(x,data) for data in y]

        axs[5].set_title('Net Income')
        axs[5].set_ylabel('Net Income ($)')
        x, y = self.__smooth_data(net_income, *tickers)
        [axs[5].plot(x,data) for data in y]

        axs[6].set_title('Total Revenue')
        axs[6].set_ylabel('Total Revenue ($)')
        x, y = self.__smooth_data(total_revenue, *tickers)
        [axs[6].plot(x,data) for data in y]

        axs[7].set_title('Earnings per Share')
        axs[7].set_ylabel('Earnings per Share')
        x, y = self.__smooth_data(earnings_per_share, *tickers)
        [axs[7].plot(x,data) for data in y]

        axs[8].set_title('Total Liability')
        axs[8].set_ylabel('Total Liability ($)')
        x, y = self.__smooth_data(total_liability, *tickers)
        [axs[8].plot(x,data) for data in y]

        axs[9].set_title('Free Cash Flow')
        axs[9].set_ylabel('Free Cash Flow ($)')
        x, y = self.__smooth_data(free_cash_flow, *tickers)
        [axs[9].plot(x,data) for data in y]

        [axs[i].set_xlabel('Year') for i in range(len(axs))]
        [axs[i].legend(list(tickers), loc='best') for i in range(len(axs))]
        [axs[i].set_xticks(np.arange(min(x), max(x)+1, 1)) for i in range(3,len(axs))]        

        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
 
        html = '<!DOCTYPE html><html><body>'
        html += '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
        html += '</body></html>'
        with open('index.html', 'w') as f:
            f.write(html)