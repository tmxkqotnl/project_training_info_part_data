from Class import URL
from const import URLS
from libs import dict_to_query


def set_this_request_url(
    url: URL,
    target: str = "training_list",
    opts: dict[str, str] = {
        "authKey": "hfI6LTOnqD5609y88FO2DHzf2OGCuFeO",
        "returnType": "XML",  # only XML avaliable
        "outType": "1",  # 1 - list, 2 - detail
        "pageNum": "1",  # maximum 1000
        "pageSize": "100",  # maximum 100
        "sort": "ASC",
        "sortCol": "TR_STT_DT",  # TOT_FXNUM - 모집인원, TR_STT_DT - 훈련시작일, TR_NM_i - 훈련과정명
        "srchTraStDt": "19700101",  # 훈련 시작일
        "srchTraEndDt": "20221231",  # 훈련 종료일
    },
):
    url.set_request_url("?".join([URLS[target], dict_to_query(opts)]))
