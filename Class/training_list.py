from typing import Optional
import pandas as pd
from bs4 import BeautifulSoup
import logging


class TrainingList:
    def __init__(self):
        self.__training: Optional[pd.DataFrame] = None
        self.__list_cnt = None

    def get_training_list(self):
        return self.__training

    def set_training_list(self, lst: pd.DataFrame):
        self.__training = lst

    def set_traininig_list_with_xml(self, xml: BeautifulSoup):
        try:
            lst = xml.find("srchList").findAll("scn_list")
        except AttributeError as ae:
            logging.debug(ae)
            return None
            
        # 검색된 데이터 갯수 갱신
        self.__list_cnt = int(xml.find("scn_cnt").text)

        n_lst = []
        for i in lst:
            n_lst.append(
                {
                    "주소": i.find("address").text,
                    "컨텐츠": i.find("contents").text,
                    "수강비": i.find("courseMan").text,
                    # "고용보험3개월 취업인원 수": i.find("eiEmplCnt3").text,
                    # "고용보험3개월 취업률": i.find("eiEmplRate3").text,
                    # "고용보험6개월 취업률": i.find("eiEmplRate6").text,
                    "등급": i.find("grade").text,
                    # "제목 아이콘 구분": i.find("imgGubun").text,
                    "훈련기관 코드": i.find("instCd").text,
                    "NCS 코드": i.find("ncsCd").text,
                    "실제 훈련비": i.find("realMan").text,
                    "수강신청 인원": i.find("regCourseMan").text,
                    "정원": i.find("yardMan").text,
                    "제목": i.find("title").text,
                    # "제목 링크": i.find("titleLink").text,
                    # "제목 아이콘": i.find("titleIcon").text,
                    "부제목": i.find("subTitle").text,
                    # "부제목 링크": i.find("subTitleLink").text,
                    "주관부처": i.find("superViser").text,
                    "전화번호": i.find("telNo").text,
                    "훈련시작일자": i.find("traStartDate").text,
                    "훈련종료일자": i.find("traEndDate").text,
                    "훈련대상": i.find("trainTarget").text,
                    "훈련구분": i.find("trainTargetCd").text,
                    "훈련기관ID": i.find("trainstCstId").text,
                    "훈련과정ID": i.find("trprId").text,  # primary key
                    "훈련과정 순차": i.find("trprDegr").text,
                }
            )

        self.__training = pd.DataFrame(n_lst)

    def get_list_cnt(self) -> Optional[int]:
        return self.__list_cnt
