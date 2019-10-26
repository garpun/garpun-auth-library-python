import httplib2
from googleapiclient.discovery import build
from oauth2client.client import Credentials
from oauth2client.file import Storage

storage = Storage('/Users/arturgspb/PycharmProjects/garpun-auth-library-python/out.json')

credentials: Credentials = storage.get()

print(u"cred.to_json() = %s" % str(credentials.to_json()))

http = credentials.authorize(httplib2.Http())
credentials.refresh(http)

print(u"credentials.access_token = %s" % str(credentials.access_token))
# youtube = build("qweqwe", "v3", http=authorize)
