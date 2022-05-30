import logging
from typing import Optional
from bs4 import BeautifulSoup
import pandas as pd
from url_controller import get_api_response
from Class import URL
from const import TRAINING_FOR_JOB_HUNTER


def parse_training_list_for_job_hunter(scn_list: list[BeautifulSoup]) -> pd.DataFrame:
    n_lst = []
    for i in scn_list:
        address = i.find("address")
        contents = i.find("contents")
        courseMan = i.find("courseMan")

        eiEmplCnt3 = i.find("eiEmplCnt3")
        eiEmplRate3 = i.find("eiEmplRate3")
        eiEmplRate6 = i.find("eiEmplRate6")

        grade = i.find("grade")
        imgGubun = i.find("imgGubun")
        instCd = i.find("instCd")

        ncsCd = i.find("ncsCd")
        realMan = i.find("realMan")
        regCourseMan = i.find("regCourseMan")

        subTitle = i.find("subTitle")
        subTitleLink = i.find("subTitleLink")
        superViser = i.find("superViser")

        telNo = i.find("telNo")
        title = i.find("title")
        titleIcon = i.find("titleIcon")
        titleLink = i.find("titleLink")

        traEndDate = i.find("traEndDate")
        traStartDate = i.find("traStartDate")

        trainTarget = i.find("trainTarget")

        trainTargetCd = i.find("trainTargetCd")
        trainstCstId = i.find("trainstCstId")

        trprDegr = i.find("trprDegr")
        trprId = i.find("trprId")

        yardMan = i.find("yardMan")

        n_lst.append(
            {
                "주소": address.text if address is not None else None,
                "컨텐츠": contents.text if contents is not None else None,
                "수강비": courseMan.text if courseMan is not None else None,
                "고용보험3개월 취업인원 수": eiEmplCnt3.text if eiEmplCnt3 is not None else None,
                "고용보험3개월 취업률": eiEmplRate3.text if eiEmplRate3 is not None else None,
                "고용보험6개월 취업률": eiEmplRate6.text if eiEmplRate6 is not None else None,
                "등급": grade.text if grade is not None else None,
                "제목 아이콘 구분": imgGubun.text if imgGubun is not None else None,
                "훈련기관_코드": instCd.text if instCd is not None else None,
                "NCS_코드": ncsCd.text if ncsCd is not None else None,
                "실제_훈련비": realMan.text if realMan is not None else None,
                "수강신청_인원": regCourseMan.text if regCourseMan is not None else None,
                "부제목": subTitle.text if subTitle is not None else None,
                "부제목 링크": subTitleLink.text if subTitleLink is not None else None,
                "주관부처": superViser.text if superViser is not None else None,
                "전화번호": telNo.text if telNo is not None else None,
                "제목": title.text if title is not None else None,
                "제목 아이콘": titleIcon.text if titleIcon is not None else None,
                "제목 링크": titleLink.text if titleLink is not None else None,
                "훈련시작시작일자": traStartDate.text if traStartDate is not None else None,
                "훈련시작종료일자": traEndDate.text if traEndDate is not None else None,
                "훈련대상": trainTarget.text if trainTarget is not None else None,
                "훈련구분": trainTargetCd.text if trainTargetCd is not None else None,
                "훈련기관ID": trainstCstId.text if trainstCstId is not None else None,
                "훈련과정_순차": trprDegr.text if trprDegr is not None else None,
                "훈련과정ID": trprId.text if trprId is not None else None,
                "정원": yardMan.text if yardMan is not None else None,
            }
        )

    return pd.DataFrame(n_lst)


