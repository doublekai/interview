"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from common.error.exceptions import BizException
from common.error.override import register_params_error_handler
from student.api import student_api
from student.authenticators import CustomHttpBearer

app = NinjaAPI(title="学生班级管理", description="跨链大数据平台后端API")
app.add_router("student", student_api, auth=CustomHttpBearer())
BizException.register(app)

register_params_error_handler(app)  # 全局捕获错误
urlpatterns = [path("", app.urls)]
