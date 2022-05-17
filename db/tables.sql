create table training_info{
    id char(17) primary key,
    inst_id char(12) not null,
    nsc_code char(8) not null,
    category char(5) not null,
    train_target varchar(35),
    degree smallint not null, 
    start_dt date not null,
    end_dt date not null,
    tel varchar(11),
    supervisor varchar(35),
    title varchar(60) not null,
    subtitle varchar(60),
    quota smallint not null,
    contents text,
    course_fee int not null,
    real_fee int not null,
    registered_cnt smallint not null,
    
    address varchar(20) not null,

    info_type varchar(2) not null,
    
    ei_employment_cnt_3_months text,
    ei_employment_cnt_6_months text,
    ei_employment_ratio_3_months text,
    course_degree text,
    grade text,
    link_title text,
    link_subtitle text,
    icon_title text,
    icon_subtitle text,
    contents text,
    ei_employment_Cnt_3_months_le_10 text,
};

create table institution_info{
    name varchar(30),
    address varchar(20),
    address_detail varchar(30),
    
    id char(12),
    ncs_code char(8),
    ncs_name char(20),
    ncs char(1),
    non_ncs_lec_practical_time text,
    gov_grant smallint,
    eval_grad text,
    total_days smallint,
    total_time smallint,
    training_method_code text,
    charge_name varchar(15),
    charge_email varchar(60),
    charge_tel varchar(14),
    degree smallint,
    training_id char(17),
    training_title varchar(60),
    training_classify text,
    training_proc_classify text,
    training_proc_classify_name text,
    zip_code varchar(10),

    homepage text,
    file_path text,
    logo_file_name text,
    real_fee int,

};
create table institution_info_detail{
    training_category_name text,
    training_class text,
    training_days smallint,
    training_time smallint,
    fee smallint,
    degree smallint,
    training_id smallint,
    trainig_name varchar(60)
};

create table facility_info{
    inst_name varchar(60),
    name varchar(50)
    area smallint,
    hold_quantity smallint,
    capacity smallint,
};
create table equipment_info{
    inst_name varchar(60),
    name varchar(50),
    hold_quantity smallint,
};
--- 훈련일정?? 추가정보로 간주
create table training_additional_info{
    ei_employment_cnt_3_months smallint
    ei_employment_ratio_3_months float
    ei_employment_state_3_months varchar(1),
    
    ei_employment_cnt_6_months smallint
    ei_employment_ratio_6_months float
    ei_employment_state_6_months varchar(1),

    inst_id char(12),
    quota smallint,
    registered_cnt smallint,
    total_fee int,
    start_dt date,
    end_dt date,
    degree smallint
};

--- common codes ---


--- training ---
create table training_classification{
    code char(2),
    content text
};
create table training_method{
    code char(2),
    content text
};
create table training_category{
    code char(5),
    content text
}
--- region ---
create table training_region_main{
    code char(2) primary key,
    region varchar(4),
}
create table training_region_sub{
    code char(5) primary key,
    region varchar(20),
    constraints region_sub_fk foreign key 
}
--- KECO ---
create table KECO_main{
    code char(2),
    content text,
}
create table KECO_middle{
    code char(3),
    content text,
}
create table KECO_sub{
    code char(4),
    content text,
}
--- NCS --- 
create table NCS_main{
    code varchar(2),
    content text,
}
create table NCS_middle{
    code varchar(4),
    content text,
}
create table NCS_sub{
    code varchar(6),
    content text,
}
create table NCS_subdiv{
    code varchar(8),
    content text,
}