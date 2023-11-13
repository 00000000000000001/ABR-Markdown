def getText(doc):
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)


def run(document):
    edited = False
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            i = 0
            while i < len(run.text):
                if run.text[i] == "{":
                    while i < len(run.text) and run.text[i] != "}":
                        run.text = run.text[:i] + run.text[i + 1 :]
                    run.text = run.text[:i] + run.text[i + 1 :]
                    if (i - 1 == -1 or run.text[i - 1] == "\n") and run.text[i] == "\n":
                        while i < len(run.text) and run.text[i] == "\n":
                            run.text = run.text[:i] + run.text[i + 1 :]
                    edited = True
                    i -= 1
                i += 1
    return edited
