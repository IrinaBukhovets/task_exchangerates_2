import time
from ExReAPI import ExReAPI
from ExReCach import ExReCach

filename = "save_re.json"
exchange_currency = "USD"
check = ExReCach(filename)
a=check.check_exchange_currency(exchange_currency)
if a != exchange_currency :
    print (a)
else:
    b = ExReAPI()
    response = b.get_latest('EUR',exchange_currency)
    file = ExReCach(filename)
    f=file.save_response_in_file(response)
    print("запрос проходит и сохраняется")
