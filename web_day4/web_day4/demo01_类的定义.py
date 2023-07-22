"""
作者：张浩
时间：2023/7/18  15:19
邮箱：88302599@qq.com
"""
"""
面向对象，万物皆对象
字符串、数值、列表、字典、元组、函数、类

属性
    类属性的含义:表示一类事物都具备的属性，且属性值一致，所有类的实例化对象，都具备类属性
    类属性的定义:直接在类里的变量
    类属性的调用:可以通过类或者对象直接调用
    
    对象属性的含义:表示一个对象自身的特征
    对象属性的定义:对象名称.属性名= 属性值
    对象属性的调用:只能通过对象名称调用，不能通过类名调用;在对象属性与类属性同名时，优先调用对象属性

方法
    对象方法的定义：直接定义在类里的普通方法
    对象方法的调用：只能通过对象名称调用，不能通过类名调用
    self：对象方法必须要有的参数，self代表对象本身，哪个对象调用，self就代表哪个对象
"""


class Cat:
    eye = 2#类属性
    ear = 2
    leg = 4

    def skill_1(self):#对象方法
        print("抓老鼠")

    def skill_2(self):
        print("会爬树")

    def fun(self):
        print(self.name)



cat1 = Cat()
cat2 = Cat()
cat3 = Cat()

# cat1.leg=5
# print(cat1.leg)
# print(cat2.leg)
# print(cat1.leg)
#
# cat1.name = "小白"#对象属性
# cat2.name = "小黑"


# print(cat1.name)
# print(cat3.name)


# cat1.skill_1()
# Cat.skill_1(cat1)


cat1.name = "小白"
cat2.name = "小黑"
cat3.name = "小灰"

cat1.fun()
cat2.fun()
cat3.fun()