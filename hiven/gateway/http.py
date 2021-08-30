import aiohttp

from hiven.data import API_URL


class HTTPClient:
    def __init__(self, session: aiohttp.ClientSession, client, token: str):
        self._session = session
        self._client = client
        self._token = token

    async def request(self, method: str, endpoint: str, data: dict, headers: dict = {}):
        """Sends a request with the provided information"""

        headers["Authorization"] = self._token if not headers.get("Authorization") else None
        headers["Content-Type"] = "application/json" if not headers.get("Content-Type") else None

        response = await self._session.request(
            method=method, url=API_URL + endpoint, json=data, headers=headers
        )
        response_data = await response.json()

        return response, response_data
