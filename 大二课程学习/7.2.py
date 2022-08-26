# Athour:Mr Xie
# 开发时间:2021/11/13 20:01
'''
2.士兵突击： solider(name height kg )冲锋，     weapon(AK47 AN94 M4A1)瞄准，射击，装弹
    1.士兵许三多有一把AK47
    2.士兵可以开火
    3.枪能够发射子弹
    4.枪装填子弹--增加子弹数量
'''
class gun():
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def reload(self,count):
        print("adding {0} bullets!".format(count))
        self.bullet_count += count

    def aim(self):
        print("Target confirm!")

    def shoot(self):
        if self.bullet_count <= 0:
            print("{0} lacking of ammunition!".format(self.model))
        else:
            print("{0} is shooting!".format(self.model))
            print("remaining {0} bullets!".format(self.bullet_count-1))
            self.bullet_count-1

class solider:
    def __init__(self,name,height,kg):
        self.name = name
        self.height = height
        self.kg = kg
        self.gun = None
        print("name:{0},height:{1},kg:{2} is coming!".format(self.name,self.height,self.kg))
    def fire(self):
        if self.gun == None:
            print("{0} has not gun yet!".format(self.name))
        elif  self.gun.bullet_count<=0:
            self.gun.reload(30)
        self.gun.aim()
        self.gun.shoot()


M4A1 = gun("M4A1")
xusanduo = solider("许三多",170,62)
xusanduo.gun = M4A1#对象之间的交互
xusanduo.fire()