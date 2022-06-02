"""覆盖默认的异常，如422参数校验异常，"""

import traceback

from django.http import HttpRequest, HttpResponse, JsonResponse
from ninja import NinjaAPI
from ninja.errors import ValidationError

from common.error import INTERNAL_ERROR, PARAM_VALIDATION_ERROR


#  捕获所有的错误，输出错误堆栈
def all_exception_handler(request: HttpRequest, exc: Exception):
    return JsonResponse(
        INTERNAL_ERROR.inherit("内部错误，请联系管理员")(traceback.format_exc()).dict())


def handle_params_exception(request: HttpRequest,
                            exc: ValidationError) -> HttpResponse:
    return JsonResponse(PARAM_VALIDATION_ERROR.dict())


def register_params_error_handler(app: NinjaAPI):
    app.add_exception_handler(ValidationError, handle_params_exception)
    app.add_exception_handler(Exception, all_exception_handler)