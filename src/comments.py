from docxTools import rm


def removeComments(doc):
    wasEdited = False
    delete = False
    consume = False
    for p in doc.paragraphs:
        text = p.text 
        i = 0
        while i < len(text):
            print("Analysing letter: " + str(i) + " text length: " + str(len(text)))
            if text[i] == "}":
                rm(i, i, p)
                text = p.text 
                delete = False
                if i == 0 or text[i - 1] == "\n":
                    consume = True
                continue
            if delete:
                rm(i, i, p)
                text = p.text 
                continue
            if text[i] == "{":
                delete = True
                wasEdited = True
                continue
            if text[i] == "\n" and consume:
                rm(i, i, p)
                text = p.text 
                continue
            consume = False
            i += 1
    return wasEdited