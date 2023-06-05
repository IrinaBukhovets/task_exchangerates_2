import requests
from config import API_KEY

#url="http://api.exchangeratesapi.io/v1/latest"
#params = {'access_key': API_KEY,'base':'EUR','symbols':'AED'}
#response = requests.get(url, params)
#if response.status_code == 200:
    #print('Success!')

class BaseAPI():

    def __init__(self, url):
        self.url = url

    def get_metod(self,parametr_get):  
        self.parametr_get = parametr_get
        self.get_metod=requests.get(self.url,parametr_get)
        if self.get_metod.status_code == 200:
            return self.get_metod

    def post_metod(self,params_post,data_post):
        self.params_post = params_post
        self.data_post = data_post
        self.post_metod=requests.post(self.url,params_post,data_post)

    def put_metod(self,params_put,data_put):
        self.params_put = params_put
        self.data_put = data_put
        self.put_metod=requests.put(self.url,params_put,data_put)