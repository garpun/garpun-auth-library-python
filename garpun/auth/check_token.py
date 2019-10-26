import httplib2
import requests
from oauth2client.client import Credentials
from oauth2client.file import Storage

storage = Storage('/Users/arturgspb/PycharmProjects/garpun-auth-library-python/out.json')

credentials: Credentials = storage.get()

print(u"cred.to_json() = %s" % str(credentials.to_json()))

http = credentials.authorize(httplib2.Http())
credentials.refresh(http)

print(u"credentials.access_token = %s" % str())

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
resp = requests.post("http://apimeta.devision.io/api/v1/meta/metaql/download-data?access_token=" + credentials.access_token, json=configuration)

print(u"resp.text = %s" % str(resp.text))
