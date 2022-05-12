import logging
import os
from typing import Optional
import pandas as pd
from url_controller import get_response
from Class import TrainingList, URL
from const import TRAINING_FOR_JOB_HUNTER


def get_list(url: URL) -> Optional[TrainingList]:
    xml = get_response(url)

    try:
        lst = xml.find("srchList").findAll("scn_list")

        tl = TrainingList()
        tl.set_list_cnt(int(xml.find("scn_cnt").text))
    except AttributeError as ae:
        logging.debug(ae)
        return None
    except Exception as e:
        logging.debug(e)
        return None

    n_lst = [
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
        for i in lst
    ]

    tl.set_training_list(pd.DataFrame(n_lst))
    return tl


def get_all_training_list():
    # 최대한 많이 가져오기 위해 sort와 sortcol을 이용한다.
    # 약 17만개 훈련과정
    # 한 번에 가져올 수 있는 양은 100 * 1000 = 10만
    # 정렬 순서를 바꾸어 두 dataframe을 합치고 중복을 제거한다.

    opt = {
        "authKey": os.getenv("HRD_API_KEY"),
        "returnType": "XML",  # only XML avaliable
        "outType": "1",  # 1 - list, 2 - detail / only list available
        "pageNum": "1",  # maximum 1000
        "pageSize": "100",  # maximum 100
        "sortCol": "TR_STT_DT",  # TOT_FXNUM - 모집인원, TR_STT_DT - 훈련시작일, TR_NM_i - 훈련과정명
        "srchTraStDt": "19700101",  # 훈련 시작일
        "srchTraEndDt": "20301231",  # 훈련 종료일
    }
    order = {"0": "DESC", "1": "ASC"}

    url = URL()

    dfs = []
    for o in order.values():
        opt["sort"] = o
        opt["pageNum"] = "1"

        url.set_url(TRAINING_FOR_JOB_HUNTER["info_list"])
        url.set_parameter(opt)
        tl = get_list(url)

        for i in range(2, 1001):  # to MAX PAGE NUMBER
            opt["pageNum"] = str(i)

            url.set_parameter(opt)
            tmp = get_list(url)

            if tmp:
                tl.set_training_list(
                    pd.concat([tl.get_training_list(), tmp.get_training_list()], axis=0)
                )
        dfs.append(tl.get_training_list().copy(deep=True))

    return pd.concat(dfs, axis=0).drop_duplicates()

