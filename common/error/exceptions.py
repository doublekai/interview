import typing

from django.http import HttpRequest, HttpResponse, JsonResponse
from ninja import NinjaAPI

if typing.TYPE_CHECKING:
    from .base import ERR


class BizException(Exception):
    # Business Exception，指业务代码
    err: 'ERR'

    def __init__(self, err: 'ERR', *args: object) -> None:
        super().__init__(*args)
        self.err = err

    @classmethod
    def handler(cls, request: HttpRequest,
                exc: 'BizException') -> HttpResponse:
        return JsonResponse(exc.err.dict())

    @classmethod
    def register(cls, app: NinjaAPI):
        app.add_exception_handler(cls, cls.handler)
