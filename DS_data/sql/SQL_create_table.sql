create database if not exists DS;

use DS;

drop table if exists DS_info;

create table if not exists DS_info(
  id SMALLINT UNSIGNED PRIMARY KEY auto_increment not null,
  Subject_level_1 varchar(300) not null,
  Subject_level_2 varchar(300) not null,
  Subject_level_3 varchar(300) default (CONCAT(DATE_FORMAT(NOW(), "%Y-%m-%d %T.%f"),' ','for fill')),
  Source varchar(1000),
  Notes varchar(1000),
  date_when_added_into_table TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert into DS_info (Subject_level_1, Subject_level_2) VALUES ('asdasd','asdasd');
insert into DS_info (Subject_level_1, Subject_level_2) VALUES ('asdasd3','asdasd2');
insert into DS_info (Subject_level_1, Subject_level_2) VALUES ('asdasd','asdasd');
insert into DS_info (Subject_level_1, Subject_level_2) VALUES ('asd','asdasd');

select * from DS_info;
select distinct Subject_level_1 from DS_info;



drop table if exists DS_exam;

create table if not exists DS_exam(
  id SMALLINT UNSIGNED PRIMARY KEY auto_increment not null,
  Question varchar(300) not null,
  Answer varchar(300) not null,
  View_count smallint unsigned default 0,
  Right_answer_count smallint unsigned default 0,
  Rating smallint unsigned default 0,
  Note varchar(1000)
);

insert into DS_exam (Question, Answer) VALUES ('asdasd','asdasd');

select * from DS_exam;

