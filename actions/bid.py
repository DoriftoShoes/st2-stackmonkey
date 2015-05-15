import json
from lib.base import BaseStackMonkeyAction

__all__ = [
    'Bid'
]


class Bid(BaseStackMonkeyAction):
    def _create_wisp(self, role):
        definition = json.load(self.definition[role])
        response = self._post_request(endpoint="wisp", data=definition)
        if response['response'] == 'success':
            return response['result']['wisp']
        else:
            return False

    def _run(self, flavor, role="stackstorm"):
        wisp = self._create_wisp(role)
        request_body = {
            "flavor": flavor,
            "wisp_id": wisp[id]
        }
        bid = self._post_request(endpoint="bids", data=request_body)
        if bid['response'] == 'success':
            return bid['response']
        else:
            return False
