import re
import sys
from docx_tools import extractOuterDocText
import comments, paragraph, bulletList
from traceback import print_exc

def checkAndConvert(doc):
    text = extractOuterDocText(doc)

    if hasBriefkommando(text) or not hasMDSyntax(text):
        return None

    if convertDoc(doc):
        return doc

def hasBriefkommando(string):
    return re.search(r"\$\[.+\]\$", string)


def hasMDSyntax(string):
    return (
        re.search(r"\{.+\}", string)
        or re.search(r"[\r\n]{2,}", string)
        or re.search(r"\*\*.*", string)
    )

def convertDoc(doc):
    wasEdited = False
    try:
        wasEdited |= comments.removeComments(doc)
        wasEdited |= paragraph.subdivide(doc)
        wasEdited |= bulletList.substitute(doc)
    except:
        print("Error when converting docx")
        print_exc()

    return wasEdited
