import os
import datetime
from ExReAPI import ExReAPI
import json
from pathlib import Path
import datetime

if os.path.isfile("save_re.json") == False:
    client_exre = ExReAPI()
    response = client_exre.get_latest('EUR','AED')
    time_resp = response["timestamp"]
    base_currency = response["base"]
    exchang_currency = None
    for item in response["rates"].keys():
        exchang_currency = item
    currency_value = response["rates"][exchang_currency]
    save = {time_resp:{item:currency_value}}
    with open("save_re.json", "w") as file:
        file.write(json.dumps(save,indent=4))
    
else:
    path = Path ("save_re.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    client_exre = ExReAPI()
    response = client_exre.get_latest('EUR','USD')
    time_resp_1 = response["timestamp"]
    base_currency = response["base"]
    exchang_currency = None
    for item in response["rates"].keys():
        exchang_currency = item
    currency_value_1 = response["rates"][exchang_currency]
    data[time_resp_1] = {item:currency_value_1}

    with open("save_re.json", 'w') as json_file:
        json.dump(data, json_file,indent=4)
    with open("save_re.json") as f:
        if 'AED' in f.read():
            print("true")

        
