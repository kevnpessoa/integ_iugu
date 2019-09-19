import api
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "email": "marcusccoelho@gmail.com",
        "months": "1",
        "items": [
            {"description": "Item 1",
            "quantity": "1",
            "price_cents": "1000"}],
        "credit_card": {
            "number":"4111111111111111",
            "verification_value": "123",
            "first_name": "Kevin",
            "last_name":"Pessoa",
            "month":"10",
            "year":"2020"
        }
    }

    #print(data['items'])
    #print(api.payment_token(data['credit_card']).status_code);
    #print(api.charge(data))
    response = api.charge(data)
    return response #["status_code"]
    #response = api.payment_token(data['credit_card'])
    #return response["id"]

if __name__ == '__main__':
    app.run(debug=True)