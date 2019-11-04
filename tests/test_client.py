import os
import json
import pytest
import garpunauth
from garpunauth.client import GarpunCredentials
from garpunauth import exceptions

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
AUTHORIZED_USER_FILE = os.path.join(DATA_DIR, "authorized_user.json")

with open(AUTHORIZED_USER_FILE) as fh:
    AUTHORIZED_USER_FILE_DATA = json.load(fh)


def test__get_application_default_missing_file():
    with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
        GarpunCredentials.get_application_default("")

    assert excinfo.match(r"not found")


def test__get_application_default_invalid_json(tmpdir):
    jsonfile = tmpdir.join("invalid.json")
    jsonfile.write("{")

    with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
        GarpunCredentials.get_application_default(str(jsonfile))

    assert excinfo.match(r"not a valid json file")


def test_get_application_default_bad_format(tmpdir):
    filename = tmpdir.join("authorized_user_bad.json")
    filename.write(json.dumps({"type": "authorized_user"}))
    with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
        GarpunCredentials.get_application_default(filename)

    assert excinfo.match(r"Failed to load authorized user")
    assert excinfo.match(r"missing fields")


def test__load_credentials_from_file_authorized_user():
    credentials, project_id = GarpunCredentials.get_application_default(
        AUTHORIZED_USER_FILE
    )
    assert isinstance(credentials, garpunauth.client.GarpunCredentials)
    assert project_id is None
