
--- common codes ---


--- training ---
create table inst_classification( -- 훈련기관 구분 
    code char(2) primary key,
    content text
);
create table training_method( -- 훈련방법
    code char(2) primary key,
    content text
);
create table training_category( -- 훈련종류
    code char(5) primary key,
    content text
);

--- region ---
create table training_region_main( -- 훈련지역 대분류
    code char(2) primary key,
    region varchar(4)
);
create table training_region_sub( -- 훈련지역 중분류
    code char(5) primary key,
    region varchar(18),
    region_main_code char(2),

    constraint region_sub_fk foreign key(region_main_code) references training_region_main(code) on delete cascade 
);

--- KECO ---
create table KECO_main( -- KECO 대분류
    code char(2) primary key,
    content text
);
create table KECO_middle( -- KECO 중분류
    code char(3) primary key,
    code_main char(2),
    content text,

    constraint fk_keco_middle foreign key(code_main) references KECO_main(code) on delete cascade
);
create table KECO_sub( -- KECO 소분류
    code char(4) primary key,
    code_middle char(3),
    content text,

    constraint fk_keco_sub foreign key(code_middle) references KECO_middle(code) on delete cascade
);

--- NCS --- 
create table NCS_main( -- NCS 대분류
    code char(2) primary key,
    content text
);
create table NCS_middle( -- NCS 중분류
    code char(4) primary key,
    code_main char(2),
    content text,

    constraint fk_ncs_middle foreign key(code_main) references NCS_main(code) on delete cascade
);
create table NCS_sub( -- NCS 소분류
    code char(6) primary key,
    code_middle char(4),
    content text,

    constraint fk_ncs_sub foreign key(code_middle) references NCS_middle(code) on delete cascade
);
create table NCS_subdiv( -- NCS 세분류
    code char(8) primary key,
    code_sub char(6),
    content text,

    constraint fk_ncs_subdiv foreign key(code_sub) references NCS_sub(code) on delete cascade
);


create table institution_info(
    id char(12) primary key, -- 훈련기관 ID

    name varchar(30), -- 훈련기관명
    address varchar(20), -- 주소지
    address_detail varchar(30), -- 상세주소

    zip_code varchar(10), -- 우편번호
    homepage text -- 홈페이지 주소

);


create table training(
    id char(17) primary key, -- 훈련과정 id
    inst_id char(12) not null, -- 훈련기관 코드
    
    degree smallint not null, -- 훈련과정 회차
    
    title varchar(60) not null, -- 제목
    subtitle varchar(60), -- 부제목
    contents text, -- 컨텐츠

    constraint fk_training_inst_id foreign key(inst_id) references institution_info(id)
);


create table institution_detail(
    inst_id char(12) primary key,
    training_id char(17), -- 훈련과정 ID

    training_title varchar(60), -- 훈련과정명
    training_classify text, -- 훈련과정 구분 (훈련종류와 동일)
    training_proc_classify text, -- 주요 훈련과정 구분 
    training_proc_classify_name text, -- 주요 훈련과정 구분명
    training_method_code text, -- 훈련방법코드

    degree smallint, -- 훈련과정 회차
    
    ncs smallint, -- NCS 여부 (Y/N - 1/0)
    ncs_code char(8), -- NCS 코드
    ncs_name char(20), -- NCS 명

    non_ncs_lec_practical_time text, -- 비 NCS교과 실기시간
    non_ncs_lec_theory_time text, -- 비 NCS교과 이론시간	

    gov_grant smallint, -- 정부지원금
    eval_grad text, -- 평가등급

    inst_total_days smallint, -- 기관 총 훈련일수
    inst_total_time smallint, -- 기관 총 훈련시간
    
    file_path text, -- 파일경로
    logo_file_name text, -- 로고파일명
    real_fee int, -- 실제 훈련비


    constraint fk_institution_detail_inst_id foreign key(inst_id) references institution_info(id),
    constraint fk_institution_detail_training_id foreign key(training_id) references training(id),
    constraint fk_institution_detail_training_classify foreign key(training_classify) references training_category(code),
    constraint fk_institution_detail_training_method foreign key(training_method_code) references training_method(code),
    constraint fk_institution_detail_ncs_code foreign key(ncs_code) references NCS_subdiv(code)
);

