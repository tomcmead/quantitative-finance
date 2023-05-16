import quantitative_analysis.quantitative_analysis as qa
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class GenerateMarketReports:
    def __init__(self):
        self.quant_analysis = qa.QuantativeAnalysis
    
    def generate_market_report(self, *tickers:str) -> None:
        stock_prices = self.quant_analysis.get_hist_stock_prices(None, *tickers)
        stock_volumes = self.quant_analysis.get_hist_stock_volumes(None, *tickers)
        stock_dividends = self.quant_analysis.get_hist_stock_dividends(None, *tickers)
        total_assets = self.quant_analysis.get_total_assets(None, *tickers)
        total_debt = self.quant_analysis.get_total_debt(None, *tickers)

        fig, axs = plt.subplots(5, 1, constrained_layout=True, figsize=(12, 15))
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
        axs[3].plot(total_assets)

        axs[4].set_title('Total Debt')
        axs[4].set_ylabel('Total Debt ($)')
        axs[4].plot(total_debt)

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