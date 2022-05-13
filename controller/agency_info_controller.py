from bs4 import BeautifulSoup


def parse_xml_agency_info_default(xml: BeautifulSoup):  ## 기본
    instIno = xml.find("instIno")
    addr1 = xml.find("addr1")
    addr2 = xml.find("addr2")
    filePath = xml.find("filePath")
    hpAddr = xml.find("hpAddr")

    inoNm = xml.find("inoNm")

    instPerTrco = xml.find("instPerTrco")

    ncsCd = xml.find("ncsCd")
    ncsNm = xml.find("ncsNm")
    ncsYn = xml.find("ncsYn")
    nonNcsCoursePrcttqTime = xml.find("nonNcsCoursePrcttqTime")
    nonNcsCourseTheoryTime = xml.find("nonNcsCourseTheoryTime")

    pFileName = xml.find("pFileName")

    perTrco = xml.find("perTrco")
    torgParGrad = xml.find("torgParGrad")

    traingMthCd = xml.find("traingMthCd")

    trprChap = xml.find("trprChap")
    trprChapEmail = xml.find("trprChapEmail")
    trprChapTel = xml.find("trprChapTel")

    trprDegr = xml.find("trprDegr")
    trprGbn = xml.find("trprGbn")
    trprId = xml.find("trprId")
    trprNm = xml.find("trprNm")

    trprTarget = xml.find("trprTarget")
    trprTargetNm = xml.find("trprTargetNm")

    trtm = xml.find("trtm")
    trDcnt = xml.find("trDcnt")

    zipCd = xml.find("zipCd")

    govBusiNm = xml.find("govBusiNm")
    torgGbnCd = xml.find("torgGbnCd")
    totTraingDyct = xml.find("totTraingDyct")
    totTraingTime = xml.find("totTraingTime")
    totalCrsAt = xml.find("totalCrsAt")
    trprDegr = xml.find("trprDegr")
    trprId = xml.find("trprId")
    trprNm = xml.find("trprNm")

    return {
        "주소지": addr1.text if addr1 else None,
        "상세주소": addr2.text if addr2 else None,
        "파일경로": filePath.text if filePath else None,
        "홈페이지_주소": hpAddr.text if hpAddr else None,
        "훈련기관명": inoNm.text if inoNm else None,
        "훈련기관_코드": instIno.text if instIno else None,
        "실제_훈련비": instPerTrco.text if instPerTrco else None,
        "NCS코드": ncsCd.text if ncsCd else None,
        "NCS명": ncsNm.text if ncsNm else None,
        "NCS여부": ncsYn.text if ncsYn else None,
        "비NCS교과_실기시간": nonNcsCoursePrcttqTime.text if nonNcsCoursePrcttqTime else None,
        "비NCS교과_이론시간": nonNcsCourseTheoryTime.text if nonNcsCourseTheoryTime else None,
        "로고파일명": pFileName.text if pFileName else None,
        "정부지원금": perTrco.text if perTrco else None,
        "평가등급": torgParGrad.text if torgParGrad else None,
        "훈련방법코드": traingMthCd.text if traingMthCd else None,
        "담당자명": trprChap.text if trprChap else None,
        "담당자_이메일": trprChapEmail.text if trprChapEmail else None,
        "담당자_전화번호": trprChapTel.text if trprChapTel else None,
        "훈련과정회차": trprDegr.text if trprDegr else None,
        "훈련과정구분": trprGbn.text if trprGbn else None,
        "훈련과정ID": trprId.text if trprId else None,
        "훈련과정명": trprNm.text if trprNm else None,
        "주요_훈련과정_구분": trprTarget.text if trprTarget else None,
        "주요_훈련과정_구분명": trprTargetNm.text if trprTargetNm else None,
        "총_훈련시간": trtm.text if trtm else None,
        "총_훈련일수": trDcnt.text if trDcnt else None,
        "우편번호": zipCd.text if zipCd else None,
        ## 상세
        "훈련분야명": govBusiNm.text if govBusiNm else None,
        "훈련종류": torgGbnCd.text if torgGbnCd else None,
        "훈련일수": totTraingDyct.text if totTraingDyct else None,
        "훈련시간": totTraingTime.text if totTraingTime else None,
        "수강료": totalCrsAt.text if totalCrsAt else None,
        "훈련과정회차": trprDegr.text if trprDegr else None,
        "훈련과정코드": trprId.text if trprId else None,
        "훈련과정명": trprNm.text if trprNm else None,
    }


def parse_xml_agency_info_facility_detail(xml: BeautifulSoup):
    lst = []

    instIno = xml.find("instIno")
    for k in xml.findAll("inst_facility_info_list"):
        cstmrNm = k.find("cstmrNm")
        fcltyArCn = k.find("fcltyArCn")
        ocuAcptnNmprCn = k.find("ocuAcptnNmprCn")
        trafcltyNm = k.find("trafcltyNm")

        lst.append(
            {
                "훈련기관_코드": instIno.text if instIno else None,
                "등록훈련기관": cstmrNm.text if cstmrNm else None,
                "시설면적(m*m)": fcltyArCn.text if fcltyArCn else None,
                "인원(명)": ocuAcptnNmprCn.text if ocuAcptnNmprCn else None,  # 수용인원
                "시설명": trafcltyNm.text if trafcltyNm else None,
            }
        )

    return lst


def parse_xml_agency_info_facility_detail(xml: BeautifulSoup):
    lst = []

    instIno = xml.find("instIno")
    for k in xml.findAll("inst_facility_info_list"):
        cstmrNm = k.find("cstmrNm")
        fcltyArCn = k.find("fcltyArCn")
        ocuAcptnNmprCn = k.find("ocuAcptnNmprCn")
        trafcltyNm = k.find("trafcltyNm")

        lst.append(
            {
                "훈련기관_코드": instIno.text if instIno else None,
                "등록훈련기관": cstmrNm.text if cstmrNm else None,
                "시설면적(m*m)": fcltyArCn.text if fcltyArCn else None,
                "인원(명)": ocuAcptnNmprCn.text if ocuAcptnNmprCn else None,  # 수용인원
                "시설명": trafcltyNm.text if trafcltyNm else None,
            }
        )

    return lst
