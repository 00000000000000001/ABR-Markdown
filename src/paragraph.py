from docxTools import rm, duplicate
from gui import showMsg

# Ersetzungsregeln Paragraph (P)
# I:    (u\n\nv)n|(u)n(v)n+1

def process(pN):
    wasEdited = False
    text = pN.text
    i = text.find("\n\n")
    if i != -1:
        pN1 = duplicate(pN)
        rm(i, len(text) - 1, pN)
        rm(0, i + 2 - 1, pN1)
        wasEdited = True

    return wasEdited


def subdivide(doc):
    wasEdited = False
    j = 0
    while j < len(doc.paragraphs):

        showMsg(
            "replacing double line breaks in paragraph "
            + str(j)
            + " ("
            + str(doc)
            + ")"
        )

        p = doc.paragraphs[j]
        wasEdited |= process(p)
        j += 1
    return wasEdited
