from typing import Generic, List, Optional, TypeVar

from ninja import Field, Schema
from pydantic.generics import GenericModel

T = TypeVar("T")


class R(GenericModel, Generic[T]):

    code: int = Field(200, description="测试")
    msg: str = Field("成功", description="返回信息")
    data: Optional[T] = None


class P(GenericModel, Generic[T]):
    page: int = Field(1, description="页码")
    size: int = Field(10, description="页面容量")
    total: int = Field(0, description="总容量")
    data_list: List[T] = Field(default_factory=list, description="数据列表")


class PaginationSchema(Schema):
    page: int = Field(default=1, description="页码")
    size: int = Field(default=10, description="页面容量",lt=100)  #小于 100
