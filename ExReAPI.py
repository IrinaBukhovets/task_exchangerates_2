from BaseAPI import BaseAPI 
from general_config import GeneralConfigsUrl

class ExReAPI(BaseAPI):

    url = GeneralConfigsUrl.BASE_URL
    name_api = '/latest'    
    url_exre = url + name_api

    def __init__(self):
        super().__init__(url=self.url_exre)

    def get_latest_json(self,api_key,base_currency,exchange_currency): 
        resp = self.get_method([('access_key', api_key),('base',base_currency),('symbols',exchange_currency)])
        return resp.json()