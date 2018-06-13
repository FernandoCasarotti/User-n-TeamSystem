from google.appengine.ext import ndb

import endpoints
from protorpc import messages

class User(ndb.Model):
    name = ndb.StringProperty()

class ApiUser(messages.Message):
    name = messages.StringField(1)
    country = messages.StringField(2)
    id = messages.IntegerField(3)

class ApiUsers(messages.Message):
    users = messages.MessageField(ApiUser,1,repeated=True)
