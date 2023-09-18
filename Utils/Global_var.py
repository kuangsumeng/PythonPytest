import os

# Project root directory
# PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.getcwd(), "../.."))

# Testcases file storage path
TEST_CASE_DATA_DIR = os.path.join(PROJECT_ROOT_DIR, r'TestData\case.xlsx')

# Log file storage path
LOG_FILE = PROJECT_ROOT_DIR + "/log/" + "interface_auto_test.log"

# Information of login interface
HOST = "http://gateway.fxdd6678.cc"
PATH = "/game-server/game/api/v1/common/login"

# Userinfo
USER1 = 'Test001'
USER2 = 'Test002'
PASSWORD = 'a123456'

print(PROJECT_ROOT_DIR)
