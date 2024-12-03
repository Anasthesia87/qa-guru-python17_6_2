import csv
from pypdf import PdfReader
from openpyxl import load_workbook
import zipfile
from files_paths import *


def test_csv_to_zip(create_archive):
    with zipfile.ZipFile(ARCHIVE_PATH) as u_f:
        csv_archived = u_f.extract('user_file.csv')
        with open(csv_archived) as user_file:
            csv_rows = csv.reader(user_file)
            new_list = []
            for row in csv_rows:
                new_list.append(row)
            assert len(new_list) == 3, "Количество строк в выбранном файле не соответствует ожидаемому."
            assert new_list == [['1', 'alice', 'alice@example.com'],
                                ['2', 'bob', 'bob@example.com'],
                                ['3', 'carol', 'carol@example.com']], "Содержание выбранного файла не совпадает с ожидаемым."
        os.remove('user_file.csv')

        assert os.path.exists(ARCHIVE_PATH), "Архив был удален до окончания теста."


def test_pdf_to_zip(create_archive):
    with zipfile.ZipFile(ARCHIVE_PATH) as p_f:
        pdf_archived = p_f.extract('Python Testing with Pytest (Brian Okken).pdf')
        reader = PdfReader(pdf_archived)
        assert len(reader.pages) == 256, "Количество страниц в выбранном файле не соответствует ожидаемому."
        page = reader.pages[1]
        text = page.extract_text()
        print(text)
        assert 'Copyright © 2017 The Pragmatic Programmers, LLC' in text, "Содержание выбранного файла не совпадает с ожидаемым."
        os.remove('Python Testing with Pytest (Brian Okken).pdf')

        assert os.path.exists(ARCHIVE_PATH), "Архив был удален до окончания теста."


def test_xlsx_to_zip(create_archive):
    with zipfile.ZipFile(ARCHIVE_PATH) as x_f:
        xlsx_archived = x_f.extract('file_example_XLSX_50.xlsx')
        workbook = load_workbook(xlsx_archived)
        sheet = workbook.active
        assert sheet.cell(row=49, column=2).value == 'Demetria', "Значение в указанной ячейке не соответствует ожидаемому."
        os.remove('file_example_XLSX_50.xlsx')

        assert os.path.exists(ARCHIVE_PATH),"Архив был удален до окончания теста."
