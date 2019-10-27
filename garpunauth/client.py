import json
import os
import datetime

from oauth2client import _helpers
from oauth2client.file import Storage

from garpunauth import GARPUN_TOKEN_URI, GARPUN_REVOKE_URI
from garpunauth._default import _get_well_known_file
from oauth2client.client import OAuth2Credentials, EXPIRY_FORMAT


class GarpunCredentials(OAuth2Credentials):

    def __init__(self, access_token, client_id, client_secret, refresh_token,
                 token_expiry, token_uri, user_agent,
                 revoke_uri=GARPUN_REVOKE_URI, store=None):
        """Create an instance of GoogleCredentials.

        This constructor is not usually called by the user, instead
        GoogleCredentials objects are instantiated by
        GarpunCredentials.get_application_default().

        Args:
            access_token: string, access token.
            client_id: string, client identifier.
            client_secret: string, client secret.
            refresh_token: string, refresh token.
            token_expiry: datetime, when the access_token expires.
            token_uri: string, URI of token endpoint.
            user_agent: string, The HTTP User-Agent to provide for this
                        application.
            revoke_uri: string, URI for revoke endpoint. Defaults to
                        GARPUN_REVOKE_URI; a token can't be
                        revoked if this is None.
        """
        super(GarpunCredentials, self).__init__(
            access_token, client_id, client_secret, refresh_token,
            token_expiry, token_uri, user_agent, revoke_uri=revoke_uri)
        self.store = store

    def create_scoped_required(self):
        """Whether this Credentials object is scopeless.

        create_scoped(scopes) method needs to be called in order to create
        a Credentials object for API calls.
        """
        return False

    def create_scoped(self, scopes):
        """Create a Credentials object for the given scopes.

        The Credentials type is preserved.
        """
        return self

    @property
    def serialization_data(self):
        """Get the fields and values identifying the current credentials."""
        return {
            'type': 'authorized_user',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token
        }

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
            user_agent="Python client library",
            token_uri=GARPUN_TOKEN_URI,
            store=storage
        )

    @staticmethod
    def authenticate_user(scopes, flags=None, reauth=False):
        """Auth user with scopes. Auth not start if credentials already exist in storage"""
        if not reauth:
            creds = GarpunCredentials.get_application_default()
            if creds:
                return

        from argparse import Namespace
        from garpunauth.flow import flow_authenticate
        if flags is None:
            flags = Namespace(noauth_local_webserver=True, logging_level="INFO")
        flow_authenticate(scopes=scopes, flags=flags)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(_helpers._from_bytes(json_data))
        if (data.get('token_expiry') and
                not isinstance(data['token_expiry'], datetime.datetime)):
            try:
                data['token_expiry'] = datetime.datetime.strptime(
                    data['token_expiry'], EXPIRY_FORMAT)
            except ValueError:
                data['token_expiry'] = None
        garpun_creds = cls(
            data['access_token'],
            data['client_id'],
            data['client_secret'],
            data['refresh_token'],
            data['token_expiry'],
            data['token_uri'],
            data['user_agent'],
            revoke_uri=data.get('revoke_uri', None)
        )
        garpun_creds.invalid = data['invalid']
        return garpun_creds
