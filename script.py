import requests

URL = "https://api.iugu.com/v1/"
ACCOUNT_ID = 'D8B1B481EBF240E08C6325D64C4CBB08'
#TOKEN = 'e022d466b0b445ec68c65470f3af7019'
TOKEN = '39B1841C-3940-49D5-9F5FA2596755629D'

def payment_token():
    url = URL + "payment_token"
    data = {'account_id': ACCOUNT_ID, 'method': 'credit_card', 'test': 'true'}

    return requests.post(url, data = data)

def charge( data ):
    url = URL + "charge"
    #data = {'account_id': ACCOUNT_ID, 'method': 'credit_card'}

    #return requests.post(url, data = data)
    return requests.request("POST", url, data = data)

def api_tokens():
    url = URL + ACCOUNT_ID + "/api_tokens"
    #data = {'account_id': ACCOUNT_ID, 'method': 'credit_card'}

    return requests.post(url, data = data)


items = [
    {'description': 'Item 1',
     'quantity': 1,
     'price_cents': 1000},
    {'description': 'Item 2',
     'quantity': 1,
     'price_cents': 2000 },
]
data = {
        'token': TOKEN,
        #'account_id': 'D8B1B481EBF240E08C6325D64C4CBB08', 
        #'customer_payment_method_id': '4111111111111111', 
        'email': 'user@example.com',
        'items': items}

#print(api_tokens())
#print(payment_token().text)
print(charge(data).text)