import requests

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

api.refresh_access_token()

configuration = {
    "download": {
        "dbQuery": {
            "command": """
            SELECT COALESCE(NULLIF(organization_id, 2), 42) as org, SUM(salary) as sum_salary
            FROM meta_samples.employee
            GROUP BY org
            ORDER BY sum_salary DESC
            """
        }
    }
}
resp = requests.post("http://apimeta.devision.io/api/v1/meta/metaql/download-data?access_token=" + api.access_token, json=configuration)

print(u"resp.text = %s" % str(resp.text))
