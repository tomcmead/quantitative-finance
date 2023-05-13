import pytest
import os
import quantitative_analysis.generate_market_reports as gm

def test_generate_market_report():
    os.system("rm index.html")
    assert os.path.exists("index.html") == False
    market_reports = gm.GenerateMarketReports()
    market_reports.generate_market_report("MSFT", "GOOG")
    assert os.path.exists("index.html") == True