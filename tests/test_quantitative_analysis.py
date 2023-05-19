import pytest
import pandas as pd
import quantitative_analysis.quantitative_analysis as qa

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

def test_get_total_assets():
    quant_analysis = qa.QuantativeAnalysis()

    total_assets = quant_analysis.get_total_assets("MSFT", "GOOG")
    assert type(total_assets)==pd.DataFrame    
    assert list(total_assets.columns)==["MSFT", "GOOG"]

    total_assets = quant_analysis.get_total_assets("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(total_assets)==pd.Series    
    assert total_assets.empty

def test_get_total_debt():
    quant_analysis = qa.QuantativeAnalysis()

    total_debt = quant_analysis.get_total_debt("MSFT", "GOOG")
    assert type(total_debt)==pd.DataFrame    
    assert list(total_debt.columns)==["MSFT", "GOOG"]

    total_debt = quant_analysis.get_total_debt("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(total_debt)==pd.Series    
    assert total_debt.empty

def test_get_net_income():
    quant_analysis = qa.QuantativeAnalysis()

    net_income = quant_analysis.get_net_income("MSFT", "GOOG")
    assert type(net_income)==pd.DataFrame    
    assert list(net_income.columns)==["MSFT", "GOOG"]

    net_income = quant_analysis.get_net_income("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(net_income)==pd.Series
    assert net_income.empty

def test_get_total_revenue():
    quant_analysis = qa.QuantativeAnalysis()

    total_revenue = quant_analysis.get_total_revenue("MSFT", "GOOG")
    assert type(total_revenue)==pd.DataFrame    
    assert list(total_revenue.columns)==["MSFT", "GOOG"]

    total_revenue = quant_analysis.get_total_revenue("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(total_revenue)==pd.Series
    assert total_revenue.empty

def test_get_earnings_per_share():
    quant_analysis = qa.QuantativeAnalysis()

    earnings_per_share = quant_analysis.get_earnings_per_share("MSFT", "GOOG")
    assert type(earnings_per_share)==pd.DataFrame    
    assert list(earnings_per_share.columns)==["MSFT", "GOOG"]

    earnings_per_share = quant_analysis.get_earnings_per_share("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(earnings_per_share)==pd.Series
    assert earnings_per_share.empty

def test_get_total_liability():
    quant_analysis = qa.QuantativeAnalysis()

    total_liability = quant_analysis.get_total_liability("MSFT", "GOOG")
    assert type(total_liability)==pd.DataFrame    
    assert list(total_liability.columns)==["MSFT", "GOOG"]

    total_liability = quant_analysis.get_total_liability("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(total_liability)==pd.Series
    assert total_liability.empty

def test_get_free_cash_flow():
    quant_analysis = qa.QuantativeAnalysis()

    free_cash_flow = quant_analysis.get_free_cash_flow("MSFT", "GOOG")
    assert type(free_cash_flow)==pd.DataFrame    
    assert list(free_cash_flow.columns)==["MSFT", "GOOG"]

    free_cash_flow = quant_analysis.get_free_cash_flow("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(free_cash_flow)==pd.Series
    assert free_cash_flow.empty

def test_get_free_cash_flow():
    quant_analysis = qa.QuantativeAnalysis()

    change_in_cash = quant_analysis.get_change_in_cash("MSFT", "GOOG")
    assert type(change_in_cash)==pd.DataFrame    
    assert list(change_in_cash.columns)==["MSFT", "GOOG"]

    change_in_cash = quant_analysis.get_change_in_cash("FAKE_STOCK", "UNKOWN_STOCK")
    assert type(change_in_cash)==pd.Series
    assert change_in_cash.empty