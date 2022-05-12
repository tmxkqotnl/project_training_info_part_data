from typing import Optional, Union
import pandas as pd
from bs4 import BeautifulSoup
import logging


class TrainingList:
    def __init__(self):
        self.__training_list: Optional[pd.DataFrame] = None
        self.__list_cnt = None

    def get_training_list(self):
        return self.__training_list

    def set_training_list(self, lst: pd.DataFrame):
        if not isinstance(lst, pd.DataFrame):
            logging.error("training list must be Dataframe")
            raise TypeError("training list must be Dataframe")

        self.__training_list = lst

    def get_list_cnt(self) -> Optional[int]:
        return self.__list_cnt

    def set_list_cnt(self, cnt: int):
        self.__list_cnt = cnt
