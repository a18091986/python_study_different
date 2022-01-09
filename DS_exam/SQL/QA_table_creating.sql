create database DS_exam;

use DS_exam;

drop table if exists QA;

create table if not exists QA(
  id int auto_increment not null,
  question varchar(1000),
  answer varchar(100),
  answer_wait bool,
  link varchar(500),
  question_category varchar(500),
  question_rate int,
  note varchar(500),
  primary key (id)
  );

insert into QA (question, answer) values ('На каком языке ты учишься програмировать?', 'Python'), ('Как называется система контроля версий ПО', 'git'), ('Какую СУБД ты изучаешь', 'mysql');

select * from QA;