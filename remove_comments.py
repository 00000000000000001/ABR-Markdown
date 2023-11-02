import re
import config

def removeComment(line):
    return re.subn(config.RE_COMMENT, "", line)

def run(document):
    for paragraph in document.paragraphs:
        editedText = ''
        consume = False
        for j in range(len(paragraph.text.splitlines())):
            tupel = removeComment(paragraph.text.splitlines()[j])
            if (tupel[1] == 1 and tupel[0] == ""):
                consume = True
                continue
            elif (consume and paragraph.text.splitlines()[j] == ""):
                continue
            consume = False
            line = tupel[0]
            editedText += line + '\n'
        paragraph.text = editedText[:-1]