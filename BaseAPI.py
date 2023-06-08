import requests
from config import API_KEY

class BaseAPI():

    def __init__(self, url):
        self.url = url

    def get_method(self,parametr_get):          
        response=requests.get(self.url,parametr_get)
        #if response.status_code == 200:
        return response

    def post_method(self,params_post,data_post):
        self.post_metod=requests.post(self.url,params_post,data_post)

    def put_method(self,params_put,data_put):
        self.put_metod=requests.put(self.url,params_put,data_put)