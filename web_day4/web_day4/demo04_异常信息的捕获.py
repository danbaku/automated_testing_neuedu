"""
作者：张浩
时间：2023/7/19  13:33
邮箱：88302599@qq.com
"""
"""
try:
    可能会出现错误的代码(出现异常后，后续代码不会执行)
except:
    当try代码块中出现异常后，后续处理的逻辑代码
    如果需要获取异常信息，except Exception as e
    如果不需要处理异常，直接pass
else:
    当try代码块中没有出现异常后，后续处理的逻辑代码
finally:
    不论是否出现异常都会打印
"""

#-------------------捕获所有异常------------------------
# def add(a:int,b:int):
#     try:
#         c = a+b
#         print(c)
#     except:
#         print("参数类型不对！")
#
#
#
# # add(1,2)
# add("a",3)
# #

#-------------------捕获指定的异常------------
# try:
#     a="aaaa"
#     # res = int(a)
#     asdasdasd
# except NameError as e:
#     print("数据类型转换错误")



#------------------捕获异常不处理------------------------
# try:
#     a="aaaa"
#     # res = int(a)
#     asdasdasd
# except NameError as e:
#     pass

#------------------捕获异常并打印------
# try:
#     a="aaaa"
#     # res = int(a)
#     asdasdasd
# except NameError as e:
#     print(e)
#     print("处理异常")


try:
    print("---------1------------")
    print("---------2------------")
    print(aaa)
    print("---------4------------")
    print("---------5------------")
except Exception as e:
    print("AAAAAAA")
else:
    print("BBBBBB")
finally:
    print("CCCCC")
