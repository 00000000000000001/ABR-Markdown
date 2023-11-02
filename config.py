from pathlib import Path
from docx.shared import Pt

TOMEDO_CACHE_PROXY = str(Path.home()) + "/.tomedoCache/temporaryFiles/proxy/"
SQLITE_FILE_NAME = str(Path(__file__).parent.resolve()) + "/sqlite.db"
NORMAL_FONT_NAME = "Nexa"
NORMAL_FONT_SIZE = Pt(10)
