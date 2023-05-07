import pytest
import pandas as pd
import os
from quantitative_analysis import quantitative_analysis as qa

def test_get_hist_stock_prices():
    quant_analysis = qa.QuantativeAnalysis()

    stock_prices = quant_analysis.get_hist_stock_prices("MSFT", "GOOG")
    assert type(stock_prices)==pd.DataFrame    
    assert list(stock_prices.columns)==["MSFT", "GOOG"]

    stock_prices = quant_analysis.get_hist_stock_prices("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(stock_prices)==pd.Series    
    assert stock_prices.empty

def test_get_hist_stock_volumes():
    quant_analysis = qa.QuantativeAnalysis()

    stock_volumes = quant_analysis.get_hist_stock_volumes("MSFT", "GOOG")
    assert type(stock_volumes)==pd.DataFrame    
    assert list(stock_volumes.columns)==["MSFT", "GOOG"]

    stock_volumes = quant_analysis.get_hist_stock_volumes("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(stock_volumes)==pd.Series    
    assert stock_volumes.empty

def test_get_hist_stock_dividends():
    quant_analysis = qa.QuantativeAnalysis()

    stock_dividends = quant_analysis.get_hist_stock_dividends("MSFT", "GOOG")
    assert type(stock_dividends)==pd.DataFrame    
    assert list(stock_dividends.columns)==["MSFT", "GOOG"]

    stock_dividends = quant_analysis.get_hist_stock_dividends("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(stock_dividends)==pd.Series    
    assert stock_dividends.empty

def test_generate_market_report():
    os.system("rm index.html")
    quant_analysis = qa.QuantativeAnalysis()
    quant_analysis.generate_market_report("MSFT", "GOOG")
    assert os.path.exists("index.html") == True