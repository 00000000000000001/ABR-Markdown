import sys

sys.path.append("../src")
sys.path.append("./src")
from docx import Document
import comments, paragraph, bulletList

def test_wasEdited():
    doc = Document()
    p_src = doc.add_paragraph("")
    assert comments.removeComments(doc) | paragraph.subdivide(doc) | bulletList.substitute(doc) == False

    doc = Document()
    p_src = doc.add_paragraph("{}")
    assert comments.removeComments(doc) | paragraph.subdivide(doc) | bulletList.substitute(doc) == True

    doc = Document()
    p_src = doc.add_paragraph("FOO\n\nBAR")
    assert comments.removeComments(doc) | paragraph.subdivide(doc) | bulletList.substitute(doc) == True

    doc = Document()
    p_src = doc.add_paragraph("** FOO")
    assert comments.removeComments(doc) | paragraph.subdivide(doc) | bulletList.substitute(doc) == True

    doc = Document()
    p_src = doc.add_paragraph("FOO")
    assert comments.removeComments(doc) | paragraph.subdivide(doc) | bulletList.substitute(doc) == False

    # doc.save("test.docx")
