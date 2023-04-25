import quantitative_analysis as qa
import matplotlib.pyplot as plt

def main():
    quant_analysis = qa.QuantativeAnalysis()
    hist_stock_price = quant_analysis.get_hist_stock_prices("MSFT", "GOOG")
    return

if __name__ == "__main__":
    main()