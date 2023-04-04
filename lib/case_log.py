import json
import sys
from config.config import *

sys.path.append('..')


def log_case_info(case_name, url, data, expect_res, res):
    """方法：输出测试用例日志"""
    if isinstance(data, dict):  # 比较data是否是字典数据
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    logging.info("测试用例：{}".format(case_name))
    logging.info("URL：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res))
