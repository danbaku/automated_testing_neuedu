import openpyxl

def add_test_data(file_path, sheet):
    excel_data = openpyxl.load_workbook(file_path)
    sheet = excel_data[sheet]
    test_data = []
    title_data = [cell.value for cell in sheet[1]]   # 获取表头数据
    for row in sheet.iter_rows(min_row=2):   # 从第二行开始遍历数据
        row_data = [cell.value for cell in row]   # 获取当前行的数据
        case = dict(zip(title_data, row_data))   # 将表头和当前行的数据合并为字典
        test_data.append(case)
    return test_data