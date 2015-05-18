from lib.base import BaseStackMonkeyAction

__all__ = [
    'Flavors'
]


class Flavors(BaseStackMonkeyAction):
    def run(self, vpus, memory):
        matching_flavors = []
        flavors = self._get_request(endpoint="flavors")
        return flavors
        for flavor in flavors:
            if flavor['vpus'] == vpus and flavor['memory'] == memory:
                matching_flavors.append(flavor['name'])

        return matching_flavors
