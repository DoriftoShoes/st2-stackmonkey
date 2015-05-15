from lib.base import BaseStackMonkeyAction

__all__ = [
    'Flavors'
]


class Flavors(BaseStackMonkeyAction):
    def _run(self, role, vpus, memory):
        matching_flavors = []
        flavors = self._get_request(endpoint="flavors")
        for flavor in flavors:
            if flavor['vpus'] == vpus and flavor['memory'] == memory:
                matching_flavors.append(flavor['name'])

        return matching_flavors