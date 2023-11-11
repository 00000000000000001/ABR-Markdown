import re
import config

def removeComment(line):
    return re.subn(config.RE_COMMENT, "", line)

def run(document):
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            if run.text == "\n":
                continue

            # remember font style
            bold = run.font.bold
            italic = run.font.italic
            underline = run.font.underline

            editedText = ''
            consume = False
            for j in range(len(run.text.splitlines())):
                tupel = removeComment(run.text.splitlines()[j])
                if (tupel[1] >= 1 and tupel[0] == ""):
                    consume = True
                    continue
                elif (consume and run.text.splitlines()[j] == ""):
                    continue
                consume = False
                # line = tupel[0]
                line = run.text.splitlines()[j]
                editedText += line + '\n'
            run.text = editedText[:-1]

            # adopt font style
            run.font.bold = bold
            run.font.italic = italic
            run.font.underline = underline
