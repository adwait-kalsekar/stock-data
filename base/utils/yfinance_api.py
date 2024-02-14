import yfinance as yf

def get_historic_data(symbol):

    data = yf.Ticker(symbol)

    # get historical market data
    return data.history(period="1mo")