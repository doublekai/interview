from ninja import Field, ModelSchema
from common.base_schema import PaginationSchema
from student.models import SEX, ClassModel, StudentModel
from django.contrib.auth.models import User
class StudentRequestSchema(PaginationSchema):
    sex: SEX = Field(None, description="用户名")
class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id','username']
class ClassSchema(ModelSchema):
    class Config:
        model = ClassModel
        model_fields = ['id','name']
class StudentResponeSchema(ModelSchema):
    user:UserSchema
    cs:ClassSchema
    
    class Config:
        model = StudentModel
        arbitrary_types_allowed=True
        model_fields = ['id', 'sex']
