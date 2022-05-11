import logging
from typing import Optional

import requests
import lxml
from bs4 import BeautifulSoup


class URL:
    __request_url: Optional[str]

    def __init__(self):
        self.__request_url = None

    def get_request_url(self):
        return self.__request_url

    def set_request_url(
        self, r_url: str,
    ):
        self.__request_url = r_url

    def get_response(self) -> Optional[BeautifulSoup]:
        if not self.__request_url:
            logging.debug("URL get_reponse ERROR")
            raise ValueError("request URL is None")

        try:
            res = requests.get(self.__request_url)
            xml = BeautifulSoup(res.content, "lxml-xml")

            xml_error_check = xml.find("error")
            if xml_error_check:
                logging.error(xml_error_check.text)
                raise ValueError("parameter error")
            else:
                logging.debug('get reponse success')
                return xml
        # except requests.exceptions.Timeout as errd:
        #     logging.exception("Timeout Error : ", errd)
        # except requests.exceptions.ConnectionError as errc:
        #     logging.exception("Error Connecting : ", errc)
        # except requests.exceptions.HTTPError as errb:
        #     logging.exception("Http Error : ", errb)
        # Any Error except upper exception
        except requests.exceptions.RequestException as erra:
            logging.exception("Exception : ", erra)
            return None
        except ValueError:
            return None
