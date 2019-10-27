import os
from oauth2client.file import Storage
from garpun.auth._default import _get_well_known_file
from oauth2client.client import OAuth2Credentials


class GarpunCredentials(OAuth2Credentials):

    @staticmethod
    def get_application_default():
        file = _get_well_known_file()
        if not os.path.exists(file):
            return None

        storage = Storage(file)
        creds = storage.get()

        if creds is None:
            return None

        return GarpunCredentials(
            access_token=creds.access_token,
            refresh_token=creds.refresh_token,
            token_expiry=creds.token_expiry,
            client_id=creds.client_id,
            client_secret=creds.client_secret,
            user_agent="Python client library"
        )

