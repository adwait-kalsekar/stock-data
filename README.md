# Stocks Data App

This is a full stack application that uses Django Framework for its backend, Django REST Framework for the data fetching API, Django Templates on the frontend, yFinance library to fetch stocks data and the D3.js library to display the data in form of graphs.

The application consists of the following pages:

1. Home Page - which gives a brief of the project and lists the features with some Lorem Ipsum Text

2. About Page - List more features and the tech stack used to build this project

3. Services Page - Gives details about what the project does

4. StockData Page (requires authentication) - Is a drop down menu with different stocks listed. When clicked on any stock, data is fetched from the database and provided to D3.js using an API, which show on the webpage

5. FetchData Page (requires authentication) - Presents different visualizations performed on the stock market data for Apple (AAPL) and Microsoft (MSFT)

6. Login / Register Pages - Django authentication implemented

## To setup the project:

1. In the current directory create a python virtual environment (make sure python is installed)

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

2. If everything goes right, the application will be available at `http://localhost:8000/` or `http://127.0.0.1:3000/`

3. Django Admin Panel will be available at `http://localhost:8000/admin` or `http://127.0.0.1:8000/admin`

### Login Credentials:

> Admin account:

- username -> admin
- password -> Admin1234

> Test account:

- username -> testuser
- password -> Test@123
