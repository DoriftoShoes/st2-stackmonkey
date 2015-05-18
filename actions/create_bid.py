import json
from lib.base import BaseStackMonkeyAction

__all__ = [
    'CreateBid'
]


class CreateBid(BaseStackMonkeyAction):
    def _create_wisp(self, role):
        definition = json.load(open(self.definition[role]))
        response = self._post_request(endpoint="wisp", data=json.dumps(definition))
        if response['response'] == 'success':
            return response['result']['wisp']
        else:
            return False

    def run(self, flavor, role="stackstorm"):
        wisp = self._create_wisp(role)
        self.logger.info(wisp)
        request_body = {
            "flavor": flavor,
            "wisp_id": wisp['id']
        }
        self.logger.info(request_body)
        bid = self._post_request(endpoint="bids", data=json.dumps(request_body))
        return bid
        if bid['response'] == 'success':
            return json.dumps(bid)
        else:
            return False
