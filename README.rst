Garpun Auth Python Library
^^^^^^^^^^^^^^^^^^^^^^^^^^

This library simplifies using Garpun's various server-to-server authentication
mechanisms to access Garpun APIs.

Google `oauth2client
<https://github.com/googleapis/oauth2client>`_ library is taken as a basis.

Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.4


Installing
----------

You can install using `pip`_::

    $ pip install garpun-auth

.. _pip: https://pip.pypa.io/en/stable/




Using
_____


.. code-block:: python

    # Use it for first auth with your scopes
    GarpunCredentials.authenticate_user(['cloud-platform'])

    # Get default credentials
    credentials = GarpunCredentials.get_application_default()
    print(u"credentials.access_token = %s" % str(credentials.access_token))
    print(u"credentials.access_token_expired = %s" % str(credentials.access_token_expired))
    print(u"credentials.refresh_token = %s" % str(credentials.refresh_token))

    # Refresh access_token if it expired
    import httplib2
    http = credentials.authorize(httplib2.Http())
    credentials.refresh(http)
    print(u"credentials.access_token = %s" % str(credentials.access_token))
