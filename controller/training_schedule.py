import logging
from bs4 import BeautifulSoup
import pandas as pd
from Class.url import URL

from controller.url_controller import get_response


def parse_xml_training_schedule(xml: BeautifulSoup) -> pd.DataFrame:
    lst = []
    for i in xml.findAll("scn_list"):
        eiEmplRate3 = i.find("eiEmplRate3")
        eiEmplCnt3 = i.find("eiEmplCnt3")
        eiEmplRate6 = i.find("eiEmplRate6")
        eiEmplCnt6 = i.find("eiEmplCnt6")
        hrdEmplRate6 = i.find("hrdEmplRate6")
        hrdEmplCnt6 = i.find("hrdEmplCnt6")
        instIno = i.find("instIno")
        totFxnum = i.find("totFxnum")
        totParMks = i.find("totParMks")
        totTrco = i.find("totTrco")
        trEndDt = i.find("trEndDt")
        trStaDt = i.find("trStaDt")
        trprDegr = i.find("trprDegr")

        lst.append(
            {
                "3개월_고용보험_취업률(pct)": eiEmplRate3.text
                if eiEmplRate3 is not None
                else None,
                "3개월_고용보험_취업인원": eiEmplCnt3.text if eiEmplCnt3 is not None else None,
                "6개월_고용보험_취업률(pct)": eiEmplRate6.text
                if eiEmplRate6 is not None
                else None,
                "6개월_고용보험_취업인원": eiEmplCnt6.text if eiEmplCnt6 is not None else None,
                "6개월_고용보험_미가입_취업률(pct)": hrdEmplRate6.text
                if hrdEmplRate6 is not None
                else None,
                "6개월_고용보험_미가입_취업인원": hrdEmplCnt6.text
                if hrdEmplCnt6 is not None
                else None,
                "훈련기관 코드": instIno.text if instIno is not None else None,
                "모집인원(정원)": totFxnum.text if totFxnum is not None else None,
                "수강인원": totParMks.text if totParMks is not None else None,
                "총_훈련비": totTrco.text if totTrco is not None else None,
                "훈련_시작일": trStaDt.text if trStaDt is not None else None,
                "훈련_종료일": trEndDt.text if trEndDt is not None else None,
                "훈련과정_회차": trprDegr.text if trprDegr is not None else None,
            }
        )
    return pd.DataFrame(lst)


def get_traininig_schedule_info(url: URL):
    return parse_xml_training_schedule(get_response(url, feat="xml"))

def get_training_schedule_info_list(url:URL,df:pd.DataFrame):
    
    if not ['훈련과정ID','훈련과정_순차'] in df.keys():
        logging.error('훈련과정ID, 훈련과정_순차 컬럼이 존재하지 않습니다.')
        raise AttributeError('훈련과정ID, 훈련과정_순차 컬럼이 존재하지 않음')
    
    df = df[['훈련과정ID','훈련과정_순차']]
    
    lst = []
    for i,n in df.values:
        params = url.get_parameter()
        params['srchTrprId'] = i
        if n is not None:
            params['srchTrprDegr'] = n
        
        get_training_schedule_info(url)