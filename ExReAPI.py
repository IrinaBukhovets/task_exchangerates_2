import requests
from BaseAPI import BaseAPI 
from config import API_KEY

#GET_url_latest='http://api.exchangeratesapi.io/v1/latest'
#params = {'access_key': API_KEY,'base':'EUR','symbols':'AED'}
#GET_url_symbols='http://api.exchangeratesapi.io/v1/symbols'
#GET_url_convert='http://api.exchangeratesapi.io/v1/convert' 

class ExReAPI(BaseAPI):

    url_metod = 'http://api.exchangeratesapi.io/v1/latest'

    def __init__(self):
        super().__init__(url=self.url_metod)

    def get_latest(self):
        self.get_metod({'access_key': API_KEY,'base':'EUR','symbols':'AED'})
        return self.get_metod


r = ExReAPI()
response = r.get_latest()
print(response.status_code)