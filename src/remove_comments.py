from docx_tools import rm

def getText(doc):
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)


def comments(document):
    edited = False
    delete = False
    consume = False
    for p in document.paragraphs:
        i = 0
        while i < len(p.text):
            if p.text[i] == "}":
                rm(i,i,p)
                delete = False
                consume = True
                continue
            if delete:
                rm(i,i,p)
                continue
            if p.text[i] == "{":
                delete = True
                edited = True
                continue
            if p.text[i] == "\n" and consume:
                rm(i,i,p)
                continue
            consume = False
            i += 1
    return edited
