import requests
import json

#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://api.iugu.com/v1/"
ACCOUNT_ID = "D8B1B481EBF240E08C6325D64C4CBB08"
#TOKEN = 'e022d466b0b445ec68c65470f3af7019'

headers = { "content-type" : "application/json" }

def payment_token(data):
    payload = {"account_id": ACCOUNT_ID, "method": "credit_card", "test":"true", "data": data }
    response = requests.post(URL + "payment_token", data=json.dumps(payload), headers=headers).json()
    return response

def charge(data):
    token_response = payment_token(data['credit_card'])
    #return token_response
    #if token_response["status_code"] != 200:
    #    return 'Erro ao buscar token de autenticação'
    headers = { #"content-type" : "application/json", 
                "Accept": 'application/json',
                "Content-Type": 'application/json; charset=UTF-8',
                "Authorization": token_response["id"] }
 
    payload = {
        #"method": "credit_card",
        "token": "e022d466b0b445ec68c65470f3af7019",#token_response["id"],
        "email": data['email'],
        #"months": data['months'],
        "items": data['items'],
        "payer":{}
    }
    #return json.dumps(payload);
    payload = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    #return payload
    return requests.post(URL + "charge", data=payload, headers=headers).json()