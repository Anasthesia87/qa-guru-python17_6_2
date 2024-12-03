import pathlib
import zipfile
from files_pathes import *
import pytest


@pytest.fixture
def create_archive():
    with zipfile.ZipFile(ARCHIVE_PATH, mode='w') as zip_file:
        for file in pathlib.Path(FILE_PATH).iterdir():
            zip_file.write(file, arcname=file.name)
    assert len(os.listdir(RESOURCES_PATH)) == 1

    assert os.path.exists(ARCHIVE_PATH)
