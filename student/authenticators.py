from typing import Any, Optional

from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from ninja.security import HttpBearer
from common.error import LOGINREQUIRED

class CustomHttpBearer(HttpBearer):

    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:

        if token ==  "doublekaitoken":
            return True
        else: 
            LOGINREQUIRED.throw()
