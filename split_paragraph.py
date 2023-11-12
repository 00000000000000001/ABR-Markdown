import re
import docx_utils

def split_paragraph(p, run, text):
    new_p = docx_utils.insert_paragraph_after(p, "")
    runner = new_p.add_run(text)
    runner.bold = run.bold
    runner.italic = run.italic
    runner.underline = run.underline
    runner.font.color.rgb = run.font.color.rgb
    runner.font.name = run.font.name
    runner.font.size = run.font.size

def process(p):
    for run in p.runs:
        i = 0
        split = False
        while i < len(run.text):
            if run.text[i] == "\n":
                if split == True:
                    split_paragraph(p, run, run.text[i+1:])
                    run.text = run.text[:i-1]
                    split = False
                else:
                    split = True
            else:
                split = False
            i += 1

def run(document):
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        process(p)
        j += 1
