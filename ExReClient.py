from ExReAPI import ExReAPI
from config import API_KEY

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