import sys

from docx_tools import removeTextSegment as rm
from gui import showMsg
from traceback import print_exc


def removeComments(doc):
    wasEdited = False

    for p in doc.paragraphs:
        text = p.text
        i = text.find("{")

        while i < len(text) and i > -1:

            showMsg(
                "searching for comments letter: "
                + str(i)
                + " text length: "
                + str(len(text))
            )
            if text[i] == "{":
                j = text.find("}", i)
                if not j == -1:
                    text = rm(p, i, j).text
                    wasEdited = True
                    if i < len(text) and (
                        i == 0 or (text[i] == "\n" and text[i - 1] == "\n")
                    ):
                        while i < len(text) and text[i] == "\n":
                            text = rm(p, i, i).text
                else:
                    break
                i = text.find("{", i)

    return wasEdited
