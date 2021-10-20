import requests
r=requests.get("https://www.google.com")
r.status_code
r.headers

r.headers["Date"]

r.text