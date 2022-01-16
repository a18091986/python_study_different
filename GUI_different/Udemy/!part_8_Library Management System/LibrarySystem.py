from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from mainGUI import Ui_MainWindow
from addbook import Add_Dialog
from addmember import Member_Dialog
from bookview import View_Dialog
from membersview import MembersView_Dialog
from dbconnect import connect_to_db
from random import choice



class LibrarySystem (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_addBook.clicked.connect(self.add_book)
        self.toolButton_addmember.clicked.connect(self.add_member)
        self.toolButton_viewbook.clicked.connect(self.view_books)
        self.toolButton_viewmember.clicked.connect(self.view_members)
        self.lineEdit_bookid.returnPressed.connect(self.book_id)
        self.lineEdit_memberid.returnPressed.connect(self.member_id)
        self.toolButton_issue.clicked.connect(self.issue_book)
        self.lineEdit_submission.returnPressed.connect(self.load_issue)
        self.toolButton_submitbook.clicked.connect(self.submit_book)
        self.toolButton_renew.clicked.connect(self.renew_book)

    def add_book(self):
        dialog = QDialog()
        ui = Add_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def add_member(self):
        dialog = QDialog()
        ui = Member_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_books(self):
        dialog = QDialog()
        ui = View_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_members(self):
        dialog = QDialog()
        ui = MembersView_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def book_id(self):
        id = self.lineEdit_bookid.text()
        mydb, connection = connect_to_db()
        if connection == True:
            print('Connection is Established')
            try:
                mycursor = mydb.cursor()
                mycursor.execute(f'select * from tbl_addbook where title like "%{id}%" or author like "%{id}%"')
                result = mycursor.fetchall()
                if result:
                    row = choice(result)
                    self.label_bookname.setText(f'Book Title: {row[1]}')
                    self.label_bookauthor.setText(f'Book Author: {row[2]}')
                    return row[0]
                else:
                    self.label_bookname.setText(f'Информация не найдена')
                    self.label_bookauthor.setText(f'Информация не найдена')
            except Exception as e:
                e = str(e)
                print(e)

        else:
            print(str(connection))

    def member_id(self):
        id = self.lineEdit_memberid.text()
        mydb, connection = connect_to_db()
        if connection == True:
            print('Connection is Established')
            try:
                mycursor = mydb.cursor()
                mycursor.execute(f'select * from tbl_addmember where name like "%{id}%"')
                result = mycursor.fetchall()
                if result:
                    row = choice(result)
                    self.label_membername.setText(f'Member Name: {row[1]}')
                    self.label_contactinfo.setText(f'Member phone: {row[2]}')
                    return row[0]
                else:
                    self.label_membername.setText(f'Информация не найдена')
                    self.label_contactinfo.setText(f'Информация не найдена')
            except Exception as e:
                e = str(e)
                print(e)

        else:
            print(str(connection))

    def issue_book(self):
        book_id = self.book_id()
        member_id = self.member_id()
        print(book_id, member_id)
        mydb, connection = connect_to_db()

        if connection == True:

            print('Connection is Established')

            if book_id == None or member_id == None:
                print('Не найден пользователь или книга')
                QMessageBox.about(self, 'Issue Book', 'Не найден пользователь или книга')
            else:
                try:
                    mycursor = mydb.cursor()
                    query1 = f'insert into tbl_issue (book_id, member_id)  VALUE (%s, %s)'
                    query2 = f'update tbl_addbook set isAvailable = 0 where id = {book_id}'
                    value = (book_id, member_id)
                    mycursor.execute(query1, value)
                    mycursor.execute(query2)
                    mydb.commit()
                    QMessageBox.about(self, 'Issue Book', 'Book Issued Successfully')
                except Exception as e:
                    print(e)
        else:
            print(str(connection))

    def load_issue(self):
        issue_id = self.lineEdit_submission.text()
        mydb, connection = connect_to_db()
        if connection == True:
            print('Connection is Established')
            try:
                mycursor = mydb.cursor()
                mycursor.execute(f'select * from tbl_issue where book_id like "{issue_id}"')
                result = mycursor.fetchall()
                if result:
                    self.tableWidget_bookinfo.setRowCount(0)
                    for row_number, row_data in enumerate(result):
                        self.tableWidget_bookinfo.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.tableWidget_bookinfo.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                else:
                    self.tableWidget_bookinfo.setRowCount(0)
                    QMessageBox.about(self, 'book submission', 'Книга не на руках')
                    print(f'Информация не найдена')
            except Exception as e:
                e = str(e)
                print(e)
        else:
            print(str(connection))

    def submit_book(self):
        issue_id = self.lineEdit_submission.text()
        mydb, connection = connect_to_db()
        if connection == True:
            print('Connection is Established')
            try:
                if issue_id == '':
                    print('Please choose a book')
                    QMessageBox.about(self, 'Book Submission', 'Please choose a book')
                else:
                    mycursor = mydb.cursor()
                    mycursor.execute(f'delete from tbl_issue where book_id like "{issue_id}"')
                    mycursor.execute(f'update tbl_addbook set isAvailable = 1 where id = "{issue_id}"')
                    self.tableWidget_bookinfo.setRowCount(0)
                    mydb.commit()
                    QMessageBox.about(self, 'book submission', 'book submitted')
            except Exception as e:
                e = str(e)
                print(e)
        else:
            print(str(connection))

    def renew_book(self):
        issue_id = self.lineEdit_submission.text()
        mydb, connection = connect_to_db()
        if connection == True:
            print('Connection is Established')
            try:
                if issue_id == '':
                    print('Please choose a book')
                    QMessageBox.about(self, 'Book Submission', 'Please choose a book')
                else:
                    mycursor = mydb.cursor()
                    mycursor.execute(f'update tbl_issue set issue_time = current_timestamp, renew_count = renew_count + 1 where book_id = "{issue_id}"')
                    mydb.commit()
                    QMessageBox.about(self, 'book renew', 'book renewed successfully')
            except Exception as e:
                e = str(e)
                print(e)
        else:
            print(str(connection))

