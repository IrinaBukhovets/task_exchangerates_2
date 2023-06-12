import os
import datetime
from ExReAPI import ExReAPI

if os.path.isfile("save_response.txt") == False:
    client_exre = ExReAPI()
    response = client_exre.get_latest('EUR','AED')
    time_resp = response["timestamp"]
    base_currency = response["base"]
    exchang_currency = None
    for item in response["rates"].keys():
        exchang_currency = item
    currency_value = response["rates"][exchang_currency]
    with open("save_response.txt", "w") as file:
        file.write(f"{time_resp}, {base_currency}, {exchang_currency}, {currency_value} \n")
else:
    #with open("save_response.txt", "a") as file:
        #file.write(f"{datetime.datetime.now()} - File updated \n")
    with open("save_response.txt") as f:
        if 'AED' in f.read():
            print("true")