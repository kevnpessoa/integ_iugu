import iugu
api = iugu.config(token='39B1841C-3940-49D5-9F5FA2596755629D')

iugu_token_api = iugu.Token()
items = [
    {'description': 'Item 1',
     'quantity': 1,
     'price_cents': 1000},
    {'description': 'Item 2',
     'quantity': 1,
     'price_cents': 2000 },
]
content = iugu_token_api.charge(
    {
        'customer_payment_method_id': '4111111111111111', 
        'email': 'marcusccoelho@gmail.com',
        'test': 'true',
        'items': items})

print(content)