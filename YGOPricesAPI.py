import requests


class YGOPricesAPI:

    def __init__(self):
        self.url = "http://yugiohprices.com/api"

    @staticmethod
    def __make_request(url):
        request = requests.get(url)

        if request.status_code != 200:
            status_code = request.status_code
            reason = request.reason
            raise Exception(f'Status code: {status_code} Reason: {reason}')

        return request.json()

    def get_names(self):
        url = f"{self.url}/card_names"
        return self.__make_request(url)

    def get_data(self, name):
        url = f"{self.url}/card_data/{name}"
        return self.__make_request(url)

    def get_image(self, name):
        url = f"{self.url}/card_image/{name}"
        return self.__make_request(url)
