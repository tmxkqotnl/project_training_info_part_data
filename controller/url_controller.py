import logging
from time import sleep
from typing import Optional
import requests
from bs4 import BeautifulSoup

from libs import dict_to_query, error_handler
from Class import URL


def get_full_url(url: URL) -> str:
    base_url = url.get_url()
    if base_url is None:
        raise ValueError("URL is None")

    return "?".join([base_url, dict_to_query(url.get_parameter())])


@error_handler
def get_api_response(
    url: URL, encoding: str = "utf-8", feat: str = "xml"
) -> Optional[BeautifulSoup]:

    full_url = get_full_url(url)

    logging.debug("Tried URL : {}".format(full_url))
    res = requests.get(full_url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    })

    if feat == "xml":
        feat = "lxml-xml"
    elif feat == "html":
        feat = "lxml"

    xml = BeautifulSoup(res.content, feat, from_encoding=encoding)
    xml_error_check = xml.find("error")

    if xml_error_check:
        logging.warning("GET ERROR CODE")
        logging.warning(xml)
        raise requests.exceptions.RequestException(xml)
    else:
        logging.debug("Success to get API reponse")
        logging.debug(res.status_code)
        return xml

    # except requests.exceptions.Timeout as errd:
    #     logging.exception("Timeout Error : ", errd)
    # except requests.exceptions.ConnectionError as errc:
    #     logging.exception("Error Connecting : ", errc)
    # except requests.exceptions.HTTPError as errb:
    #     logging.exception("Http Error : ", errb)
    # Any Error except upper exception
    # except requests.exceptions.MissingSchema as errm:
    #     logging.exception(erra)

    #     # temp
    #     sleep(1)
    #     get_api_response(url, encoding, feat)

    # except requests.exceptions.RequestException as erra:
    #     logging.exception(erra)

    #     return None
    # except ValueError:
    #     return None

