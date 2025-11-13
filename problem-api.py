import requests
import json
print(("🩷 "*25))

product = (input("What is the product you are searching for??"))
response =  requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline")
look =