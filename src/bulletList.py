import sys

from docx_tools import copyTextSegment as cp
from docx_tools import appendPara as append_paragraph
from docx_tools import deletePara as delete_paragraph
from gui import showMsg
import re
from traceback import print_exc


# Ersetzungsregeln Bullet List (BL)
# I:    (** u)n|(• u)n
# II:   (** u\n** v)n|(• u)n(** v)n+1
# III:  uw\n** v)n|(u)n(• v)n+1
# IV:   (u\n** v\n** w)n|(u)n(• v)n+1(** w)n+2


def blI(paragraph):
    text = paragraph.text
    posOfBullet = text.find("** ")
    if posOfBullet == 0 and not re.search(r"\n\*\* ", text[3:]):
        pN = append_paragraph(paragraph, "", "List Bullet")
        cp(paragraph, pN, 3, len(text) - 1)
        delete_paragraph(paragraph)
        return True
    return False


def blII(paragraph):
    text = paragraph.text
    posOfBullet = text.find("** ")
    if posOfBullet == 0 and re.search(r"\n\*\* ", text[posOfBullet + 3 :]):
        pN = append_paragraph(paragraph, "", "List Bullet")
        posOfLineBreak = text.find("\n** ")
        cp(paragraph, pN, 3, posOfLineBreak - 1)
        pN1 = append_paragraph(pN)
        cp(paragraph, pN1, posOfLineBreak + 1, len(text) - 1)
        delete_paragraph(paragraph)
        return True
    return False


def blIII(paragraph):
    text = paragraph.text
    posOfBullet = text.find("\n** ")
    if posOfBullet > -1 and not re.search(r"\n\*\* ", text[posOfBullet + 4 :]):
        pN = append_paragraph(paragraph)
        cp(paragraph, pN, 0, posOfBullet - 1)
        pN1 = append_paragraph(pN, "", "List Bullet")
        cp(paragraph, pN1, posOfBullet + 4, len(text) - 1)
        delete_paragraph(paragraph)
        return True
    return False


def blIV(paragraph):
    text = paragraph.text
    posOfBullet = text.find("\n** ")
    if posOfBullet > -1 and re.search(r"\n\*\* ", text[posOfBullet + 4 :]):
        pN = append_paragraph(paragraph)
        cp(paragraph, pN, 0, posOfBullet - 1)
        pN1 = append_paragraph(pN, "", "List Bullet")
        posOfLineBreak = text[posOfBullet + 4 :].find("\n** ") + posOfBullet + 4
        cp(paragraph, pN1, posOfBullet + 4, posOfLineBreak - 1)
        pN2 = append_paragraph(pN1)
        cp(paragraph, pN2, posOfLineBreak + 1, len(text) - 1)
        delete_paragraph(paragraph)
        return True
    return False


def substitute(doc):
    wasEdited = False
    try:
        l = 0
        while l < len(doc.paragraphs):

            showMsg(
                "replacing double asterisks in paragraph "
                + str(l)
                + " ("
                + str(doc)
                + ")"
            )

            if blI(doc.paragraphs[l]):
                wasEdited = True
                l += 1
                continue
            elif blII(doc.paragraphs[l]):
                wasEdited = True
                l += 1
                continue
            elif blIII(doc.paragraphs[l]):
                wasEdited = True
                l += 1
                continue
            elif blIV(doc.paragraphs[l]):
                wasEdited = True
                l += 2
                continue
            l += 1
        return wasEdited
    except:
        print("Error when converting the bullet list")
        print_exc()
        return False
