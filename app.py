import endpoints
import apis.base

app = endpoints.api_server([
    apis.base.api_holder
])
