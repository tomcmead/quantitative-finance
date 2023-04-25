import pytest
import pandas as pd
from quantitative_analysis import quantitative_analysis as qa

def test_get_hist_stock_prices():
    quant_analysis = qa.QuantativeAnalysis()
    assert type(quant_analysis.get_hist_stock_prices("MSFT", "GOOG")[0])==pd.Series
    assert type(quant_analysis.get_hist_stock_prices("MSFT", "GOOG"))==list
    assert quant_analysis.get_hist_stock_prices("Not_Real", "Fake_Stock")==[]

def test_get_hist_stock_volumes():
    quant_analysis = qa.QuantativeAnalysis()
    assert type(quant_analysis.get_hist_stock_volumes("MSFT", "GOOG")[0])==pd.Series
    assert type(quant_analysis.get_hist_stock_volumes("MSFT", "GOOG"))==list
    assert quant_analysis.get_hist_stock_volumes("Not_Real", "Fake_Stock")==[]   