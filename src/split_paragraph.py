from docx_tools import mv, rm, duplicate

def process(p):
    edited = False
    split = False
    i = 0
    while i < len(p.text):
        if p.text[i] == "\n":
            if split == True:
                p_new = duplicate(p)
                p_new.text = ""
                mv(i + 1, len(p.text) - 1, p, p_new)
                rm(i - 1, i, p)
                split = False
                edited = True
            else:
                split = True
        else:
            split = False
        i += 1
    return edited


def para(document):
    edited = False
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        edited |= process(p)
        j += 1
    return edited
