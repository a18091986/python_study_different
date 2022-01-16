create database if not exists LibManSys;

use LibManSys;

-- drop table if exists tbl_addbook;

create table if not exists tbl_addbook(
  id int auto_increment not null,
  title varchar(100) not null, 
  author varchar(100),
  publisher int,
  isAvailable bool default 1,
  primary key (id)
  );

insert into tbl_addbook (title, author, publisher)  VALUE ('Преступление и наказание', 'Достоевский', '111');

select * from tbl_addbook;

create table if not exists tbl_addmember(
  id int auto_increment not null,
  name varchar(100) not null, 
  mobile varchar(100),
  email int,
  primary key (id)
  );

insert into tbl_addmember (name, mobile, email)  VALUE ('Андрей', '111111', '111@mail.ru');