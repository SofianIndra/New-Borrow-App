from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

###
# Properties configurations
###

LIMIT = 30

ACTIVE_DATA = 'ACTIVE'

BLOCKED_DATA = 'BLOCKED'

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

config = Config(".env")

ROUTE_PREFIX_V1 = "/v1"

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

