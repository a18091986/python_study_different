create database if not exists music;

use music;

-- INSERT INTO music.music(`index`, ссылка, жанр, `автор канала`, `описание видео`, дата, `было ли`) VALUES

drop table if exists music;

create table if not exists music(
  id SMALLINT UNSIGNED auto_increment not null,
  link varchar(300) unique,
  genre varchar(100),
  channel_author varchar(100),
  description varchar(300),
  date_when_send_into_group date,
  whether_sent boolean,
  date_when_added_into_table TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  primary key (id)
  );

INSERT INTO music(id, link, genre, channel_author, description, date_when_send_into_group, whether_sent) VALUES (0, 'https://youtu.be/ujudeWdbJsc', 'акробатика', 'Paper Doll Militia', 'Rain Anya Aerial Silks 2017', 20200727, 1);

select * from music where whether_sent = 0;
select * from music where channel_author = 'NILETTO';

select * from music;

select * FROM music where channel_author = 'Alexandr Misko' and id = 17;

update music set id = 1000 where id = 17;

update music set id = 999 where id = 1000 and genre = 'гитара';

select * from music where id = 5555;


update music set genre = 'музыка', channel_author = 'Опанасенко' where channel_author = 'accordionman';

select * from music where channel_author = 'опанасенко'

select * from music where channel_author = 'Accordionman'

select * from music where channel_author = 'ХРЕНЬ';


select * from music where id = 15;

select * from music where genre = 'НЕРВЫ';

select * from music where link = 'https://youtu.be/T0XoA4qIt_M';

DELETE from music where link = 'https://youtu.be/T0XoA4qIt_M'

select * from music where whether_sent = 0;

-- delete from music;

select * from music;
select * from music where whether_sent = 0;
select * from music where date_when_send_into_group = DATE('2001-01-01');

-- alter table music auto_increment = 1;

-- select NOW();-- 20.01.2022 18:43:30

select DATE('2001-12-01')

-- https://youtu.be/xSgT4ZtT5M0
