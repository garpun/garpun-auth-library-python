from oauth2client.client import Credentials
from oauth2client.file import Storage

from garpun.auth._default import _get_well_known_file


def get_default_credentials() -> Credentials:
    storage = Storage(_get_well_known_file())
    return storage.get()
