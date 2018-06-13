import endpoints
from google.appengine.ext import ndb
from resources.users import ApiUser, ApiUsers, User
from protorpc import messages, message_types, remote
from apis.base import api_holder
from resources.countries import Country
import httplib

class ConflictException(endpoints.ServiceException):
  """Conflict exception that is mapped to a 409 response."""
  http_status = httplib.CONFLICT

NameResource = endpoints.ResourceContainer(
message_types.VoidMessage,
id=messages.IntegerField(1),
)

CountryResource = endpoints.ResourceContainer(
message_types.VoidMessage,
country=messages.StringField(1)
)

@api_holder.api_class(resource_name='Users',path='users')
class Users_Service(remote.Service):
    @endpoints.method(
    ApiUser,
    ApiUser,
    path="add",
    http_method="PUT",
    name="create",
    )
    def create(self,user):
        country = Country.get_by_id(user.country)
        if not country:
            raise endpoints.NotFoundException(
            "Error: Country assigned to user does not exist"
            )
        entity = User(
            name=user.name,
            parent=ndb.Key("Country",user.country),
        )
        key = entity.put()
        user.id = key.id()
        return user

    @endpoints.method(
    CountryResource,
    ApiUsers,
    path="list",
    http_method="GET",
    name="list",
    )
    def items_list(self,query):
        country = Country.get_by_id(user.country)
        if not country:
            raise endpoints.NotFoundException(
            "Error: Country searched does not exist "
            )
        parent = None
        if query.country:
            parent = ndb.Key("Country",query.country)
        entities = User.query(ancestor=parent).fetch()
        apiUserList = []
        for item in entities:
            apiUserList.append(ApiUser(
            name=item.name,
            country=item.key.parent().id(),
            id=item.key.id(),
            ))
        return ApiUsers(
        users=apiUserList
        )

    @endpoints.method(
    NameResource,
    message_types.VoidMessage,
    path='{id}',
    http_method='DELETE',
    name='delete'
    )
    def delete(self, user):
        entity = User.get_by_id(user.id)
        if not entity:
            raise endpoints.BadRequestException(
            "Error: This user is not registered in our system"
            )

        entity.key.delete()
        return message_types.VoidMessage();
