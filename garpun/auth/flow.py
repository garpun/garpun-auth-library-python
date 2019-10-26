from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

from garpun import GARPUN_AUTH_URI, GARPUN_TOKEN_URI, GARPUN_TOKEN_INFO_URI
from garpun.auth import CLIENT_ID, CLIENT_SECRET
from oauth2client.tools import run_flow

scopes = ['meta.metaql']
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, " ".join(scopes),
                           auth_uri=GARPUN_AUTH_URI,
                           token_uri=GARPUN_TOKEN_URI,
                           token_info_uri=GARPUN_TOKEN_INFO_URI,
                           )

storage = Storage('/Users/arturgspb/PycharmProjects/garpun-auth-library-python/out.json')
run_flow(flow, storage)
