from typing import Optional


def get_url_splitted(url: str) -> (str, dict[str, str]):
    b_u, p = url.split("?")
    p = {j[0]: j[1] for j in [i.split("=") for i in p.split("&")]}

    return (b_u, p)


class URL:
    __url: Optional[str]
    __parameter: dict[str, str]

    def __init__(self):
        self.__url: Optional[str] = None
        self.__parameter = {}

    def get_url(self):
        return self.__url

    def set_url(self, url: str):
        if url.find("?") != -1:
            u, params = get_url_splitted(url)

            self.set_parameter(params)
            self.set_url(u)
        else:
            self.__url = url

    def get_parameter(self):
        return self.__parameter

    def set_parameter(self, dt: dict[str, str]):
        for k, v in dt.items():
            self.__parameter[k] = v

