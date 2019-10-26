import os
from os.path import expanduser

CLIENT_ID = "3be330f2e360496592a7be653c27e51e"
CLIENT_SECRET = "939992f0-f2db-4ea4-95e5-593da220e13e"
config_folder = os.path.join(expanduser("~"), ".config", 'garpuncloud')
os.makedirs(config_folder, exist_ok=True)

DEFAULT_CREDENTIALS = os.path.join(config_folder, 'default_credentials.json')
