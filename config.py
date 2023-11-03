from pathlib import Path
from docx.shared import Pt

# program
TOMEDO_CACHE_PROXY = str(Path.home()) + "/.tomedoCache/temporaryFiles/proxy/"
SQLITE_FILE_NAME = str(Path(__file__).parent.resolve()) + "/sqlite.db"
# regex
RE_LINE_BREAK = r'^>>>$'
RE_COMMENT = r'({)([^}^{]*)(})'
RE_BULLETPOINT_LIST_ITEM = r'^(\*\*)(.*)$'
# document
NORMAL_FONT_NAME = "Nexa"
NORMAL_FONT_SIZE = Pt(10)
NORMAL_PARAGRAPH_SPACE_BEFORE = Pt(0)
NORMAL_PARAGRAPH_SPACE_AFTER = Pt(7)
# options
LEAVE_EMPTY_PARAGRAPH_AFTER_LIST = False