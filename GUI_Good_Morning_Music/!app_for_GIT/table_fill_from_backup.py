import pandas as pd
import datetime
from datetime import date, datetime
from not_for_github.db_connect import connect_to_db

df = pd.read_excel('SQL/backup_music_db_20_01_2022_19_10_22.xlsx') #когда записвыаю из бэкапа
# df = pd.read_excel('SQL/music_fin.xlsx') #когда записываю из music_fin

def add_row_in_db_from_df(row):
    """
    для добавления старой музыки из excell в папке SQL
    """
    # print(row[1])
    # date_of = date(datetime.strptime(row[1], "%d.%m.%Y"))
    # date_of = datetime.strptime(row[1], '%d.%m.%Y').date()
    # print(date_of)
    try:
        date_of = datetime.date(row[6]) #когда записываю с бэкапа
        #date_of = datetime.strptime(row[1], '%d.%m.%Y').date() #когда записываю из music_fin
    except TypeError:
        date_of = date(2001, 1, 1)
    link = row[2]
    genre = row[3]
    author = row[4]
    description = row[5]
    was = 1 if (row[7] == 'было' or row[7] == 1) else 0 #когда записываю с бэкапа
    # was = 1 if (row[6] == 'было' or row[6] == 1) else 0 #когда записываю из music_fin


    mydb, connection = connect_to_db()

    if connection == True:

        # print('Connection is Established')

        if author == '' or link == '' or description == '' or was == '':
            print('заполнены не все поля')
            # self.label_result.setText('Please add all fields')
            # self.label_result.setStyleSheet('color:red')

        else:
            try:
                mycursor = mydb.cursor()
                query = f"INSERT INTO music(link, genre, channel_author, description, date_when_send_into_group, whether_sent) VALUES (%s, %s, %s, %s, %s, %s)"
                value = (link, genre, author, description, date_of, was)
                mycursor.execute(query, value)
                mydb.commit()
                print('Информация успешно записана')
                # self.label_result.setText('Information added successfully')
                # self.label_result.setStyleSheet('color:green')
                # self.lineEdit_question_into_db.setText('')
            except Exception as e:
                # e = string_split(str(e))
                print(e)
                # self.label_result.setText('Can\'t add information to DB' + '\n' + e)
                # self.label_result.setStyleSheet('color:red')

    else:
        print(connection)
        # self.label_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
        # self.label_result.setStyleSheet('color:red')

for row in df.itertuples():
    add_row_in_db_from_df(row)