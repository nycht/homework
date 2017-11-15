#类定义
class people:
    name = ''
    age = 0
    weight = 0
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def name_agt_weight(self):
        print('姓名：',self.name,'年龄:',self.age,'体重:',self.weight)
