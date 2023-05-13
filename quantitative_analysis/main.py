import generate_market_reports as gm

def main():
    quant_analysis = gm.GenerateMarketReports()
    quant_analysis.generate_market_report("MSFT", "GOOG")
    return

if __name__ == "__main__":
    main()