def parse_training_list_for_worker(scn_list: list[BeautifulSoup]) -> pd.DataFrame:
    n_lst = []
    for i in scn_list:
        address = i.find("address")
        contents = i.find("contents")
        courseMan = i.find("courseMan")
        grade = i.find("grade")

        imgGubun = i.find("imgGubun")
        instCd = i.find("instCd")
        ncsCd = i.find("ncsCd")
        realMan = i.find("realMan")

        regCourseMan = i.find("regCourseMan")
        subTitle = i.find("subTitle")
        subTitleLink = i.find("subTitleLink")
        superViser = i.find("superViser")
        telNo = i.find("telNo")

        title = i.find("title")
        titleIcon = i.find("titleIcon")
        titleLink = i.find("titleLink")

        traEndDate = i.find("traEndDate")
        traStartDate = i.find("traStartDate")

        trainTarget = i.find("trainTarget")
        trainTargetCd = i.find("trainTargetCd")
        trainstCstId = i.find("trainstCstId")

        trprDegr = i.find("trprDegr")
        trprId = i.find("trprId")

        yardMan = i.find("yardMan")

        n_lst.append(
            {
                "주소": address.text if address is not None else None,
                "컨텐츠": contents.text if contents is not None else None,
                "수강비": courseMan.text if courseMan is not None else None,
                "등급": grade.text if grade is not None else None,
                "제목 아이콘 구분": imgGubun.text if imgGubun is not None else None,
                "훈련기관_코드": instCd.text if instCd is not None else None,
                "NCS_코드": ncsCd.text if ncsCd is not None else None,
                "실제_훈련비": realMan.text if realMan is not None else None,
                "수강신청_인원": regCourseMan.text if regCourseMan is not None else None,
                "부제목": subTitle.text if subTitle is not None else None,
                "부제목 링크": subTitleLink.text if subTitleLink is not None else None,
                "주관부처": superViser.text if superViser is not None else None,
                "전화번호": telNo.text if telNo is not None else None,
                "제목": title.text if title is not None else None,
                "제목 아이콘": titleIcon.text if titleIcon is not None else None,
                "제목 링크": titleLink.text if titleLink is not None else None,
                "훈련시작종료일자": traEndDate.text if traEndDate is not None else None,
                "훈련시작시작일자": traStartDate.text if traStartDate is not None else None,
                "훈련대상": trainTarget.text if trainTarget is not None else None,
                "훈련구분": trainTargetCd.text if trainTargetCd is not None else None,
                "훈련기관ID": trainstCstId.text if trainstCstId is not None else None,
                "훈련과정_순차": trprDegr.text if trprDegr is not None else None,
                "훈련과정ID": trprId.text if trprId is not None else None,
                "정원": yardMan.text if yardMan is not None else None,
            }
        )

    return pd.DataFrame(n_lst)


def parse_training_list_for_enterprise(scn_list: list[BeautifulSoup]) -> pd.DataFrame:
    n_lst = []
    for i in scn_list:
        address = i.find("address")
        contents = i.find("contents")
        courseMan = i.find("courseMan")
        grade = i.find("grade")

        imgGubun = i.find("imgGubun")

        instCd = i.find("instCd")
        ncsCd = i.find("ncsCd")
        realMan = i.find("realMan")
        regCourseMan = i.find("regCourseMan")
        subTitle = i.find("subTitle")
        subTitleLink = i.find("subTitleLink")
        superViser = i.find("superViser")
        telNo = i.find("telNo")

        title = i.find("title")
        titleIcon = i.find("titleIcon")
        titleLink = i.find("titleLink")

        traEndDate = i.find("traEndDate")
        traStartDate = i.find("traStartDate")

        trainTarget = i.find("trainTarget")
        trainTargetCd = i.find("trainTargetCd")
        trainstCstId = i.find("trainstCstId")
        trprDegr = i.find("trprDegr")
        trprId = i.find("trprId")

        yardMan = i.find("yardMan")
        n_lst.append(
            {
                "주소": address.text if address is not None else None,
                "컨텐츠": contents.text if contents is not None else None,
                "수강비": courseMan.text if courseMan is not None else None,
                "등급": grade.text if grade is not None else None,
                "제목 아이콘 구분": imgGubun.text if imgGubun is not None else None,
                "훈련기관_코드": instCd.text if instCd is not None else None,
                "NCS_코드": ncsCd.text if ncsCd is not None else None,
                "실제_훈련비": realMan.text if realMan is not None else None,
                "수강신청_인원": regCourseMan.text if regCourseMan is not None else None,
                "부제목": subTitle.text if subTitle is not None else None,
                "부제목 링크": subTitleLink.text if subTitleLink is not None else None,
                "주관부처": superViser.text if superViser is not None else None,
                "전화번호": telNo.text if telNo is not None else None,
                "제목": title.text if title is not None else None,
                "제목 아이콘": titleIcon.text if titleIcon is not None else None,
                "제목 링크": titleLink.text if titleLink is not None else None,
                "훈련시작종료일자": traEndDate.text if traEndDate is not None else None,
                "훈련시작시작일자": traStartDate.text if traStartDate is not None else None,
                "훈련대상": trainTarget.text if trainTarget is not None else None,
                "훈련구분": trainTargetCd.text if trainTargetCd is not None else None,
                "훈련기관ID": trainstCstId.text if trainstCstId is not None else None,
                "훈련과정_순차": trprDegr.text if trprDegr is not None else None,
                "훈련과정ID": trprId.text if trprId is not None else None,
                "정원": yardMan.text if yardMan is not None else None,
            }
        )

    return pd.DataFrame(n_lst)


