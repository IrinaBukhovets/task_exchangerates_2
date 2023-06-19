import os
import json
import time
from pathlib import Path


class ExReCach():

    def __init__(self, filename: str):
        if not os.path.exists(path=filename):
            with open(filename, "a"):
                pass
        self.filename = filename

    def check_exchange_currency(self,exchange_currency):
        if os.stat(self.filename).st_size != 0:
            path = Path (self.filename)
            data = json.loads(path.read_text(encoding='utf-8'))
            keys = data.keys()
            time_now = time.time()
            if exchange_currency in keys:
                if data[exchange_currency]["timestamp"]<time_now-600:
                    #print ('Нужен запрос, валюта уже есть и прошло 10 мин')
                    return exchange_currency
                else: 
                    #print("не прошло 10 мин")
                    return data[exchange_currency]                 
            else: 
                #print("валюты нет")
                return exchange_currency
        else:
            return exchange_currency

    def save_response_in_file (self,response):
        if os.stat(self.filename).st_size == 0:
            #print ('пустой файл')
            time_resp = response["timestamp"]
            exchange_currency = None
            for item in response["rates"].keys():
                exchange_currency = item
            currency_value = response["rates"][exchange_currency]
            save = {item:{"currency_value":currency_value,"timestamp":time_resp }}
            with open(self.filename, "w") as file:
                file.write(json.dumps(save,indent=4))
            path = Path (self.filename)
            data = json.loads(path.read_text(encoding='utf-8'))
            #print('первое сохранение в файл')
            return data
        else:     
            path = Path(self.filename)
            data = json.loads(path.read_text(encoding='utf-8'))
            time_resp = response["timestamp"]
            exchange_currency = None
            for item in response["rates"].keys():
                exchange_currency = item
            currency_value = response["rates"][exchange_currency]
            data[item] = {"currency_value":currency_value,"timestamp":time_resp}
            with open(self.filename, "w") as file:
                json.dump(data, file,indent=4)
            path = Path (self.filename)
            data = json.loads(path.read_text(encoding='utf-8'))
            #print('сохранено')
            return data
                


                



    

