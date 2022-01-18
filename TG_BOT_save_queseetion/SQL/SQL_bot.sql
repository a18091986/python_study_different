create database if not exists QBot;

use QBot;

drop table if exists Question;

create table if not exists Question(
  id int auto_increment not null,
  question varchar(10000),
  links varchar(200),
  description varchar(1000),
  primary key (id)
  );

-- insert into Question (question) VALUE ('dfgdf');

select * from Question;