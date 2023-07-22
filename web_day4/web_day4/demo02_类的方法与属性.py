"""
作者：张浩
时间：2023/7/19  10:28
邮箱：88302599@qq.com
"""
"""
方法
    类方法的定义：在类中方法上加@classmethod，把self改成cls
    类方法的调用：对象名称和类名称都可以调用
    cls：类方法必须要有的参数，cls代表类本身

    静态方法的定义：在类中方法上加@staticmethod，不加任何参数
    静态方法的调用：对象名称和类名称都可以调用
   
"""

class Cat:
    eye = 2#类属性
    ear = 2
    leg = 4

    def __init__(self,mz,ys):#魔术方法
        self.name = mz
        self.color = ys


    def skill_1(self):#对象方法
        print("抓老鼠")
        self.skill_4()

    def skill_2(self):
        print("会爬树")

    @classmethod
    def skill_3(cls):#类方法
        print("会猫叫")
        cls.skill_4()

    @classmethod
    def skill_4(cls):#类方法
        print("会呼吸")

    @staticmethod
    def fun():#静态方法
        print("---------静态方法--------------")

cat1 = Cat("小白","白色")
cat2 = Cat("小黑","黑色")
cat3 = Cat("小灰","灰色")


print(cat1.name)
print(cat2.name)
# cat1.skill_3()
# cat1.skill_1()
#
# cat1.name = "小白"
# cat2.name = "小黑"
# cat3.name = "小灰"
#
#
# cat1.color = "白色"
# cat2.color = "黑色"
# cat1.color = "灰色"
