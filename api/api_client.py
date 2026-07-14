import requests

class APIClient:

    def __init__(self, token):

        self.base_url = "https://app.workflowpro.com/api/v1"

        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def post(self, endpoint, body):

        return requests.post(
            self.base_url + endpoint,
            json=body,
            headers=self.headers
        )