create table training_detail(
    id UUID primary key,
    training_id char(17),

    ncs_code char(8) not null, -- ncs 코드

    category char(5) not null, -- 훈련구분
    train_target varchar(35), -- 훈련대상
    
    start_dt date not null, -- 시작일
    end_dt date not null, -- 종료일
    
    tel varchar(11), -- 연락처
    
    supervisor varchar(35), -- 주관부처
    
    link_title text, -- 제목 링크
    link_subtitle text, -- 부 제목 링크
    icon_title text, -- 제목 아이콘
    icon_category_title text, -- 제목 아이콘 구분

    quota smallint not null, -- 정원
    course_fee int not null, -- 훈련비
    real_fee int not null, -- 실제 훈련비
    registered_cnt smallint not null, -- 신청인원
    
    address varchar(20) not null, -- 주소
    grade text, -- 등급

    constraint fk_training_detail_training_id foreign key(training_id) references training(id),
    constraint fk_training_detail_training_category foreign key(category) references training_category(code),
    constraint fk_training_detail_ncs_code foreign key(ncs_code) references NCS_subdiv(code)
    
);

--- 훈련일정?? 추가정보로 간주
create table training_additional_info(
    id UUID primary key,
    training_id char(17),
    inst_id char(12), -- 훈련기관 코드
    
    degree smallint, -- 훈련과정 회차
    
    quota smallint, -- 수강정원
    registered_cnt smallint, -- 수강인원
    
    total_fee int, -- 총 훈련비

    start_dt date, -- 시작일
    end_dt date, -- 종료일

    ei_emp_ins_cnt_3_months smallint, -- 	3개월 고용보험 취업인원
    ei_emp_ins_ratio_3_months float, -- 3개월 고용보험 취업률(%)
    ei_emp_ins_state_3_months varchar(1), -- 3개월 훈련정보 상세(A-개설예정, B-진행중, C-미실시, D-수료자없음)
    
    ei_emp_ins_cnt_6_months smallint, -- 6개월 고용보험 취업인원
    ei_emp_ins_ratio_6_months float, -- 6개월 고용보험 취업률(%)
    ei_emp_ins_state_6_months varchar(1), -- 6개월 훈련정보 상세(A-개설예정, B-진행중, C-미실시, D-수료자없음)

    ei_emp_ins_non_registered_6_months_cnt smallint, -- 6개월 고용보험 미가입 취업인원

    ei_employment_Cnt_3_months_le_10 smallint, -- 고용보험3개월 취업누적인원 10인이하 여부(Y/N - 1/0)

    constraint fk_training_additional_info_training_id foreign key(training_id) references training(id),
    constraint fk_training_additional_info_inst_id foreign key(inst_id) references institution_info(id)
);

create table charge(
    id UUID primary key,

    training_id char(17) not null,
    inst_id char(12) not null,
    degree smallint not null,
    
    charge_name varchar(15), -- 담당자 이름
    charge_email varchar(60), -- 담당자 이메일
    charge_tel varchar(14), -- 담당자 전화번호

    constraint fk_charge_training_id foreign key(training_id) references institution_info(id),
    constraint fk_charge_inst_id foreign key(inst_id) references institution_info(id)
);


-- create table inst_training_info(
--     id uuid primary key,
--     inst_id char(12),

--     training_code smallint, -- 훈련과정 코드
--     trainig_name varchar(60) -- 훈련과정명

--     training_category_name text, -- 훈련 분야명
    
--     training_class text, -- 훈련 종류

--     training_days smallint, -- 총 훈련일수
--     training_time smallint, -- 총 훈련시간
    
--     fee smallint, -- 수강료
    
--     degree smallint, -- 훈련과정 회차
    
--     constraint fk_inst_training_info_inst_id foreign key(inst_id) references institution_info(id)
-- );

create table facility_info(
    id UUID primary key,

    inst_id char(12),
    training_id char(17),

    degree smallint,

    inst_name varchar(60), -- 등록 훈련기관 명
    name varchar(50), -- 시설명
    area smallint, -- 면적
    hold_quantity smallint, -- 시설 수
    capacity smallint, -- 수용인원

    constraint fk_facility_info_training_id foreign key(training_id) references training(id),
    constraint fk_facility_info_inst_id foreign key(inst_id) references institution_info(id)
);

create table equipment_info(
    id UUID primary key,

    inst_id char(12),
    training_id char(17),

    degree smallint,

    inst_name varchar(60), -- 등록 훈련기관 명
    name varchar(50), -- 장비명
    hold_quantity smallint, -- 장비 수
    
    constraint fk_equipment_info_training_id foreign key(training_id) references training(id),
    constraint fk_equipment_info_inst_id foreign key(inst_id) references institution_info(id)
);


