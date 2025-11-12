import requests
API_KEY = "51caf20ce201fe2a05577411f3b556bdf45712c60ba66b396ae9c25e660032f6"

bitcoin = float(input("How many bitcoins do you want to buy?"))

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apikey="+API_KEY)
