from django.http import HttpRequest
from ninja import Query, Router

from common.base_schema import P, R
from common.error import OK
from student.dal import action
from student.schemas import StudentRequestSchema, StudentResponeSchema

student_api = Router(tags=["学生管理"])


@student_api.get("/student/info",
                 response=R[P[StudentResponeSchema]],
                 summary="获取学生信息")
def get_student_info(request: HttpRequest, query: StudentRequestSchema=Query(...)):
    """
        ## 获取学生信息
        - 根据输入的性别
        - TODO
        - 返回相应的学生及所属班级名称（数据库中学生人数近万，请考虑性能）
        

    """
    return OK(
        action.get_student_info(sex=query.sex,
                                page=query.page,
                                size=query.size))


@student_api.delete("/student/{id}/info", response=R, summary="删除学生信息")
def delete_student_info(request: HttpRequest,
                        id: int = Query(..., description="学生id")):

    return OK(action.delete_student_info(id=id))


@student_api.get("/fibnacci/{values}", response=R[int], summary="实现斐波那契数列")
def fibnacci(request: HttpRequest, values: int = Query(..., description="数值")):
    """
    ## 实现斐波那契数列
    -   提供计算Fibnacci数列的接口，输入为数字序号，输出为相应序号上的数字。同时确保该接口仅能被已登陆学生调用(请考虑框架)。
    -   提示：Fibnacci指如下数列：0、1、1、2、3、5、8、13、21、34，数学表达式为F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)。
    -   该接口输入n，输出F(n)。比如，输入5，则返回3；输入6，则返回5；输入7，则返回8。注意，这个F函数、Fibnacci数列是需要你自行实现的，请考虑算法时间复杂度！

    
    
    """

    return OK(action.fibnacci(values=values))


# @student_api.get("days",response=R[int],summary=)
# def get_days()