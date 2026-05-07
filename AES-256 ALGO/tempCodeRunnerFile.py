import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=oi9lfOXrQWH8R8wTWxKDHzGbm2oGhEFJEmGoP0aT'
r = requests.get(url)
data = r.json()