class Girl:
    def __init__(self,age,name,zhaobei,tall,weight,school,first,baihu):
        self.age = age
        self.name = name
        self.zhaobei = zhaobei
        self.tall = tall
        self.weight = weight 
        self.school = school
        self.first = first
        self.baihu = baihu
        
    def get_info(self):
        
        print("The girl is {},{} years old,{} zhaobei,in {},and she is {} high,{}.she's first is {},she's baihu is {}".format(self.name,self.age,self.zhaobei,self.school,\
              self.tall,self.weight,self.first,self.baihu))
        
age = input("your age:")
name = input("name:")
zhaobei = input("zhaobei:")
tall = input("tall:")
weight = input("weight:")
school = input("school:")
first = input("first(True or False):")
baihu  = input("baihu(True or False):")


girl = Girl(age,name,zhaobei,tall,weight,school,first,baihu)
girl.get_info()

