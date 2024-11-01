import requests


class DNDAPI:
    def __init__(self):
        self.url = "https://www.dnd5eapi.co/api/spells"
        self.headers = {'Accept': 'application/json'}
        self.spells = self.connect()

    def connect(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                result = data['results']
                return result
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
