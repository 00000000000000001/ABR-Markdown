import utils

def process(p):
    edited = False
    for run in p.runs:
        i = 0
        split = False
        while i < len(run.text):
            if run.text[i] == "\n":
                if split == True:
                    utils.copy_to_new_paragraph(p, run.text[i + 1 :], run)
                    run.text = run.text[: i - 1]
                    split = False
                    edited = True
                else:
                    split = True
            else:
                split = False
            i += 1
    return edited


def run(document):
    edited = False
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        edited |= process(p)
        j += 1
    return edited
