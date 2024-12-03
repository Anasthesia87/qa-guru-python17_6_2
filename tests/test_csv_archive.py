import csv
import zipfile
from files_pathes import *


def test_csv_to_zip(create_archive):
    with zipfile.ZipFile(ARCHIVE_PATH) as u_f:
        csv_archived = u_f.extract('user_file.csv')
        with open(csv_archived) as user_file:
            csv_rows = csv.reader(user_file)
            new_list = []
            for row in csv_rows:
                new_list.append(row)
            assert len(new_list) == 3
            assert new_list == [['1', 'alice', 'alice@example.com'],
                                ['2', 'bob', 'bob@example.com'],
                                ['3', 'carol', 'carol@eample.com']]
        os.remove('user_file.csv')

        assert os.path.exists(ARCHIVE_PATH)


def test_archive_deleted(create_archive):
    os.remove(ARCHIVE_PATH)
    assert not os.path.exists(ARCHIVE_PATH)
