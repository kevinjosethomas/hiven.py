import aiohttp

from hiven.data import API_URL


class HTTPClient:
    def __init__(self, session: aiohttp.ClientSession, client, token: str):
        self._session = session
        self._client = client
        self._token = token

    async def request(self, method: str, endpoint: str, data: dict = None, headers: dict = None):
        """Sends a request with the provided information"""

        if not headers:
            headers = {"Authorization": self._token, "Content-Type": "application/json"}
        else:
            headers["Authorization"] = headers.get("Authorization", self._token)
            headers["Content-Type"] = headers.get("Content-Type", "application/json")

        response = await self._session.request(method=method, url=API_URL + endpoint, json=data, headers=headers)
        response_data = await response.json()

        return response, response_data
