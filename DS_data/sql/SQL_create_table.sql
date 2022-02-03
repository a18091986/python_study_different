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

update Subject_level_2 set Subject_level_2 = 'Алгоритмы классификации (кластеризации)' where Subject_level_2 = 'Алгоритмы классификации';  
update Subject_level_2 set Subject_level_2 = 'Обучающий курс' where Subject_level_2 = 'обучающий курс';  
update Subject_level_2 set Subject_level_2 = 'Manifold Learning (понижение размерности)' where Subject_level_2 = 'Понижение размерности (пространство признаков)';  

insert into Subject_level_2 (Subject_level_2, Subject_level_1_id) VALUES ('asdfdsf', 1);



select * from Subject_level_2;

select id from Subject_level_2 where Subject_level_2 = 'Manifold Learning';

select Subject_level_2 from Subject_level_2 where subject_level_1_id = (select id from subject_level_1 where subject_level_1 = "11111111")


drop table if exists DS_info;

create table if not exists DS_info(
  id SMALLINT UNSIGNED PRIMARY KEY auto_increment not null,
  Subject_level_1_id smallint unsigned not null,
  Subject_level_2_id smallint unsigned not null,
  Subject_level_3 varchar(300) not null unique default (CONCAT(DATE_FORMAT(NOW(), "%Y-%m-%d %T.%f"),' ','for fill')),
  Source varchar(1000),
  Notes varchar(3000),
  date_when_added_into_table TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  for_question bool default 0,
  FOREIGN KEY (Subject_level_1_id) REFERENCES Subject_level_1 (id),
  FOREIGN KEY (Subject_level_2_id) REFERENCES Subject_level_2 (id)
);

ALTER TABLE DS_info ADD COLUMN RATING TINYINT UNSIGNED NOT NULL;
ALTER TABLE DS_info ADD COLUMN VIEWED bool NOT NULL default 0;
ALTER TABLE DS_info MODIFY Notes varchar(3000);

INSERT INTO DS_info (id,Subject_level_1_id,Subject_level_2_id,Subject_level_3,Source,Notes,date_when_added_into_table,for_question,RATING,VIEWED) VALUES (59,64,5,13,'линейное преобразование линейных пространств. матрица линейного преобразования','https://colab.research.google.com/drive/1-f34MB1y6Ytuom1Ja6Wlz7hIetpf7wzs#scrollTo=Kyx05c8oklTH&line=4&uniqifier=1','nan','2022-02-01 18:04:18',0)

insert into DS_info (Subject_level_1_id, Subject_level_2_id, Subject_level_3) VALUES (1,1, 'sdfsdf');

DELETE from DS_info where id = 6


select * from DS_info;

select * from DS_info where Subject_level_2_id = 15;

update DS_info set Subject_level_2_id = (select id from Subject_level_2 where Subject_level_2 = 'Manifold Learning')
select * from DS_info where Subject_level_2_id = (select id from Subject_level_2 where Subject_level_2 = 'Понижение размерности (пространство признаков)');
select * from DS_info where Subject_level_2_id = 15;
select * from Subject_level_2 where Subject_level_2 = 'Manifold Learning';
select * from Subject_level_1 where id = 6;
select * from Subject_level_2 where id = 14;

select id from Subject_level_2 where Subject_level_2 = 'Понижение размерности (пространство признаков)'

INSERT INTO DS_info (Subject_level_1_id,Subject_level_2_id,Subject_level_3,Source,Notes,date_when_added_into_table,for_question,RATING,VIEWED) VALUES (67,5,13,
'Что такое усеченное SVD разложение ранга r матрицы $M^{m,х,n} in mathbb R$',
'https://colab.research.google.com/drive/1-f34MB1y6Ytuom1Ja6Wlz7hIetpf7wzs#scrollTo=jhi75pRFLByN&line=1&uniqifier=1',
'SVD разложение, где оставили только самые большие сингулярные значения вместе с соответствующими сингулярными векторами',
'2022-02-01 20:05:21','1', '1', '0')

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



update Subject_level_2 set Subject_level_2='Manifold Learning (понижение размерности)' where Subject_level_2='Пространство признаков' or Subject_level_2='Manifold Learning';

update Subject_level_2 set Subject_level_2='Курсы' where Subject_level_2='обучающий курс';

update Subject_level_2 set Subject_level_2='Приложения/Сервисы' where Subject_level_2='Приложения';

update DS_info set Subject_level_2_id=14 where Subject_level_2_id=15;
delete from Subject_level_2 where Subject_level_2='Manifold Learning';

select Subject_level_1.Subject_level_1, Subject_level_2.Subject_level_2, DS_info.* FROM DS_info 
  left join Subject_level_1 on DS_info.Subject_level_1_id = Subject_level_1.id
  left join Subject_level_2 on DS_info.Subject_level_2_id = Subject_level_2.id;