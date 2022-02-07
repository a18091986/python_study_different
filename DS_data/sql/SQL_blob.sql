create database if not exists image;

use image;

drop table if exists imag;

create table if not exists imag(

  id tinyint unsigned auto_increment,
  name varchar(100) not null,
  img longblob not null,
  primary key(id));

select * from imag;

паопароn
insert into imag (name, img) values ('123', '123das');