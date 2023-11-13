import hashlib
import config
import docx
import normal_paragraph_style
import remove_comments
import split_paragraph
import create_bullet_lists
import sqlite3

# def delete_paragraph(paragraph):
#     p = paragraph._element
#     if p.getparent() is not None:
#         p.getparent().remove(p)
#         p._p = p._element = None


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
