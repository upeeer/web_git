from fastapi import HTTPException

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from pydantic import validator
from basic_data import *
student = APIRouter()

#取固定id学生数据
@student.get('/{student_id}')
async def get_all_student(student_id:int):
    stu=await Student.get(id=student_id).values("name","clas__name","course__name")
    return stu


#取所有学生数据
@student.get('/')
async def getstudent():
    stu=await Student.all().values("name","clas__name","course__name")
    return stu

class Student_in(BaseModel):
    name : str
    pwd :str
    clas_id:int
    course:List[int]=[]

    @validator("name")
    def namevalidator(cls,value):
        assert value.isalpha(),"name must be alpha!"
        return value


#添加学生数据
@student.post('/')
async def add_student(student_in:Student_in):
    stu=await Student.create(
        name=student_in.name,
        clas_id=student_in.clas_id,
        pwd=student_in.pwd,
    )

    choose_course=await Course.filter(id__in=student_in.courses)
    #await stu.course.clear()
    await stu.course.add(*choose_course)

    return stu

#更新学生数据
@student.put('/{student_id}')
async def update_student(student_id:int,student_in:Student_in):
    data=student_in.dict()#基于student_in类属性与模型类属性命名一致，可以转化为字典快速传参
    courses=data.pop("course")#由于多对多关系需要单独更新，所以去除course并将其赋予courses列表
    await Student.filter(id=student_id).update(**data)#更新update,由于update函数里可加id限制，所以更新一般关系时不需要取对于id的学生queryset

    update_stu=await Student.get(id=student_id)#取student_id的对象列表（id为主键，一般唯一id，所以用get也行）
    # 更新多对多course
    choose_course=await Course.filter(id__in=courses)
    await update_stu.course.add(*choose_course)

    return update_stu


#取固定id学生数据
@student.delete('/{student_id}')
async def delete_student(student_id:int):
    deletecount=await Student.filter(id=student_id).delete()
    if not deletecount:
        raise HTTPException(status_code=404,detail=f"id为{student_id}的学生不存在")
    return "delete successfully!"
