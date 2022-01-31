create database if not exists DS;

use DS;

drop table if exists Subject_level_1;

create table if not exists Subject_level_1(
  id SMALLINT UNSIGNED PRIMARY KEY auto_increment not null,
  Subject_level_1 varchar(300) unique not null 
);

insert into Subject_level_1 (Subject_level_1) VALUES ('asd');
insert into Subject_level_1 (Subject_level_1) VALUES ('adsdsd');
insert into Subject_level_1 (Subject_level_1) VALUES ('ffffffff');


select distinct Subject_level_1 from Subject_level_1;
select * from Subject_level_1;

drop table if exists Subject_level_2;

create table if not exists Subject_level_2(
  id SMALLINT UNSIGNED PRIMARY KEY auto_increment not null,
  Subject_level_1_id smallint unsigned not null,
  Subject_level_2 varchar(300) unique not null,
  FOREIGN KEY (Subject_level_1_id) REFERENCES Subject_level_1 (id)
);

insert into Subject_level_2 (Subject_level_2, Subject_level_1_id) VALUES ('asdfdsf', 1);

select * from Subject_level_2;

select Subject_level_2 from Subject_level_2;

select Subject_level_2 from Subject_level_2 where subject_level_1_id = (select id from subject_level_1 where subject_level_1 = "11111111")


drop table if exists DS_info;

create table if not exists DS_info(
  id SMALLINT UNSIGNED PRIMARY KEY auto_increment not null,
  Subject_level_1_id smallint unsigned not null,
  Subject_level_2_id smallint unsigned not null,
  Subject_level_3 varchar(300) not null unique default (CONCAT(DATE_FORMAT(NOW(), "%Y-%m-%d %T.%f"),' ','for fill')),
  Source varchar(1000),
  Notes varchar(1000),
  date_when_added_into_table TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  for_question bool default 0,
  FOREIGN KEY (Subject_level_1_id) REFERENCES Subject_level_1 (id),
  FOREIGN KEY (Subject_level_2_id) REFERENCES Subject_level_2 (id)
);

ALTER TABLE DS_info ADD COLUMN RATING TINYINT UNSIGNED NOT NULL;
ALTER TABLE DS_info ADD COLUMN VIEWED bool NOT NULL default 0;

insert into DS_info (Subject_level_1_id, Subject_level_2_id, Subject_level_3) VALUES (1,1, 'sdfsdf');

DELETE from DS_info where id = 6


select * from DS_info;


select * from DS_info where for_question = 1;



-- drop table if exists QA;

create table if not exists QA(
  id SMALLINT UNSIGNED PRIMARY KEY auto_increment not null,
  Question varchar(300) not null,
  Answer varchar(300) not null,
  View_count smallint unsigned default 0,
  Right_answer_count smallint unsigned default 0,
  Rating smallint unsigned default 0,
  Note varchar(1000)
);

-- insert into QA (Question, Answer) VALUES ('asdasd','asdasd');

select * from QA;


SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'DS_info' AND table_schema = 'DS';



