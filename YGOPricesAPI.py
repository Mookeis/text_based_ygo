import json
import requests


class YGOPricesAPI():

    def __init__(self):
        self.url = "http://yugiohprices.com/api"

    @staticmethod
    def __make_request(self, url):
        request = requests.get(url)

        if request.status_code != 200:
            status_code = request.status_code
            reason = request.reason
            raise Exception(f'Status code: {status_code} Reason: {reason}')

        return request.json()
