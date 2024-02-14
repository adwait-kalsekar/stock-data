from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("services/", views.services_page, name="services"),
    path("stockdata/<str:symbol>", views.get_stock_data, name="stockdata"),
    path("presenting/", views.data_presenting_page, name="presenting"),
    path("fetchdata/", views.refresh_stock_data, name="fetchdata"),

    path('<path:all_paths>/', views.error_page, name="error"),
]
