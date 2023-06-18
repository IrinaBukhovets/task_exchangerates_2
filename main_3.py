from ExReClient import ExReClient


client_requests = ExReClient()
response = client_requests.requests_exre('AED')
print(response['currency_value'])
    

