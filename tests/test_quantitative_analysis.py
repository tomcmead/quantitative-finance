import pytest
import pandas as pd
import quantitative_analysis.quantitative_analysis as qa

def test_get_total_assets():
    quant_analysis = qa.QuantativeAnalysis()

    total_assets = quant_analysis.get_total_assets("MSFT", "GOOG")
    assert type(total_assets)==pd.DataFrame    
    assert list(total_assets.columns)==["MSFT", "GOOG"]

    total_assets = quant_analysis.get_total_assets("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(total_assets)==pd.Series    
    assert total_assets.empty

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

def test_get_total_debt():
    quant_analysis = qa.QuantativeAnalysis()

    total_debt = quant_analysis.get_total_debt("MSFT", "GOOG")
    assert type(total_debt)==pd.DataFrame    
    assert list(total_debt.columns)==["MSFT", "GOOG"]

    total_debt = quant_analysis.get_total_debt("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(total_debt)==pd.Series    
    assert total_debt.empty