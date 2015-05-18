import json
import time
from lib.base import BaseStackMonkeyAction

__all__ = [
    'GetBid'
]


class GetBid(BaseStackMonkeyAction):
    def run(self, bid_token):
        endpoint = "bids/%s" % (bid_token)
        bid = self._get_request(endpoint=endpoint)
        while 'instance' not in bid['result'].keys() and bid['response'] == 'success':
            time.sleep(20)
        
        if bid['response'] != 'success':
            return False
        return bid
