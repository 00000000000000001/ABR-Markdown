from docxTools import rm
from gui import showMsg


def removeComments(doc):
    wasEdited = False
    consume = False

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
                    wasEdited = True
                    text = rm(i, j, p).text
                    if i < len(text) and (
                        i == 0 or (text[i] == "\n" and text[i - 1] == "\n")
                    ):
                        while i < len(text) and text[i] == "\n":
                            text = rm(i, i, p).text
                else:
                    break
            elif text[i] == "\n" and consume:
                text = rm(i, i, p).text
            else:
                consume = False
                i = text.find("{", i)

    return wasEdited
