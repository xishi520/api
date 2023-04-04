import logging
import os
import unittest
import requests
import json
import sys

from config.config import data_path
from lib.case_log import log_case_info
from lib.read_excel import excel_to_list, get_test_data

sys.path.append("../..")  # 提升2级到项目根目录下


class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"),
                                      "TestUserLogin")  # 读取TestUserReg工作簿的所有数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test1_user_login_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_login_normal')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res1 = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_normal', url, data, expect_res, res1.text)
        self.assertEqual(res1.text, expect_res)  # 断言
        return res1

    def test2_user_login_password_wrong(self):
        case_data = get_test_data(self.data_list, 'test_user_login_password_wrong')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res2 = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res2.text)
        self.assertEqual(res2.text, expect_res)  # 断言

    def test3_user_login_username_wrong(self):
        case_data = get_test_data(self.data_list, 'test_user_login_username_wrong')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res3 = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_username_wrong', url, data, expect_res, res3.text)
        self.assertEqual(res3.text, expect_res)  # 断言

    def test4_user_login_none(self):
        case_data = get_test_data(self.data_list, 'test_user_login_none')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res4 = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_none', url, data, expect_res, res4.text)
        self.assertEqual(res4.text, expect_res)  # 断言

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
