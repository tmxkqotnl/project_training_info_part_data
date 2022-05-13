def parse_xml_agency_info_default(xml: BeautifulSoup):
    instIno = xml.find('instIno')
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
            ## 기본
            "주소지": xml.find("addr1").text if addr1 else None,
            "상세주소": xml.find("addr2").text if addr2 else None,
            "파일경로": xml.find("filePath").text if filePath else None,
            "홈페이지_주소": xml.find("hpAddr").text if hpAddr else None,
            "훈련기관명": xml.find("inoNm").text if inoNm else None,
            "훈련기관_코드": xml.find("instIno").text if instIno else None,
            "실제_훈련비": xml.find("instPerTrco").text if instPerTrco else None,
            "NCS코드": xml.find("ncsCd").text if ncsCd else None,
            "NCS명": xml.find("ncsNm").text if ncsNm else None,
            "NCS여부": xml.find("ncsYn").text if ncsYn else None,
            "비NCS교과_실기시간": xml.find("nonNcsCoursePrcttqTime").text
            if nonNcsCoursePrcttqTime
            else None,
            "비NCS교과_이론시간": xml.find("nonNcsCourseTheoryTime").text
            if nonNcsCourseTheoryTime
            else None,
            "로고파일명": xml.find("pFileName").text if pFileName else None,
            "정부지원금": xml.find("perTrco").text if perTrco else None,
            "평가등급": xml.find("torgParGrad").text if torgParGrad else None,
            "훈련방법코드": xml.find("traingMthCd").text if traingMthCd else None,
            "담당자명": xml.find("trprChap").text if trprChap else None,
            "담당자_이메일": xml.find("trprChapEmail").text if trprChapEmail else None,
            "담당자_전화번호": xml.find("trprChapTel").text if trprChapTel else None,
            "훈련과정회차": xml.find("trprDegr").text if trprDegr else None,
            "훈련과정구분": xml.find("trprGbn").text if trprGbn else None,
            "훈련과정ID": xml.find("trprId").text if trprId else None,
            "훈련과정명": xml.find("trprNm").text if trprNm else None,
            "주요_훈련과정_구분": xml.find("trprTarget").text if trprTarget else None,
            "주요_훈련과정_구분명": xml.find("trprTargetNm").text if trprTargetNm else None,
            "총_훈련시간": xml.find("trtm").text if trtm else None,
            "총_훈련일수": xml.find("trDcnt").text if trDcnt else None,
            "우편번호": xml.find("zipCd").text if zipCd else None,
            ## 상세
            "훈련분야명": xml.find("govBusiNm").text if govBusiNm else None,
            "훈련종류": xml.find("torgGbnCd").text if torgGbnCd else None,
            "훈련일수": xml.find("totTraingDyct").text if totTraingDyct else None,
            "훈련시간": xml.find("totTraingTime").text if totTraingTime else None,
            "수강료": xml.find("totalCrsAt").text if totalCrsAt else None,
            "훈련과정회차": xml.find("trprDegr").text if trprDegr else None,
            "훈련과정코드": xml.find("trprId").text if trprId else None,
            "훈련과정명": xml.find("trprNm").text if trprNm else None,
            }
def parse_xml_agency_info_facility_detail(xml:BeautifulSoup):
    lst = []
    
    instIno = xml.find('instIno')
    for k in xml.findAll("inst_facility_info_list"):
        cstmrNm = k.find("cstmrNm")
        fcltyArCn = k.find("fcltyArCn")
        ocuAcptnNmprCn = k.find("ocuAcptnNmprCn")
        trafcltyNm = k.find("trafcltyNm")
    
        lst.append({
            "훈련기관_코드": xml.find("instIno").text if instIno else None,
            "등록훈련기관": k.find("cstmrNm").text if cstmrNm else None,
            "시설면적(m*m)": k.find("fcltyArCn").text if fcltyArCn else None,
            "인원(명)": k.find("ocuAcptnNmprCn").text if ocuAcptnNmprCn else None,  # 수용인원
            "시설명": k.find("trafcltyNm").text if trafcltyNm else None
        })
        
    return lst

def parse_xml_agency_info_facility_detail(xml:BeautifulSoup):
    lst = []
    
    instIno = xml.find('instIno')
    for k in xml.findAll("inst_facility_info_list"):
        cstmrNm = k.find("cstmrNm")
        fcltyArCn = k.find("fcltyArCn")
        ocuAcptnNmprCn = k.find("ocuAcptnNmprCn")
        trafcltyNm = k.find("trafcltyNm")
    
        lst.append({
            "훈련기관_코드": xml.find("instIno").text if instIno else None,
            "등록훈련기관": k.find("cstmrNm").text if cstmrNm else None,
            "시설면적(m*m)": k.find("fcltyArCn").text if fcltyArCn else None,
            "인원(명)": k.find("ocuAcptnNmprCn").text if ocuAcptnNmprCn else None,  # 수용인원
            "시설명": k.find("trafcltyNm").text if trafcltyNm else None
        })
        
    return lst