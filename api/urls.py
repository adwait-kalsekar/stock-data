from django.urls import path

from .views import StockDataView, CheckHealth

urlpatterns = [
    path("check_health/", CheckHealth.as_view() ),
    path("get_stock_data/<str:symbol>/", StockDataView.as_view()),
]