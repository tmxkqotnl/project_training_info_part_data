import traceback
import logging

import requests

logger = logging.getLogger(__name__)

def dict_to_query(d: dict[str, str]):
    if len(d) == 0:
        return ''
    
    items = d.items()
    return "&".join(list(map(lambda x: "=".join(x), items)))

def logging_msg(exception_obj,msg):
    logging.error(msg)
    logging.debug(exception_obj)
    
def error_handler(func):
    def inner(*args, **kargs):
        try:
            return func(*args, **kargs)
        except TypeError as te:
            logging_msg(te,"TypeError Occured. Check Your Arguments or Variables ")
        except KeyError as ke:
            logging_msg(ke,"KeyError Occurred. Invalid Key is used")
        except ValueError as ve:
            logging_msg(ve,"Variable Type is not appropriate or None Type")
            return None
        except requests.exceptions.RequestException as re:
            logging_msg(re,"Requests Error Occured.")
            return None
        except Exception as e:
            logging_msg(e,"EXCEPTION HAS NO HANLDER")
        finally:
            logging.debug("Error Handling.. find me")
            logging.debug(traceback.format_exc())

    return inner

