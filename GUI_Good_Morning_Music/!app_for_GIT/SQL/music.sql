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
  primary key (id)
  );

INSERT INTO music(id, link, genre, channel_author, description, date_when_send_into_group, whether_sent) VALUES (0, 'https://youtu.be/ujudeWdbJsc', 'акробатика', 'Paper Doll Militia', 'Rain Anya Aerial Silks 2017', 20200727, 1);

select * from music where whether_sent = 0;