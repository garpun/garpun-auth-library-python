import os


CLIENT_ID = "3be330f2e360496592a7be653c27e51e"
CLIENT_SECRET = "939992f0-f2db-4ea4-95e5-593da220e13e"

_GARPUN_CLOUDSDK_CONFIG_ENV_VAR = 'GARPUN_CLOUDSDK_CONFIG'
_CLOUDSDK_CONFIG_DIRECTORY = 'garpuncloud'
_WELL_KNOWN_CREDENTIALS_FILE = 'default_credentials.json'


def _get_well_known_file():
    """Create config dir if not exists and return path of default config file"""
    default_config_dir = os.getenv(_GARPUN_CLOUDSDK_CONFIG_ENV_VAR)
    if default_config_dir is None:
        if os.name == 'nt':
            try:
                default_config_dir = os.path.join(os.environ['APPDATA'],
                                                  _CLOUDSDK_CONFIG_DIRECTORY)
            except KeyError:
                # This should never happen unless someone is really
                # messing with things.
                drive = os.environ.get('SystemDrive', 'C:')
                default_config_dir = os.path.join(drive, '\\',
                                                  _CLOUDSDK_CONFIG_DIRECTORY)
        else:
            default_config_dir = os.path.join(os.path.expanduser('~'),
                                              '.config',
                                              _CLOUDSDK_CONFIG_DIRECTORY)

    os.makedirs(default_config_dir, exist_ok=True)

    return os.path.join(default_config_dir, _WELL_KNOWN_CREDENTIALS_FILE)
