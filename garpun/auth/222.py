from metasdk.apiclient import ApiClient

from garpun.auth import CLIENT_ID, CLIENT_SECRET

api_host = "http://trafficestimator.apis.devision.io"
api_version = "v1"

api = ApiClient(
    host=api_host,
    api_version=api_version,
    access_token=None,
    refresh_token="2eaad05bc46549398ad32a6cdf31362f",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

resp = api.post("keyword/get", post_data={
    "keywords": [
        "bmw"
    ]
})
print(resp)
