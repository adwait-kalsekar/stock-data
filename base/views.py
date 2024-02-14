from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize

from .models import StockData
from .utils import format_date, yfinance_api

# Create your views here.
stocks = ["AAPL", "MSFT", "DIS", "SBUX", "NKE"]

def home_page(request):
    return render(request, "base/home.html")

def about_page(request):
    return render(request, "base/about.html")

def services_page(request):
    return render(request, "base/services.html")

def data_presenting_page(request):
    return render(request, "base/data_presenting.html")


@login_required(login_url="login")
def get_stock_data(request, symbol):
    context = { "symbol": symbol }
    return render(request, "base/stock_data.html", context)
    

@login_required(login_url="login")
def refresh_stock_data(request):
    try:
        StockData.objects.all().delete()
        for stock in stocks:
            fetch_data_and_store_handler(stock)

        return render(request, "base/fetch_data.html", {})
    
    except Exception as err:
        print(err)
        context = { "message": "Could not refresh from yFinance API" }
        return render(request, "base/error.html", context)
    
def fetch_data_and_store_handler(symbol):
    results = yfinance_api.get_historic_data(symbol)

    try:
        for i in range(len(results)):
            stock_data_model = StockData(
                symbol=symbol,
                date = results.index[i],
                open = results.iloc[i]["Open"],
                close = results.iloc[i]["Close"],
                high = results.iloc[i]["High"],
                low = results.iloc[i]["Low"],
                volume = results.iloc[i]["Volume"]
            )
            stock_data_model.save()
        
        return results
    
    except Exception as err:
        raise err 
    
def error_page(request, all_paths=""):
    context = {"message": "Page does not exist"}
    return render(request, "base/error.html", context)