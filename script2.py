import requests

URL = "https://api.iugu.com/v1/"
ACCOUNT_ID = "D8B1B481EBF240E08C6325D64C4CBB08"
#TOKEN = 'e022d466b0b445ec68c65470f3af7019'
#TOKEN = '39B1841C-3940-49D5-9F5FA2596755629D'

def payment_token():
    #data = {'account_id': ACCOUNT_ID, 'method': 'credit_card', 'test': 'true'}

    data = {"account_id": ACCOUNT_ID, "method": "credit_card", "test":"true", 
            "data": {
                "number":"4111111111111111",
                "verification_value": "123",
                "first_name": "Kevin",
                "last_name":"Pessoa",
                "month":"10",
                "year":"2020"
            } }

    #payload = "{\"account_id\":\"D8B1B481EBF240E08C6325D64C4CBB08\",\"method\":\"credit_card\",\"test\":\"true\",\"data\":{\"number\":\"4111111111111111\",\"verification_value\":\"123\",\"first_name\":\"Kevin\",\"last_name\":\"Pessoa\",\"month\":\"10\",\"year\":\"2020\"}}"
    payload = {"account_id":"D8B1B481EBF240E08C6325D64C4CBB08","method":"credit_card","test":"true","data":{"number":"4111111111111111","verification_value":"123","first_name":"Kevin","last_name":"Pessoa","month":"10","year":"2020"}}

    return requests.post(URL + "payment_token", data=payload)

def charge( data ):
    return requests.post(URL + "charge", data = data)