from BaseAPI import BaseAPI
from ExReAPI import ExReAPI
import time
from ExReCach import ExReCach



#a = BaseAPI(url='http://api.exchangeratesapi.io/v1/latest')
#resp = a.get_method(parametr_get=[('access_key', '8dcaab652b9e48d734026fef88cfa30a'), ('base', 'EUR'), ('symbols', 'USD')])
#print(str(resp.text))
print(time.time())
b = ExReAPI()
respon = b.get_latest('EUR','USD')
save = ExReCach()
file = save.save_response_in_file(respon)
print(file)