"""
作者：张浩
时间：2023/7/26  10:02
邮箱：88302599@qq.com
"""

import  os

# path=os.path.abspath(__file__)#通过文件名获得文件的绝对路径
#
# path2=os.path.dirname(os.path.abspath(__file__))


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)


data_path= os.path.join(base_dir,"data")

print(data_path)
