LOGGING_LEVEL = {"DEV": 10, "STAG": 30, "PROD": 40}

###########################################################

INFO_TYPE = {"목록": "1", "과정/기관정보": "2", "훈련일정": "3", "훈련생출결정보": "4"}

# HRD

### 구직자훈련과정 URL
TRAINING_FOR_JOB_HUNTER = {
    "1": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_1.jsp",  # 구직자훈련과정 목록
    "2": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_2.jsp",  # 구직자훈련과정 과정/기관정보
    "3": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_3.jsp",  # 구직자훈련과정 훈련일정
    "4": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_4.jsp",  # 구직자훈련과정 훈련생 출결정보
}

### 근로자 훈련과정 URL
TRAINING_FOR_WORKER = {
    "1": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA61/HRDPOA61_1.jsp",  # 근로자훈련과정 목록
    "2": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA61/HRDPOA61_2.jsp",  # 근로자훈련과정 과정/기관정보
    "3": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA61/HRDPOA61_3.jsp",  # 근로자훈련과정 훈련일정
    "4": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA61/HRDPOA61_4.jsp",  # 근로자훈련과정 훈련생 출결정보
}

### 기업 훈련과정 URL
TRAINING_FOR_ENTERPRISE = {
    "1": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA62/HRDPOA62_1.jsp",  # 기업훈련과정 목록
    "2": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA62/HRDPOA62_2.jsp",  # 기업훈련과정 과정/기관정보
    "3": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA62/HRDPOA62_3.jsp",  # 기업훈련과정 훈련일정
}

### 현재 비활성화된 과정 ###
### 중장년특화훈련과정
TRAINING_FOR_MIDDLE_AGED = {
    "1": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA64/HRDPOA64_1.jsp",  # 중장년특화훈련과정 목록
    "2": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA64/HRDPOA64_2.jsp",  # 중장년특화훈련과정 과정/기관정보
    "3": "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA64/HRDPOA64_3.jsp",  # 중장년특화훈련과정 훈련일정
}

# 과정/기관정보의 정보 타입
TRAINING_AGENCY_INFO_SEARCH_TYPE = {
    "목록": "default",
    "시설": "facility_detail",
    "장비": "eqnm_detail",
}


### 공통코드 URL
COMMON_CODE_URL = "https://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA90/HRDPOA90_1.jsp"

### 공통코드
COMMON_CODE = {
    "훈련지역 대분류 코드": "00",
    "훈련지역 중분류 코드": "01",
    "KECO 대분류 코드": "02",
    "KECO 중분류 코드": "03",
    "KECO 소분류 코드": "04",
    "NCS 대분류 코드": "05",
    "NCS 중분류 코드": "06",
    "NCS 소분류 코드": "07",
    "NCS 세분류 코드": "08",
    "훈련종류 코드": "09",
    "훈련방법 코드": "10",
    "훈련기관 구분코드": "11",
}

