# Athour:Mr Xie
# 开发时间:2021/10/31 21:01
'''
类的定义： class 类名(基类):      基类可无
            属性1
            属性2
            ....
            def __init__(self,参数1,参数2....):   有参  python有参无参只能写一个
                self.属性1 = 参数1
                self.属性2 = 参数2
                ..........
            def __init__(self):             无参

            def show(self):
                print(self.属性1)
                print(self.属性2)
                ........
            def setValue(self,参数1,参数2...)
                self.属性1 = 参数1
                self.属性2 = 参数2
                ........

类的实例化： 对象名 = 类名([参数])
不同类的对象之间可以相互作用
所有实例方法都的第一个形参都是self，self代表当前对象，

静态方法（类方法），静态属性（类属性）：与实例无关，对象名或类名调用
    实例方法，实例属性：通过实例化才可调用，对象名调用
对象.：显示所有公开成员
对象._:显示类和对象的所有成员，包括私有成员
dir(对象)：查看指定对象，模块，命名空间的所有成员


类定义中用下划线定义成员名前缀和后缀表示类的特殊成员
1._xxx:一个下划线开头，类对象和子类可访问；模块使用__all__指明，可以导入
2.__xxx__:系统定义特殊成员，可改写，不可改名
3.__xxx:表示私有成员，类对象可访问，子类不可，对象外部：对象名名._类名__xxx访问
'''
class Empolyee(object):
    name = ''
    salary = 0
    def __init__(self, name, salary):
        print(name,salary)

    def updata(self):
        print("My car is needed to be updated!")
e1 = Empolyee('小可', 2000)
e1.updata()


class Test:
    '''This is only a test!'''
    pass         #关键字pass,用来占位，什么也不实现
print(Test.__doc__)   #查看帮助文档，即是上面的注释


