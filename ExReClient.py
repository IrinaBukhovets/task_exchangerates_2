from ExReAPI import ExReAPI
from config import API_KEY
from ExReCach import ExReCache
import json

client_exre = ExReAPI()
response = client_exre.get_latest('EUR','AED')
#print(str(response.json()))
#resp_dict = response.json()
print(response)
print(response["timestamp"])
print(response["base"])
print(response["rates"].keys())
cache_second_value = None
for item in response["rates"].keys():
    cache_second_value = item
print(cache_second_value)   

time_resp = response["timestamp"]
base_currency = response["base"]
#exchang_currency = exchang_currency_value

exchang_currency = None
for item in response["rates"].keys():
    exchang_currency = item
currency_value = response["rates"][exchang_currency]

save = {"time_resp":response["timestamp"],"base_currency":response["base"],item:currency_value}
print(save)

with open("save_re.json", "w") as f:
    f.write(json.dumps(save, indent=4))
