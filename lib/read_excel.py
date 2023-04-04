import xlrd

from config.config import prj_path


def excel_to_list(data_file, sheet):
    """
    方法：读取excel表格的数据
    :param data_file: 文件名
    :param sheet: 文件的sheet
    :return: data_list
    """
    data_list = []  # 新建空列表，来存储所有的数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典


def get_test_data(data_list, case_name):
    """
    方法：获取到读取的数据
    :param data_list: 数据列表
    :param case_name: 用例名
    :return: case_data
    """
    for case_data in data_list:
        if case_name == case_data['case_name']:  # 如果字典数据中case_name与参数一致
            return case_data  # 返回查询结果，如果查询不到会返回None


if __name__ == '__main__':
    data_list = excel_to_list(prj_path + "/data/test_user_data.xlsx", "TestUserLogin")  # 读取excel，TestUserLogin工作簿的所有数据
    print(data_list)
    case_data = get_test_data(data_list, 'test_user_login_normal')  # 查找用例'test_user_login_normal'的数据
    print(case_data)
