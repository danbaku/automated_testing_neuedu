"""
作者：张浩
时间：2023/7/18  15:19
邮箱：88302599@qq.com
"""
"""
面向对象，万物皆对象
字符串、数值、列表、字典、元组、函数、类

属性
    

方法


"""


class Cat:
    eye = 2#类属性
    ear = 2
    leg = 4

    def skill_1(self):#对象方法
        print("抓老鼠")

    def skill_2(self):
        print("会爬树")



cat1 = Cat()
cat2 = Cat()
cat3 = Cat()


# print(cat1.leg)

cat1.name = "小白"#对象属性
cat2.name = "小黑"


# print(cat1.name)
# print(cat3.name)


# cat1.skill_1()
Cat.skill_1(cat1)