import requests
from config import API_KEY

url="http://api.exchangeratesapi.io/v1/latest"
#payload={}
#auth = {"access_key":"8dcaab652b9e48d734026fef88cfa30a"}
#?access_key=8dcaab652b9e48d734026fef88cfa30a&base=EUR&symbols=AED
params = {'access_key': API_KEY,'base':'EUR','symbols':'AED'}
response = requests.get(url, params)
print(response.status_code)
