"""
作者：张浩
时间：2023/7/26  9:43
邮箱：88302599@qq.com
"""
import  os
#
# path=os.path.abspath("test.txt")#通过相对路径获得绝对路径
# print(path)
#
# # path=os.path.abspath(".")
# # print(path)
#
#
# fp = __file__#当前文件的文件名
# print(fp)


# path=os.path.abspath(__file__)#当前文件的绝对路径
# print(path)

# file_path=r"E:\class_2017\web_day7\test.txt"
#
# path2=os.path.dirname(file_path)#通文件的绝对路径，获得所在目录绝对路径
#
# print(path2)


path=os.path.abspath(__file__)#通过文件名获得文件的绝对路径

path2=os.path.dirname(os.path.abspath(__file__))
print(path2)