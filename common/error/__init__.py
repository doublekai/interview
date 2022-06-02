from .base import ERR

OK = ERR.register(200, "请求成功")
ERROR = ERR.register(400, "请求错误")
PARAM_VALIDATION_ERROR = ERR.register(422, "输入参数不正确")
INTERNAL_ERROR = ERR.register(500, "服务器内部出错请联系管理员")
LOGINREQUIRED = ERR.register(403, "登录信息过期或无效")