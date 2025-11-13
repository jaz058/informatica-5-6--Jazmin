import requests
import json
print(("🩷 🧡 ")*9)

product = (input("What is the product you are searching for??"))
free_list=
free=(input("What type of free are you looking for?"))
response =  requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline")
look = (response.json()["name"]["product_type"]["description"])
print("Your pruduct is :"{look})
