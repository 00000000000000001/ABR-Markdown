import hashlib
import config
import docx
import remove_comments
import split_paragraph
import create_bullet_lists
import sqlite3
from docx.text.paragraph import Paragraph
from docx.oxml.shared import OxmlElement



def open_file(filename):
    return open(filename, "rb")


def get_hash(file):
    with file:
        bytes = file.read()
        hash = hashlib.md5(bytes).hexdigest()
    return hash


def is_registered(hash):
    con = sqlite3.connect(config.SQLITE_FILE_NAME)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hashes(hash)")
    res = cur.execute(f"SELECT hash FROM hashes WHERE hash = '{hash}'")
    is_registered = res.fetchone() is not None
    con.close()
    return is_registered


def getText(doc):
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)


def convert_file(file):
    doc = docx.Document(file.name)
    edited = (
        remove_comments.run(doc)
        | split_paragraph.run(doc)
        | create_bullet_lists.run(doc)
    )
    if edited:
        doc.save(file.name)
        return open_file(file.name)
        # True
    else:
        return None


def register_hash(hash):
    conn = sqlite3.connect(config.SQLITE_FILE_NAME)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO hashes (hash) VALUES ('{hash}')")
    conn.commit()
    conn.close()

def insert_paragraph_after(paragraph, text=None, style=None):
    """Insert a new paragraph after the given paragraph."""
    new_p = OxmlElement("w:p")
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    if text:
        new_para.add_run(text)
    if style is not None:
        new_para.style = style
    return new_para

def concate(arr):
    res = ''
    for line in arr:
        res += line + '\n'
    return res[:-1]

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    paragraph._p = paragraph._element = None

def copy_to_new_paragraph(p, text, run, style=None):
    new_p = insert_paragraph_after(p, "", style)
    runner = new_p.add_run(text)
    runner.bold = run.bold
    runner.italic = run.italic
    runner.underline = run.underline
    runner.font.color.rgb = run.font.color.rgb
    runner.font.name = run.font.name
    runner.font.size = run.font.size
    return new_p