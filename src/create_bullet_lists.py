from docx_tools import cp, appendParagraph, deleteParagraph
import re


# Ersetzungsregeln Bullet List (BL)
# I:    (** v)n|(• v)n
# II:   (** v\nw)n|(• v)n(w)n+1
# III:  (w\n** v)n|(w)n(• v)n+1
# IV:   (w\n** v1\nv2)n|(w)n(• v)n+1(v2)n+2


def blI(paragraph):
    text = paragraph.text
    posOfBullet = text.find("** ")
    if (
        posOfBullet == 0
        # and len(text) >= 3
        and not re.search(r"\n", text[3:])
    ):
        pN = appendParagraph(paragraph, "", "List Bullet")
        cp(3, len(text) - 1, paragraph, pN)
        deleteParagraph(paragraph)
        return True
    return False


def blII(paragraph):
    text = paragraph.text
    posOfBullet = text.find("** ")
    if (
        posOfBullet == 0
        # and len(text) >= 3
        and re.search(r"\n", text[posOfBullet + 3 :])
    ):
        pN = appendParagraph(paragraph, "", "List Bullet")
        posOfLineBreak = text.find("\n")
        cp(3, posOfLineBreak - 1, paragraph, pN)
        pN1 = appendParagraph(pN)
        cp(posOfLineBreak + 1, len(text) - 1, paragraph, pN1)
        deleteParagraph(paragraph)
        return True
    return False


def blIII(paragraph):
    text = paragraph.text
    posOfBullet = text.find("\n** ")
    if posOfBullet > -1 and not re.search(r"\n", text[posOfBullet + 4 :]):
        pN = appendParagraph(paragraph)
        cp(0, posOfBullet - 1, paragraph, pN)
        pN1 = appendParagraph(pN, "", "List Bullet")
        cp(posOfBullet + 4, len(text) - 1, paragraph, pN1)
        deleteParagraph(paragraph)
        return True
    return False


def blIV(paragraph):
    text = paragraph.text
    posOfBullet = text.find("\n** ")
    if posOfBullet > -1 and re.search(r"\n", text[posOfBullet + 4 :]):
        pN = appendParagraph(paragraph)
        cp(0, posOfBullet - 1, paragraph, pN)
        pN1 = appendParagraph(pN, "", "List Bullet")
        posOfLineBreak = text[posOfBullet + 4 :].find("\n") + posOfBullet + 4
        cp(posOfBullet + 4, posOfLineBreak - 1, paragraph, pN1)
        pN2 = appendParagraph(pN1)
        cp(posOfLineBreak + 1, len(text) - 1, paragraph, pN2)
        deleteParagraph(paragraph)
        return True
    return False


def bulletList(doc):
    wasEdited = False
    try:
        l = 0
        while l < len(doc.paragraphs):
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
