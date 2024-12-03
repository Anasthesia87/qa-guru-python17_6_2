from pypdf import PdfReader
import zipfile
from files_pathes import *


def test_pdf_to_zip(create_archive):
    with zipfile.ZipFile(ARCHIVE_PATH) as p_f:
        pdf_archived = p_f.extract('Python Testing with Pytest (Brian Okken).pdf')
        reader = PdfReader(pdf_archived)
        assert len(reader.pages) == 256
        page = reader.pages[1]
        text = page.extract_text()
        print(text)
        assert 'Copyright © 2017 The Pragmatic Programmers, LLC' in text
        os.remove('Python Testing with Pytest (Brian Okken).pdf')

        assert os.path.exists(ARCHIVE_PATH)


def test_archive_deleted(create_archive):
    os.remove(ARCHIVE_PATH)
    assert not os.path.exists(ARCHIVE_PATH)
