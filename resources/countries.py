from google.appengine.ext import ndb

import endpoints
from protorpc import messages

#This will make the second flow rule: a country cannot be registered twice
class Country(ndb.Model):
    pass

class ApiCountry(messages.Message):
    name = messages.StringField(1)
    id = messages.StringField(2)

class ApiCountries(messages.Message):
    countries = messages.MessageField(ApiCountry,1,repeated=True)
