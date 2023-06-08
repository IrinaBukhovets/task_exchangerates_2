from BaseCache import BaseCache
import time

class ExReCache(BaseCache):

    def exre_save_response(self):
        response = {}# не понимаю как определить response 
        time_resp = response["timestamp"]
        base_currency = response["base"]
        exchang_currency = exchang_currency_value

        exchang_currency_value = None
        for item in response["rates"].keys():
            exchang_currency_value = item

        return [time_resp,base_currency,exchang_currency] 

        #self.save_cache() #не понимаю как применить пустую функцию save_cache
