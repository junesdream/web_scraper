import requests

# URL to check for IP
url = "http://ident.me/"

# Send of request via the proxy
page = requests.get(url)

print(page.text)
