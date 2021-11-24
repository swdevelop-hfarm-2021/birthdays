import json
import requests

class v2:
    api_key = 6981d02afb34fb0d7f67b5ad93491ab8283a7773

    def __init__(self, api_key):
        self.api_key = api_key

    def holidays(self, parameters):
        url = 'https://calendarific.com/api/v2/holidays?'

        if parameters.has_key('api_key') is False:
            parameters['api_key'] = self.api_key

        response = requests.get(url, params=parameters);
        data     = json.loads(response.text)

        if response.status_code != 200:
            if data.has_key('error') is False:
                data['error'] = 'Unknown error.'

        return data

