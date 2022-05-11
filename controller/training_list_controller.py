import os
import pandas as pd
from Class import TrainingList, URL
from url_controller import set_this_request_url


def request_training_list(url: URL):
    res = url.get_response()

    if res:
        tl = TrainingList()
        tl.set_traininig_list_with_xml(res)

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

    order = {"DESC": "DESC", "ASC": "ASC"}

    url = URL()

    dfs = []
    for o in order.values():
        opt["sort"] = o
        opt["pageNum"] = "1"

        set_this_request_url(url, "training_list", opts=opt)
        tl = request_training_list(url)

        for i in range(2, 3):  # to MAX PAGE NUMBER
            opt["pageNum"] = str(i)

            set_this_request_url(url, "training_list", opts=opt)
            tmp = request_training_list(url)

            if tmp:
                tl.set_training_list(
                    pd.concat([tl.get_training_list(), tmp.get_training_list()], axis=0)
                )
        dfs.append(tl.get_training_list().copy(deep=True))

    return pd.concat(dfs, axis=0).drop_duplicates()

