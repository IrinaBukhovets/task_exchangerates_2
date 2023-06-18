import os
import json
import time
from pathlib import Path

class ExReCach():

    def save_response_in_file(self,response):
        if os.path.isfile("save_re.json") == False:
            time_resp = response["timestamp"]
            exchange_currency = None
            for item in response["rates"].keys():
                exchange_currency = item
            currency_value = response["rates"][exchange_currency]
            save = {item:{"currency_value":currency_value,"timestamp":time_resp }}
            with open("save_re.json", "w") as file:
                file.write(json.dumps(save,indent=4))
            path = Path ("save_re.json")
            data = json.loads(path.read_text(encoding='utf-8'))
            return data
        else:
            path = Path ("save_re.json")
            data = json.loads(path.read_text(encoding='utf-8'))                     
            #time_resp = response["timestamp"]
            exchange_currency = None
            for item in response["rates"].keys():
                exchange_currency = item
            #currency_value = response["rates"][exchange_currency]
            time_now = time.time()
            for key in data:
                if key == item:
                    if data[item]["timestamp"]<time_now-600:
                        data[item] = {"currency_value":currency_value,"timestamp":time_resp}
                        with open("save_re.json", 'w') as json_file:
                            json.dump(data, json_file,indent=4)
                        print (f'{data[item]["currency_value"]} - валюта уже есть и прошло 10 мин')
                    else: 

                        print(f'{data[item]} - валюта уже есть и не прошло 10 мин')         
                else:
                    data[item] = {"currency_value":currency_value,"timestamp":time_resp}
                    with open("save_re.json", 'w') as json_file:
                        json.dump(data, json_file,indent=4)
                    path = Path ("save_re.json")
                    data = json.loads(path.read_text(encoding='utf-8'))
                    print(f'{data[item]["currency_value"]} - валюта новая')
                



    

