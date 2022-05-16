import pandas as pd
from Class.url import URL
from const import COMMON_CODE
from controller.url_controller import get_api_response
import json


def get_common_code(url: URL,save:bool=False):

    df = pd.DataFrame(columns=["코드값", "코드명", "구분"])

    for k, v in COMMON_CODE.items():
        url.set_parameter({"srchType": v})

        xml = get_api_response(url)

        c_name = [i.text for i in xml.findAll("rsltName")]
        c_val = [i.text for i in xml.findAll("rsltCode")]

        if c_name.__len__() != c_val.__len__():
            continue
        
        tmp = pd.DataFrame({"코드값": c_val, "코드명": c_name})
        if save:
            file_name = "../files/common_code/" + "_".join(k.split()) + ".csv"
            tmp.to_csv(file_name, index=False)

        tmp["구분"] = k
        df = pd.concat([df, tmp], axis=0, copy=True)

    # 훈련지역 중분류 코드 누락으로 수작업
    with open("../files/훈련지역_중분류_코드.json", "rb") as f:
        data = json.load(f)

        tmp = pd.DataFrame({"코드값": data["코드값"], "코드명": data["코드명"]})
        if save:
            tmp.to_csv("../files/common_code/훈련지역_중분류_코드.csv", index=False)

        tmp["구분"] = "훈련지역 중분류"

        df = pd.concat([df, tmp], axis=0, copy=True)

    return df
