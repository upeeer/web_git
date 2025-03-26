from tortoise import fields
from tortoise.models import Model
class Student(Model):
    name=fields.CharField(max_length=32,description="学生姓名")
    id=fields.IntField(pk=True,description="学生ID")
    pwd=fields.CharField(max_length=12,description="学生用户密码")
    #一对多：
    clas=fields.ForeignKeyField("models.Clas",related_name="students") #该类多对一与该变量所属类：学生多对一班级
    #多对多：
    course=fields.ManyToManyField("models.Course",related_name="students")


class Clas(Model):
    id = fields.IntField(pk=True, description="班级ID")
    name=fields.CharField(max_length=32,description="班级名称",default="none")


class Course(Model):
    id = fields.IntField(pk=True, description="班级ID")
    name = fields.CharField(max_length=32, description="班级名称")
    # teacher=fields.ForeignKeyField("models.Teacher",related_name="courses")#
    #student=fields.ManyToManyField("models.Student",related_name="courses")

class Teacher(Model):
    name = fields.CharField(max_length=32, description="学生姓名")
    id = fields.IntField(pk=True, description="学生ID")
    pwd = fields.CharField(max_length=12, description="学生用户密码")
    course=fields.ForeignKeyField("models.Course",related_name="teachers")