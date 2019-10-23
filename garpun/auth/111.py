import requests
from oauthlib.oauth2 import WebApplicationClient

import socket
from contextlib import closing

from garpun.auth import CLIENT_ID, CLIENT_SECRET
from garpun import GARPUN_AUTH_URI, GARPUN_TOKEN_URI, GARPUN_TOKEN_INFO_URI


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


client = WebApplicationClient(CLIENT_ID)
res = client.prepare_request_uri(GARPUN_AUTH_URI,
                                 scope=['meta.metaql'],
                                 redirect_uri="http://localhost:" + str(find_free_port()) + '/auth-callback',
                                 )

# http://localhost:51637/auth-callback?code=v2:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJoYXNoSWRcIjpcIjRjZjZkMTE0LTM0YjUtNDYwOC05MTYzLWUxYzY0MWJjZWFmMlwiLFwic2lnbmF0dXJlXCI6e1wic3RhdGVcIjpudWxsLFwiY2xpZW50SWRcIjpcIjNiZTMzMGYyZTM2MDQ5NjU5MmE3YmU2NTNjMjdlNTFlXCIsXCJyZWRpcmVjdFVyaVwiOlwiaHR0cDovL2xvY2FsaG9zdDo1MTYzNy9hdXRoLWNhbGxiYWNrXCIsXCJzY29wZXNcIjpbXCJtZXRhLm1ldGFxbFwiXSxcInVzZXJJZFwiOjQ1MDEsXCJjb21wYW55SWRcIjoyODkxfSxcInZhbGlkVG9UaW1lc3RhbXBcIjoxNTcxODYyNzA2Mzg1fSJ9.UPRTPrO99TpIpIn_64FQ2H6nYy-QoF_WocqkTG8b6Og&state
print(u"res = %s" % str(res))

code = "v2:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJoYXNoSWRcIjpcIjExMzRjMDZhLTkyYTUtNGQ0Yy04MzhhLWFkY2Y1ZmNhOGEwN1wiLFwic2lnbmF0dXJlXCI6e1wic3RhdGVcIjpudWxsLFwiY2xpZW50SWRcIjpcIjNiZTMzMGYyZTM2MDQ5NjU5MmE3YmU2NTNjMjdlNTFlXCIsXCJyZWRpcmVjdFVyaVwiOlwiaHR0cDovL2xvY2FsaG9zdDo1MTgyNy9hdXRoLWNhbGxiYWNrXCIsXCJzY29wZXNcIjpbXCJtZXRhLm1ldGFxbFwiXSxcInVzZXJJZFwiOjQ1MDEsXCJjb21wYW55SWRcIjoyODkxfSxcInZhbGlkVG9UaW1lc3RhbXBcIjoxNTcxODYzMTY5NTk4fSJ9.rxDgjPjoFyJ4ahbTKixOQ3La-AQSLwpFAOa5YiE1tYc"
headers = {
    'content-type': 'application/x-www-form-urlencoded',
}
body = client.prepare_request_body(code=code, client_secret=CLIENT_SECRET)
print(u"body = %s" % str(body))
resp = requests.post(GARPUN_TOKEN_URI, data=body, headers=headers)

print(u"resp.text = %s" % str(resp.text))


# 2eaad05bc46549398ad32a6cdf31362f

# resp.text = {"scopes":["meta.metaql"],"token_type":"bearer","refresh_token":"2eaad05bc46549398ad32a6cdf31362f","access_token":"eyJraWQiOiJhZWRiYmZlN2NjZjA3YzRiZWZkNDUwOTAxNTAxYjgzNzg3Njg1ZWNmIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJhcGlzLmRldmlzaW9uLmlvIiwic3ViIjoiNDUwMSIsIml1aWQiOjAsInNjb3BlIjoibWV0YS5tZXRhcWwiLCJpc3MiOiJ0b2tlbi1pc3N1ZXIuZGV2aXNpb24uaW8iLCJleHAiOjE1NzE4NjM0MjIsImlhdCI6MTU3MTg2MzEyMn0.Gj4GESdvaXhwtvIRPMQ8IcCLxNIAJB-AdDwaMR8qkskcAzv4JLgjB-1mip-gbln85il4WUaCXGU1fCp2EnJsDqSvJ8q-2Kb9brmmMMdrJjHMTLkDhODGbjwZqthUGDGsbd_Ym3tazQla9Dgg7A8qPOiDf0zIKNRN7jQC2K_Te5xBJ66IStucVhvykg6LDVzmGxDI5t4LJqWG6GbXD8jabEpi9I3zuWyr_CYDqTFPqt573ykz8PPcA4eQ66xDkwTGE3ioFL6NxDLLGKUS4t4JKYCJbCUOqWtKiD_Rr_GmpGYX63FLHOXgiRcS1Fb_PxYQNj_L3hwU3MMXoxAwzeuGpQ","expires":300,"user_id":4501,"company_id":2891}
