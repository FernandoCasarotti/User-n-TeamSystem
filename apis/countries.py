import endpoints
from resources.countries import ApiCountry, ApiCountries, Country
from protorpc import messages, message_types, remote
from apis.base import api_holder
import httplib

class ConflictException(endpoints.ServiceException):
  """Conflict exception that is mapped to a 409 response."""
  http_status = httplib.CONFLICT

NameResource = endpoints.ResourceContainer(
message_types.VoidMessage,
name=messages.StringField(1),
)

@api_holder.api_class(resource_name='Countries',path='countries')
class Countries_Service(remote.Service):
    @endpoints.method(
    ApiCountry,
    ApiCountry,
    path="add",
    http_method="PUT",
    name="create",
    )
    def create(self,country):
        entity = Country.get_by_id(country.name)
        if entity:
            raise ConflictException(
            "Error: Cannot register two countries with the same name"
            )
        entity = Country(
            id=country.name,
        )
        key = entity.put()
        country.id = key.id()
        return country

    @endpoints.method(
    message_types.VoidMessage,
    ApiCountries,
    path="list",
    http_method="GET",
    name="list",
    )
    def items_list(self,void):
        entities = Country.query().fetch()
        apiCountryList = []
        for item in entities:
            apiCountryList.append(ApiCountry(
            name=item.key.id(),
            id=item.key.id(),
            ))
        return ApiCountries(
        countries=apiCountryList
        )

    @endpoints.method(
    NameResource,
    message_types.VoidMessage,
    path='{name}',
    http_method='DELETE',
    name='delete'
    )
    def delete(self, country):
        entity = Country.get_by_id(country.name)
        if not entity:
            raise endpoints.BadRequestException(
            "Error: This country is not registered in our system"
            )

        entity.key.delete()
        return message_types.VoidMessage();
