#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
   '所有学生的基类'
   stucount = 0
   pristucount = 0
   midstucount = 0

 
   def __init__(self, name, stu_no, class_no, gender):
      self.name = name
      self.stu_no = stu_no
      self.class_no = class_no
      self.gender = gender
      Student.stucount += 1
   
   def displaycount(self):
       print (Student.pristucount+Student.midstucount)
 
   def displayStudent(self):
       print ("Name : ", self.name,  ",Stu_no : ", self.stu_no, ",Class_no :", self.class_no, ",Gender :", self.gender)


class prinmaryStudent(Student):
    '小学生的基类'

    def __init__(self, name, stu_no, class_no, gender):
        self.name = name
        self.stu_no = stu_no
        self.class_no = class_no
        self.gender = gender
        Student.pristucount += 1

    def prinmaryname(self):
        print("the prinmartstuname is",name)

    def prinmaryclass_no(self):
        print("the prinmaryclass_no is",class_no)

    def displaypristucount(self):
       print (Student.pristucount)


class MiddleStudent(Student):
    '中学生的基类'
    midstucount = 0

    
    def __init__(self, name, stu_no, class_no, gender):
        self.name = name
        self.stu_no = stu_no
        self.class_no = class_no
        self.gender = gender
        Student.midstucount += 1
    def Chmistry(self):
        print(name," can chemistry")
        
    def Pyhics(self):
        print(name," can phhics")

    def displaymidstucount(self):
       print (Student.midstucount)
