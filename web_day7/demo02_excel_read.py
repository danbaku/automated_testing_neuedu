"""
作者：张浩
时间：2023/7/25  11:01
邮箱：88302599@qq.com
"""
#--------------------------两个列表组成字典zip--------------------------
# l1 = ["id","title","data","expect"]
# l2 = ["1","密码长度输入5位，登录失败",'{"user":"17768148441","pwd":"11111"}',"密码有效长度是6到30个字符","aaa","bb"]
# dic = dict(zip(l1,l2))
# print(dic)



# for n in range(len(l1)):
#     # dic[l1[n]]= l2[n]
#     # print(l1[n])
#     # print(l2[n])
#     dic[l1[n]]=l2[n]

#-----------------------------------------------------------------------
import openpyxl

def read_case(file_path,sheet):
    wk = openpyxl.load_workbook(file_path)

    sh = wk[sheet]
    testcase=[]
    rows = list(sh.rows)
    keys=[]
    for key in rows[0]:
        keys.append(key.value)
    for row in  rows[1:]:

        values=[]
        for cell in row:
            values.append(cell.value)
        case =dict(zip(keys,values))
        testcase.append(case)

    print(testcase)