def parse_training_list(scn_list: list[BeautifulSoup]) -> pd.DataFrame:
    n_lst = []
    for i in scn_list:
        address = i.find("address")
        contents = i.find("contents")
        courseMan = i.find("courseMan")
        eiEmplCnt3 = i.find("eiEmplCnt3")
        eiEmplRate3 = i.find("eiEmplRate3")
        eiEmplRate6 = i.find("eiEmplRate6")
        grade = i.find("grade")
        imgGubun = i.find("imgGubun")
        instCd = i.find("instCd")
        ncsCd = i.find("ncsCd")
        realMan = i.find("realMan")
        regCourseMan = i.find("regCourseMan")
        yardMan = i.find("yardMan")
        title = i.find("title")
        titleLink = i.find("titleLink")
        titleIcon = i.find("titleIcon")
        subTitle = i.find("subTitle")
        subTitleLink = i.find("subTitleLink")
        superViser = i.find("superViser")
        telNo = i.find("telNo")
        traStartDate = i.find("traStartDate")
        traEndDate = i.find("traEndDate")
        trainTarget = i.find("trainTarget")
        trainTargetCd = i.find("trainTargetCd")
        trainstCstId = i.find("trainstCstId")
        trprId = i.find("trprId")
        trprDegr = i.find("trprDegr")

        n_lst.append(
            {
                "주소": address.text if address is not None else None,
                "컨텐츠": contents.text if contents is not None else None,
                "수강비": courseMan.text if courseMan is not None else None,
                "고용보험3개월 취업인원 수": eiEmplCnt3.text if eiEmplCnt3 is not None else None,
                "고용보험3개월 취업률": eiEmplRate3.text if eiEmplRate3 is not None else None,
                "고용보험6개월 취업률": eiEmplRate6.text if eiEmplRate6 is not None else None,
                "등급": grade.text if grade is not None else None,
                "제목 아이콘 구분": imgGubun.text if imgGubun is not None else None,
                "훈련기관_코드": instCd.text if instCd is not None else None,
                "NCS_코드": ncsCd.text if ncsCd is not None else None,
                "실제_훈련비": realMan.text if realMan is not None else None,
                "수강신청_인원": regCourseMan.text if regCourseMan is not None else None,
                "정원": yardMan.text if yardMan is not None else None,
                "제목": title.text if title is not None else None,
                "제목 링크": titleLink.text if titleLink is not None else None,
                "제목 아이콘": titleIcon.text if titleIcon is not None else None,
                "부제목": subTitle.text if subTitle is not None else None,
                "부제목 링크": subTitleLink.text if subTitleLink is not None else None,
                "주관부처": superViser.text if superViser is not None else None,
                "전화번호": telNo.text if telNo is not None else None,
                "훈련시작시작일자": traStartDate.text if traStartDate is not None else None,
                "훈련시작종료일자": traEndDate.text if traEndDate is not None else None,
                "훈련대상": trainTarget.text if trainTarget is not None else None,
                "훈련구분": trainTargetCd.text if trainTargetCd is not None else None,
                "훈련기관ID": trainstCstId.text if trainstCstId is not None else None,
                "훈련과정ID": trprId.text if trprId is not None else None,
                "훈련과정_순차": trprDegr.text if trprDegr is not None else None,
            }
        )

    return pd.DataFrame(n_lst)


def get_training_list(url: URL) -> Optional[pd.DataFrame]:
    xml = get_api_response(url)
    if xml is None:
        logging.debug("get_training_list canceled")
        return None

    scn_list = xml.find("srchList").findAll("scn_list")
    return parse_training_list(scn_list) if len(scn_list) != 0 else None

def get_target_training_list(url:URL,target:str):
    if target not in ['구직자','근로자','기업']:
        return None
    
    xml = get_api_response(url)
    if xml is None:
        logging.debug("get_training_list canceled")
        return None

    scn_list = xml.find("srchList").findAll("scn_list")
    
    func = None
    if target == '구직자':
        func = parse_training_list_for_job_hunter
    elif target == '근로자':
        func = parse_training_list_for_worker
    elif target == '기업':
        func = parse_training_list_for_enterprise
        
    return func(scn_list=scn_list)