from ExReCach import ExReCach
from ExReAPI import ExReAPI

from general_config import GeneralConfigsCurrensy
from config import API_KEY

class ExReClient():
    
    api_key = API_KEY
    base_currency = GeneralConfigsCurrensy.BASE_CURRENCY
    filename = "save_re.json"
    
    def requests_exre(self, exchange_currency):
        check_in_file = ExReCach(self.filename)
        check_result = check_in_file.check_exchange_currency(exchange_currency)
        if check_result != exchange_currency:
            return check_result
        else:
            make_request = ExReAPI()
            response = make_request.get_latest_json(self.api_key, self.base_currency, exchange_currency)
            save_response = ExReCach(self.filename)
            save=save_response.save_response_in_file(response)
            return save[exchange_currency]
            
