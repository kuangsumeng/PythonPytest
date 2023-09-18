from Utils.Excel_util import ExcelUtil
from Utils.Requests_util import RequestType
from Utils.Log_util import log_config_init
import os
import json
import pytest
import allure

excel = ExcelUtil('UserLogin')


@allure.feature("UserLogin")
class TestUserLogin:
    case_data = excel.get_sheet_data()
    log = log_config_init()

    @allure.story("UserLogin")
    @allure.title("UserLogin")
    @allure.description("Test the login interface through different request parameters")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('cases', case_data)
    def test_user_login(self, cases):
        self.log.info("Calling interface data>>>{}".format(cases))
        response = RequestType().get_request(cases['Request Method'], cases['URL'], json.loads(cases['header']),
                                             params=eval(cases['params']))
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

            # while the password error
            elif 'The password' in test_assert and test_res['resp_code'] == 1:
                # self.assertIn('The password is wrong', test_assert, msg='密码错误')
                assert 'The password is wrong' in test_assert
                excel.write_excel(cases["id"] + 1, response, "PASS")
                self.log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))

            # while the username error
            elif 'wrong user' in test_assert and test_res['resp_code'] == 1:
                assert 'wrong user name or password' == test_assert
                excel.write_excel(cases["id"] + 1, response, "PASS")
                self.log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))

            # while the username is empty
            elif test_res['resp_code'] == 1 and 'Account' in test_assert:
                assert 'Account cannot be empty' == test_assert
                excel.write_excel(cases["id"] + 1, response, "PASS")
                self.log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))

            # while the password is empty
            elif test_res['resp_code'] == 1 and 'blank' in test_assert:
                assert 'password can not be blank' == test_assert
                excel.write_excel(cases["id"] + 1, response, "PASS")
                self.log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))
            else:
                self.log.error("请求失败 {}".format(response))

        except AssertionError as e:
            excel.write_excel(cases["id"] + 1, response, "FAIL")
            raise e


if __name__ == '__main__':
    # '--clean-alluredir' parameter >>> Each run will clear the last generated data.
    pytest.main(["-s", "TestUserLogin.py", "--alluredir", "../../TestResult", "--clean-alluredir"])
    # '--clean' parameter >>> Clear the last generated report
    os.system("allure generate ../../TestResult -o  ../../TestReport --clean")
