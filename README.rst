Garpun Auth Python Library
==========================

|build| |pypi|

This library simplifies using Garpun's various server-to-server authentication
mechanisms to access Garpun APIs.


.. |build| image:: https://travis-ci.org/garpun/garpun-auth-library-python.svg?branch=master
   :target: https://travis-ci.org/garpun/garpun-auth-library-python
.. |pypi| image:: https://img.shields.io/pypi/v/garpunauth.svg
   :target: https://pypi.python.org/pypi/garpunauth


Installing
__________

You can install using `pip`_::

    $ pip install garpunauth

.. _pip: https://pip.pypa.io/en/stable/


Supported Python Versions
_________________________
Python >= 3.6


Using
_____


.. code-block:: python

    # Use it for first auth with your scopes
    from garpunauth.client import GarpunCredentials

    credentials, project_id = GarpunCredentials.authenticate_user(['cloud-platform'])

    print(u"credentials.access_token = %s" % str(credentials.access_token))
    print(u"credentials.access_token_expired = %s" % str(credentials.access_token_expired))
    print(u"credentials.refresh_token = %s" % str(credentials.refresh_token))

    # Refresh access_token if it expired
    GarpunCredentials.refresh_credentials(credentials)

    print(u"credentials.access_token = %s" % str(credentials.access_token))


For contributors
________________


1. Use `make black` for blacken the code
2. Use `nox` for run tests and other checks
3. Set PyCharm default test runner to pytest
