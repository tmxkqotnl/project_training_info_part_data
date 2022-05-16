import logging
from time import sleep
from typing import Optional
import requests
from bs4 import BeautifulSoup

from libs import dict_to_query
from Class import URL


def get_full_url(url: URL) -> Optional[str]:
    try:
        return "?".join([url.get_url(), dict_to_query(url.get_parameter())])
    except Exception as e:
        logging.error(e)
        return None


def get_api_response(
    url: URL, encoding: str = "utf-8", feat: str = "xml"
) -> Optional[BeautifulSoup]:
    if not url.get_url():
        logging.debug("URL get_reponse ERROR")
        raise ValueError("request URL is None")

    try:
        res = requests.get(get_full_url(url))

        if feat == "xml":
            feat = "lxml-xml"
        elif feat == "html":
            feat = "lxml"

        xml = BeautifulSoup(res.content, feat, from_encoding=encoding)
        xml_error_check = xml.find("error")

        if xml_error_check:
            logging.error("xml error check")
            logging.error(xml)
            raise ValueError("parameter error")
        else:
            logging.debug("get reponse success")
            return xml
    # except requests.exceptions.Timeout as errd:
    #     logging.exception("Timeout Error : ", errd)
    # except requests.exceptions.ConnectionError as errc:
    #     logging.exception("Error Connecting : ", errc)
    # except requests.exceptions.HTTPError as errb:
    #     logging.exception("Http Error : ", errb)
    # Any Error except upper exception
    except requests.exceptions.MissingSchema as errm:
        logging.exception(erra)

        # temp
        sleep(1)
        get_api_response(url, encoding, feat)

    except requests.exceptions.RequestException as erra:
        logging.exception(erra)

        return None
    except ValueError:
        return None

