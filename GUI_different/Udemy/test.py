# from sqlalchemy import create_engine
# import pymysql
# import pandas as pd
#
# sqlEngine = create_engine('mysql+pymysql://admin:0gfyfctyr0MYSQL@192.168.2.165/music', pool_recycle=3600)
# dbConnection = sqlEngine.connect()
# print('!!!')
# dbConnection.close()


import mysql.connector as mc

mydb = mc.connect(

                host = '192.168.2.165',
                user = 'admin',
                password = '0gfyfctyr0MYSQL'

            )
print('connection established')
cursor = mydb.cursor()
cursor.execute(f'use unicredit')
cursor.execute(f'select * from clients')
print(cursor.fetchall())
