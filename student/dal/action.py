# 签发access_token
from logging import Logger
from common.base_schema import P
from common.error import ERROR
from student.models import SEX, StudentModel
from student.schemas import StudentResponeSchema


def get_student_info(sex:SEX,page: int = 1, size: int = 10) -> P[StudentResponeSchema]:
    """
        1.根据性别，返回学生信息
        注意：学生表有上万条数据
    """

    qs = StudentModel.objects.filter(sex=sex)
    total = qs.count()
    data_list = [
        StudentResponeSchema.from_orm(i) for i in qs[page * size - size:size * page]
    ]
    return P(page=page, size=size, total=total, data_list=data_list)

def delete_student_info(id:int):
    """
        根据REST API删除Student表记录(关联的User表记录应被同时删除)。
        另外，所有删除API需要记录操作日志
    """
    try:
        stu= StudentModel.objects.get(id=id)
    except StudentModel.DoesNotExist:
        ERROR.inherit("删除失败 ").throw()
    stu.delete()
    Logger.debug(f"删除成功,记录日志，删除学生编号为{id}")

def fibnacci(values:int)-> int:
    if values == 1:  #判断前两项的返回的值
        return 0
    elif values == 2:
        return 1
    else:
        previous_tow=0
        previous=1 #初始化前两项
        result=0
        for i in range(2,values):
            result = previous+previous_tow  #fn=fn-1+fn-2
            previous_tow=previous   #fn-2=fn-1
            previous=result      #fn-1=fn
        return result

            

