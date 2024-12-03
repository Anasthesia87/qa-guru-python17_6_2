import pathlib
import zipfile
from files_paths import *
import pytest


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(RESOURCES_PATH):
        os.mkdir(RESOURCES_PATH)

    with zipfile.ZipFile(ARCHIVE_PATH, mode='w') as zip_file:
        for file in pathlib.Path(FILE_PATH).iterdir():
            if not file.is_dir():
                zip_file.write(file, arcname=file.name)

    assert os.path.exists(ARCHIVE_PATH), "Архив не был создан."

    yield ARCHIVE_PATH

    os.remove(ARCHIVE_PATH)
    assert not os.path.exists(ARCHIVE_PATH), "Архив не был удалён."
