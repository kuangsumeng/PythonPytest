import json
import traceback
import ast
from Log_util import log_config_init

log = log_config_init()


class JsonHandler:
    """
    Encapsulate JSON processing functions
    """

    # Convert Json data into dictionary object
    @staticmethod
    def json_to_dict(json_str):
        try:
            log.info("Convert Json data into dict object successful: {}".format(json_str))
            return ast.literal_eval(json_str)
        except Exception:
            log.error("Convert Json data into dic object fail: {}".format(json_str))
            log.error(traceback.format_exc())
            raise

    # Convert dictionary object into Json data
    @staticmethod
    def dict_to_json(dict_obj):
        try:
            log.info("Convert dict object into Json data successful: {}".format(dict_obj))
            return json.dumps(dict_obj, ensure_ascii=False)
        except Exception:
            log.error("Convert dict object into Json data fail: {}".format(dict_obj))
            log.error(traceback.format_exc())
            raise

    # Remove spaces from dictionary strings
    @staticmethod
    def remove_space_for_dict_str(dict_str: str):
        try:
            log.info("Remove space successful")
            return dict_str.replace(" ", "")
        except Exception:
            log.error("Remove space fail")
            log.error(traceback.format_exc())
            raise
