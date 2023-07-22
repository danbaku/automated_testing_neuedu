"""
作者：张浩
时间：2023/7/19  10:55
邮箱：88302599@qq.com
"""

class MyClass():
    attr =100
    name = "zhanghao"
    age=40
    __a =1#私有属性

#-----------------------------动态设置类属性----------------------------------------
# k ="name1"
# v = "zhanghao"
# MyClass.k = v
# print(MyClass.name)
# setattr(MyClass,k,v)
# print(MyClass.name)
# print(MyClass.__dict__)

# dic1={'name':'张浩','age':20,'sex':'man'}

# dic1={'name':'张浩','age':20,'sex':'man'}
# for i in dic1.items():
#     print(i)
#     setattr(MyClass,i[0],i[1])
#
#
# print(MyClass.__dict__)


#-----------------------------动态获取类属性----------

x = "nameaa"

# print(MyClass.x)

print(getattr(MyClass,x,"没有此属性"))


#-----------------------------动态删除类属性---------------

x = "attr"

# print(MyClass.x)

delattr(MyClass,x)

print(MyClass.attr)