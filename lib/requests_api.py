# import json
# import logging
#
# import requests
#
# from config.config import prj_path
# from lib.read_excel import excel_to_list, get_test_data
#
#
# def get_api():
#     data_list = excel_to_list(prj_path + "/data/test_user_data.xlsx", "TestUserLogin")
#     case_data = get_test_data(data_list, "test_user_login_normal")
#     if not case_data:
#         logging.error("not have")
#     url = case_data.get("url")
#     data = case_data.get("data")
#     res1 = requests.post(url=url, data=json.loads(data))
#     res_json = res1.json()
#     return res_json
#
#
# if __name__ == '__main__':
#     get_ = get_api()
#     print(get_)
