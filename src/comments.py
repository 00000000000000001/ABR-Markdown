from docxTools import rm
import re

# finde das erste { und merke pos({)
# gehe von dort weiter und merke die Pos des letzten }
# stoppen, wenn ein { oder das ende des Strings erreich ist.
# Kommentar beginnt bei pos({) und endet beim letzten pos(})


def removeComments(doc):
    wasEdited = False
    for p in doc.paragraphs:

        while re.search(r"\{.*\}", p.text):
            o = -1
            c = -1
            i = 0

            # suche Kommentar
            while i < len(p.text):
                if o > -1 and c > -1 and p.text[i] == "{":
                    break
                if o > -1 and i == len(p.text):
                    break
                if o == -1:
                    if p.text[i] == "{":
                        o = i
                elif o > -1 and p.text[i] == "}":
                    c = i
                i += 1

            # lösche Kommentar
            if o > -1 and c > -1:
                rm(o, c, p)
                wasEdited = True

            # lösche trailing \n
            if o >= len(p.text):
                continue
            if (o == 0 or p.text[o - 1] == "\n") and p.text[o] == "\n":
                while o < len(p.text):
                    if p.text[o] == "\n":
                        rm(o, o, p)
                        wasEdited = True
                    else:
                        break
    return wasEdited


# def removeComments(doc):
#     wasEdited = False
#     delete = False
#     consume = False
#     for p in doc.paragraphs:
#         i = 0
#         while i < len(p.text):
#             if p.text[i] == "}":
#                 rm(i, i, p)
#                 delete = False
#                 if i == 0 or p.text[i - 1] == "\n":
#                     consume = True
#                 continue
#             if delete:
#                 rm(i, i, p)
#                 continue
#             if p.text[i] == "{":
#                 delete = True
#                 wasEdited = True
#                 continue
#             if p.text[i] == "\n" and consume:
#                 rm(i, i, p)
#                 continue
#             consume = False
#             i += 1
#     return wasEdited
