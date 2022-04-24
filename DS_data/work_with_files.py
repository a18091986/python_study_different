from main_window_new import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import os
import subprocess
import winshell
import nbformat
import nbconvert
from nbconvert import HTMLExporter


class File(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename_to_db = 'error'
        self.fileformat_to_db = 'error'
        self.binary = b''
        self.desktop = winshell.desktop()


    def get_filename_and_format(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'Open File', rf'{self.desktop}', 'All Files (*)')
            if path:
                self.filename_to_db, self.fileformat_to_db = path[0].split(r'/')[-1].split('.')
                self.convert_to_binary_data(path[0])
        except Exception as e:
            print(e)

    def convert_to_binary_data(self, path):
        # Преобразование данных в двоичный формат
        with open(path, 'rb') as file:
            self.binary = file.read()


    @staticmethod
    def show_answer(filename, fileextension, file):
        info = QMessageBox()
        info.setBaseSize(400,100)
        info.setWindowTitle('Показать ответ')
        info.setText('Конвертировать или сохранить в исходном формате?\nТолько для ipynb')
        info.setStandardButtons(QMessageBox.StandardButton.Save|QMessageBox.StandardButton.Apply)
        button = info.exec()

        if button == QMessageBox.StandardButton.Save:
            print('Сохраняю')
            fullname = File.join_name_format(filename, fileextension)
            File.write_to_file(fullname, file)

        if button == QMessageBox.StandardButton.Apply:
            print('Открываю')
            fullname = File.join_name_format(filename, fileextension)
            path = File.write_to_file(fullname, file)
            if fileextension == 'ipynb':
                print('Конвертирую')
                path_in = path
                path_out = '\\'.join([winshell.desktop(), 'temp_dir_for_ds', f"{filename}.html"])
                File.convert_ipynb_to_html(path_in, path_out)

    @staticmethod
    def join_name_format(filename, fileextension):
        # file_name_format = '.'.join(['_'.join(self.filename_to_db.split(' ')),self.fileformat_to_db])
        full_filename = '.'.join([filename, fileextension])
        print(full_filename)
        return full_filename


    @staticmethod
    def write_to_file(fullname, file):
        path = '\\'.join([winshell.desktop(), 'temp_dir_for_ds', fullname])
        with open(path, 'wb') as f:
            f.write(file)
        return path

    # @staticmethod
    # # def open_file(format, path):
    #     # try:
    #     #     if format == 'ipynb':
    #     #         exec = rf"nbopen C:\2.ipynb"
    #     #         print(exec)
    #     #         subprocess.Popen(exec)
    #     #     else:
    #     #         os.startfile(rf"{path}", "open")
    #     # except Exception as e:
    #     #     print(e)

    @staticmethod
    def convert_ipynb_to_html(path_in, path_out):
        # notebook_filename = "Lesson_1.ipynb"
        # notebook_html_filename = "Lesson_1.html"

        try:
            with open(path_in, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
                nb_pdf, _ = nbconvert.export(HTMLExporter, nb)
            # nb_pdf, _ = nbconvert.export(PDFExporter, nb)
            # nb_pdf, _ = nbconvert.export(WebPDFExporter, nb)

            with open(path_out, 'wb') as f:
                f.write(nb_pdf.encode('utf-8'))
        except Exception as e:
            print(e)
