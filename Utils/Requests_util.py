from Utils.Log_util import log_config_init
from Utils.Global_var import *
import traceback
import requests

log = log_config_init()


class RequestType:

    @staticmethod
    def get_request(method, url, headers=None, params=None, files=None, json=None):
        """
        Choose to call different methods according to different request methods of the interface
        :param json: json request parameters
        :param method: requests method
        :param url: interface address
        :param headers: request header
        :param params: request parameters
        :param files: parameter with file
        :return: value of the interface returned
        """

        # Start to request
        try:
            if method == "get":
                resp = requests.get(url=HOST + url, headers=headers, params=params, json=json)
                log.info("Request data success")

            elif method == "post":
                resp = requests.post(url=HOST + url, headers=headers, params=params, files=files)
                log.info("Request data success")

            elif method == "put":
                resp = requests.put(url=HOST + url, headers=headers, data=params, files=files)
                log.info("Request data success")

            elif method == "delete":
                resp = requests.delete(url=HOST + url, headers=headers, data=params, files=files)
                log.info("Request data success")
            else:
                log.error(
                    "This request type {} is not supported, please check whether your request method is correct".format(
                        method))
                log.error(traceback.format_exc())
                raise
        except Exception:
            log.error(traceback.format_exc())
            raise

            # Convert resp.text into json
        return resp.text
