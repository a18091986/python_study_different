# import mysql.connector as mc
#
# def connect_to_db():
#     try:
#         mydb = mc.connect(
#         host = '192.168.2.165',
#         port = '3306',
#         user = 'admin',
#         password = '0gfyfctyr0MYSQL',
#         database = 'image')
#         print('Connected')
#         connection = True
#     except mc.Error as e:
#         mydb = None
#         connection = e
#         print(e)
#
#     return (mydb, connection)
#
# def convertToBinaryData(filename):
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#
#     return binaryData
#
# def insertBLOB(name, photo):
#     print('Inserting BLOB into table')
#     name = name
#     photo = convertToBinaryData(photo)
#     # print(photo)
#     try:
#         mydb, connection = connect_to_db()
#         cursor = mydb.cursor()
#         # sql_insert_blob_query = f"""insert into imag (name, img) values ({name}, {photo})"""
#         sql_insert_blob_query ="""insert into imag (name, img) values (%s,%s)"""
#         # print(sql_insert_blob_query, (name, photo))
#         result = cursor.execute(sql_insert_blob_query, (name, photo))
#         mydb.commit()
#         print('image inserted successfully')
#     except Exception as e:
#         print(e)
#
#     finally:
#         if connection == True:
#             cursor.close()
#             mydb.close()
#             print('Connection closed')
#
# def write_file(data, filename):
#     # Convert binary data to proper format and write it on Hard Disk
#     with open(filename, 'wb') as file:
#         file.write(data)
#     print('УСЕ')
#
# def readBLOB(id, photo):
#     print("Reading BLOB data from python_employee table")
#
#     try:
#         mydb, connection = connect_to_db()
#         cursor = mydb.cursor()
#         sql_fetch_blob_query = """SELECT * from imag where id = %s"""
#         cursor.execute(sql_fetch_blob_query, (id,))
#         record = cursor.fetchall()
#         for row in record:
#             print("Id = ", row[0], )
#             print("Name = ", row[1])
#             image = row[2]
#             print("Storing image on disk \n")
#             write_file(image, photo)
#
#     except Exception as error:
#         print(error)
#
#     finally:
#         if mydb.is_connected():
#             cursor.close()
#             mydb.close()
#             print("MySQL connection is closed")
#
#
# insertBLOB('1_картинка', "NOT_FOR_GIT/2.jpg")
# insertBLOB('2_картинка', "NOT_FOR_GIT/1.jpg")
#
#
# readBLOB(5, r"C:\Users\admin\Desktop\PYTHON_2022\python_study_different\DS_data\NOT_FOR_GIT\eric_photo.jpg")
#


import pandas as pd

df = pd.read_excel(r'C:\Users\admin\Desktop\PYTHON_2022\python_study_different\DS_data\NOT_FOR_GIT\backup\subject_level_1\backup_Subject_level_1_db_17_02_2022_02_56_29.xlsx', header = None)
df.set_axis([2,3], axis='columns', inplace=True)
print(df)
