import re
import docx_utils
import config

def copy_to_new_paragraph(p, text, run, style=None):
    new_p = docx_utils.insert_paragraph_after(p, "", style)
    runner = new_p.add_run(text)
    runner.bold = run.bold
    runner.italic = run.italic
    runner.underline = run.underline
    runner.font.color.rgb = run.font.color.rgb
    runner.font.name = run.font.name
    runner.font.size = run.font.size

def insert_bullet_list(p):
    for run in p.runs:
        i = 0
        while i < len(run.text.splitlines()):
            line = run.text.splitlines()[i]
            if re.match(r"^(\*\*)(.*)$", line):
                if (
                    docx_utils.concate(run.text.splitlines()[i + 1 :]) != ""
                    or config.LEAVE_EMPTY_PARAGRAPH_AFTER_LIST
                ):
                    copy_to_new_paragraph(
                        p, docx_utils.concate(run.text.splitlines()[i + 1 :]), run
                    )
                p.text = docx_utils.concate(p.text.splitlines()[:i])
                value = re.split(r"^(\*\*)(.*)$", line)[2]
                copy_to_new_paragraph(p, value, run, "List Bullet")
            if p.text == "":
                docx_utils.delete_paragraph(p)
                break
            i += 1

def run(document):
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        insert_bullet_list(p)
        j += 1
