
import requests
import sys
import json

#Check for number of bitcoin as command-line argument
if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

else:
    try:
      num = float(sys.argv[1])
    except:
      sys.exit('Command-line argument is not a number')

# Calcuate the amount
try:


  response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")

  res = response.json()

  rate = res['bpi']['USD']['rate_float']

  amt = num * rate
  print(f"${amt:,.4f}")

except requests.RequestException:
   sys.exit('RequestException')