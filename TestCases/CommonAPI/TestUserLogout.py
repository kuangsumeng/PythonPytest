# coding=gbk

from Utils.Excel_util import ExcelUtil
from Utils.Requests_util import RequestType
from Utils.Log_util import log_config_init
from Utils.Get_token import get_token
from Utils.Global_var import *
import os
import json
import pytest
import allure
import ast

excel = ExcelUtil('UserLogout')


@allure.feature("UserLogout")
class TestUserLogin:
    case_data = excel.get_sheet_data()
    log = log_config_init()

    @allure.story("UserLogout")
    @allure.title("UserLogout")
    @allure.description("Test the logout interface through different request parameters")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('cases', case_data)
    def test_user_login(self, cases):
        self.log.info("Calling interface data>>>{}".format(cases))
        self.log.info("Start assembling request header data")
        self.headers = ast.literal_eval(cases['header'])
        self.headers['Authorization'] = 'Bearer {}'.format(get_token(USER1))
        response = RequestType().get_request(cases['Request Method'], cases['URL'], headers=self.headers,
                                             params=ast.literal_eval(cases['params']))
        # Convert response data from str to dict
        test_res = json.loads(response)
        test_assert = test_res["resp_msg"]
        self.log.info("Request interface success")

        try:
            # Normal status to login user
            if test_res['resp_code'] == 0:
                assert 'succeed' == test_assert
                # Write the actual return value to the test case file and set the test result as pass
                excel.write_excel(cases["id"] + 1, response, "PASS")
                self.log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))
            else:
                self.log.error("请求失败 {}".format(response))
                excel.write_excel(cases["id"] + 1, response, "FAIL")

        except AssertionError as e:
            excel.write_excel(cases["id"] + 1, response, "FAIL")
            raise e


if __name__ == '__main__':
    pytest.main(["-s", "TestUserLogout.py", "--alluredir", "../../TestResult", "--clean-alluredir"])
    os.system("allure generate ../../TestResult -o  ../../TestReport --clean")
