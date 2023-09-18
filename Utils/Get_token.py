from Utils.Log_util import log_config_init
from Utils.Global_var import *
import requests
import json
import traceback


def get_token(account):
    """
    Use the value of test_account in the global file to get the token value of test_account by
    calling the authentication interface.
    :param account:
    :return: user token
    """
    # Get a logger
    log = log_config_init()

    # Request interface address
    rq_url = HOST + PATH

    # Request header
    rq_headers = {
        "Content-Type": "application/json"
    }

    # Request data
    rq_data = {
        'username': account,
        'password': PASSWORD
    }
    log.info("User >>>{}<<< login success, get token info".format(USER1))
    try:
        response = requests.post(rq_url, headers=rq_headers, params=rq_data)
        log.info("Request success")
        result = json.loads(response.text)

        # Execute the Token acquisition operation through logical judgment
        if 'accessToken' in result['datas']:
            log.info("Get Token success")
            return result['datas']['accessToken']
        else:
            log.error('Failed to obtain Token data')
            log.error(traceback.format_exc())
            raise
    except Exception:
        log.error(traceback.format_exc())
        raise
