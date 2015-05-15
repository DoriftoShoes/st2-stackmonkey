import requests

from st2actions.runners.pythonrunner import Action

__all = [
    'BaseStackMonkeyAction'
    ]

BASE_URL = 'https://www.stackmonkey.com/api/'
API_VERSION = 'v1'


class BaseStackMonkeyAction(Action):
    def __init__(self, config):
        super(BaseStackMonkeyAction, self).__init__(config=config)
        self.definition = config['definition']

    def _build_url(self, endpoint):
        return BASE_URL + API_VERSION + "/" + endpoint + "/"

    def _get_request(self, endpoint):
        url = self._build_url(endpoint)
        r = requests.get(url)
        return r.json()

    def _post_request(self, endpoint, data):
        url = self._build_url(endpoint)
        r = requests.post(url, data)
        return r.json()
