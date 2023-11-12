def run(document):
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            i = 0
            while i < len(run.text):
                if run.text[i] == "{":
                    while i < len(run.text) and run.text[i] != "}":
                        run.text = run.text[:i] + run.text[i+1:]
                    run.text = run.text[:i] + run.text[i+1:]
                    # consume spaces
                    while i < len(run.text) and run.text[i] == "\n":
                        run.text = run.text[:i] + run.text[i+1:]
                i += 1