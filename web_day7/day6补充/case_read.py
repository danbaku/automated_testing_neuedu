"""
作者：张浩
时间：2023/7/25  11:01
邮箱：88302599@qq.com
"""
import openpyxl

def read_case(file_path,sheet):
    wk = openpyxl.load_workbook(file_path)
    sh = wk[sheet]
    testcase=[]
    rows = list(sh.rows)#获取sheet页面所有行的对象
    keys=[]
    for key in rows[0]:#处理第一行，作为案例的key
        keys.append(key.value)#取出第一行单元格的值，加入到keys的列表

    for row in  rows[1:]:#从第二行处理案例文件的值
        values=[]
        for cell in row:#循环处理每一行中的单元格
            values.append(cell.value)#取出单元格的值，加入到values的列表
        case =dict(zip(keys,values))#通过zip把keys和values两个组合成字典，形成一条案例数据
        testcase.append(case)#把一条案例数据加入到testcase的列表中

    return testcase
