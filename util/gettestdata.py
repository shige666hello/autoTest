import xlrd
from util.log import LogMessage  # 假设log_message是记录日志的函数

def fetch_test_cases(filepath, index=0):
    try:
        logs = LogMessage()  # 初始化日志记录器

        # 打开工作簿
        workbook = xlrd.open_workbook(filepath)
        sheet = workbook.sheet_by_index(index)

        # 初始化列表以存储测试用例
        test_cases = []

        # 遍历行数，从第二行开始（假设第一行是标题）
        for row in range(1, sheet.nrows):
            # 初始化每个测试用例的字典
            test_case = {
                'id': sheet.cell_value(row, 0),  # 假设ID在第一列
            }

            # 从第3列和第4列获取参数（假设第3列和第4列包含可评估的字典）
            try:
                test_case.update(eval(sheet.cell_value(row, 2)))  # 更新第3列的数据
                test_case.update(eval(sheet.cell_value(row, 3)))  # 更新第4列的数据
            except Exception as e:
                logs.error_log(f'第{row + 1}行数据评估失败：{e}')
                continue

            # 将构建好的测试用例字典添加到列表中
            test_cases.append(test_case)

        return test_cases

    except Exception as e:
        logs.error_log(f'从{filepath}获取测试用例失败：{e}')

# 示例用法:
filepath = "/Users/tal/Desktop/testTools/python-selenium/data/case.xlsx"
test_cases = fetch_test_cases(filepath)
print(test_cases)
