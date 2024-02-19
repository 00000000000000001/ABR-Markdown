from docxTools import mv, rm, duplicate


def process(p):
    wasEdited = False
    split = False
    text = p.text
    i = 0
    while i < len(text):
        if text[i] == "\n":
            if split == True:
                p_new = duplicate(p)
                p_new.text = ""
                mv(i + 1, len(text) - 1, p, p_new)
                rm(i - 1, i, p)
                text = p.text
                split = False
                wasEdited = True
            else:
                split = True
        else:
            split = False
        i += 1
    return wasEdited


def subdivide(doc):
    wasEdited = False
    j = 0
    while j < len(doc.paragraphs):
        print("inserting paragrapgs in paragraph " + str(j) + " (" + str(doc) + ")")
        p = doc.paragraphs[j]
        wasEdited |= process(p)
        j += 1
    return wasEdited
