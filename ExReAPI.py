import requests
from BaseAPI import BaseAPI 
from config import API_KEY

class ExReAPI(BaseAPI):

    url_exre = "http://api.exchangeratesapi.io/v1/latest"

    def __init__(self):
        super().__init__(url=self.url_exre)

    def get_latest(self,base_currency,exchang_currency):
        a=('access_key', API_KEY)
        b=('base',base_currency)
        c=('symbols',exchang_currency)
        parametr_get=[a,b,c]
        resp = self.get_method(parametr_get)
       #if resp.status_code == 200:
        return resp.json()