# Athour:Mr Xie
# 开发时间:2021/11/13 20:00
'''
1.创建Person、Student、Teacher类，具体要求如下
    1)创建Person类，该类中包含三种属性：姓名、性别、年龄以及针对每个属性的get和set方法；
    2)创建Student类，继承自Person类，添加额外三个属性：班级、学号。
    3)创建Teacher类，继承自Person类，添加额外三个属性：科室、工号。
    4)要求在Student类和Teacher类中分别实现printInfo方法，该方法打印对象的多个属性信息。
'''
#Person类
class Person(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
#name的get和set
    def getName(self):
        print(self.name)
    def setName(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print('name must be a string !')
#sex的get和set
    def getSex(self):
        print(self.sex)
    def setSex(self, sex):
        if sex in {'男', '女', 'man', 'men', 'woman', 'women', 'male', 'female'}:
            self.sex = sex
        else:
            print('sex must be these words: 男, 女, man, men, woman, women, male, female !')
#age的get和set
    def getAge(self):
        print(self.age)
    def setAge(self, age):
        if isinstance(age,int):
            self.age = age
        else:
            print('age must be an int!')

#Student类,添加额外三个属性：班级、学号。
class Student(Person):
    def __init__(self, name, sex, age, class_name, studentId,dormitory):
        super().__init__(name, sex, age)
        self.class_name = class_name
        self.studentId = studentId
        self.dormitory = dormitory

    def printInfo(self):  #name, sex, age, class_name, studentId,dormitory
        print('name:{0},sex:{1}, age:{2}, class_name:{3}, studentId:{4},dormitory:{5}'.format(self.name, self.sex, self.age, self.class_name, self.studentId,self.dormitory))

#Teacher类,添加额外三个属性：科室、工号。
class Teacher(Person):
    def __init__(self,name,sex,age,department,employeeId,dormitory):
        super().__init__(name,sex,age)
        self.department = department
        self.employeeId = employeeId
        self.dormitory = dormitory

    def printInfo(self):
        print("name:{0},sex:{1},age:{2},deaprtment:{3},employeeId:{4},dormitory:{5}".format(self.name,self.sex,self.age,self.department,self.employeeId,self.dormitory))


p1 = Person('xiaoming', 'man', 19)
p1.getName()
p1.setName('xiaoke')
p1.getName()

p1.getSex()
p1.setSex("woman")
p1.getSex()

p1.getAge()
p1.setAge(20)
p1.getAge()

s1 = Student('小可','man',19,'20级大数据管理与应用99班','2025080900','桃园')
s1.printInfo()

t1 = Teacher('小菲','female',26,'信息学院','3035080900','教师公寓')
t1.printInfo()
