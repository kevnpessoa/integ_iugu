import script2 as iugu_api

#print(iugu_api.payment_token().text)

import requests

url = "https://api.iugu.com/v1/payment_token"

payload = {"account_id":"D8B1B481EBF240E08C6325D64C4CBB08","method":"credit_card","test":"true","data":{"number":"4111111111111111","verification_value":"123","first_name":"Kevin","last_name":"Pessoa","month":"10","year":"2020"}}
response = requests.request("POST", url, data=payload)

print(response.text)