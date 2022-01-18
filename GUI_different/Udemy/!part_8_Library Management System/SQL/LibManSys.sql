create database if not exists LibManSys;

use LibManSys;

-- drop table if exists tbl_addbook;

create table if not exists tbl_addbook(
  id int unique auto_increment not null,
  title varchar(100) not null, 
  author varchar(100),
  publisher int,
  isAvailable bool default 1,
  primary key (id)
  );

insert into tbl_addbook (title, author, publisher)  VALUE ('Преступление и наказание', 'Достоевский', '111');
insert into tbl_addbook (title, author, publisher)  VALUE ('Братья Карамазовы', 'Достоевский', '111');

select * from tbl_addbook;
 

-- drop table if exists tbl_addmember;

create table if not exists tbl_addmember(
  id int unique auto_increment not null,
  name varchar(100) not null, 
  mobile varchar(100),
  email varchar(100),
  primary key (id)
  );

insert into tbl_addmember (name, mobile, email)  VALUE ('Андрей', '111111', '111@mail.ru');
insert into tbl_addmember (name, mobile, email)  VALUE ('Андрей', '111111', '111@mail.ru');

select * from tbl_addmember;
select * from tbl_addmember where name LIKE '%Андр%';


-- drop table if exists tbl_issue;

create table if not exists tbl_issue(
  book_id int unique,
  member_id int, 
  issue_time timestamp default current_timestamp,
  renew_count integer default 0,
  foreign key(book_id) references tbl_addbook(id),
  foreign key(member_id) references tbl_addmember(id)
);


select * from tbl_issue;

