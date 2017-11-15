#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, stu_no, class_no, gender):
      self.name = name
      self.stu_no = stu_no
      self.class_no = class_no
      self.gender = gender
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ",Stu_no : ", self.stu_no, ",Class_no :", self.class_no, ",Gender :", self.gender