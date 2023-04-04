import logging
import unittest

from config.config import report_file, test_path
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import send_email

logging.info("====================== 测试开始 ======================")
suite = unittest.defaultTestLoader.discover(test_path)      # 运行测试用例

with open(report_file, 'wb') as f:  # 将运行测试用例写入报告（从配置文件中读取）
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="乔纳森").run(suite)

# send_email(report_file)  # 发送邮件（从配置文件中读取）
logging.info("====================== 测试结束 ======================")
