import requests


class BaseAPI():

    def __init__(self, url):
        self.url = url

    def get_method(self, parametr_get):          
        response_get_method=requests.get(self.url, parametr_get)
        return response_get_method
    
    def post_method(self, params_post, data_post):
        response_post_metod=requests.post(self.url, params_post, data_post)
        return response_post_metod

    def put_method(self, params_put, data_put):
        response_put_metod=requests.put(self.url, params_put, data_put)
        return response_put_metod
        