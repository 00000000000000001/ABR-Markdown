import re
from docxTools import docText
import comments, paragraph, bulletList

def checkAndConvert(doc):
    text = docText(doc)

    if hasBriefkommando(text) or not hasMDSyntax(text):
        return None

    if convert_file(doc):
        return doc

def hasBriefkommando(string):
    return re.search(r"\$\[.+\]\$", string)


def hasMDSyntax(string):
    return (
        re.search(r"\{.+\}", string)
        or re.search(r"[\r\n]{2,}", string)
        or re.search(r"\*\*.*", string)
    )

def convert_file(doc):
    wasEdited = False
    try:
        wasEdited |= comments.removeComments(doc)
        wasEdited |= paragraph.subdivide(doc)
        wasEdited |= bulletList.substitute(doc)
    except:
        print("Error when converting docx")
    return wasEdited