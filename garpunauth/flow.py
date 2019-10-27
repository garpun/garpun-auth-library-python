from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

from oauth2client.tools import run_flow

from garpunauth import GARPUN_AUTH_URI, GARPUN_TOKEN_URI, GARPUN_TOKEN_INFO_URI
from garpunauth._default import CLIENT_SECRET, _get_well_known_file, CLIENT_ID


def flow_authenticate(scopes, flags=None, http=None):
    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, " ".join(scopes),
                               auth_uri=GARPUN_AUTH_URI,
                               token_uri=GARPUN_TOKEN_URI,
                               token_info_uri=GARPUN_TOKEN_INFO_URI,
                               )

    storage = Storage(_get_well_known_file())
    run_flow(flow, storage, flags=flags, http=http)
