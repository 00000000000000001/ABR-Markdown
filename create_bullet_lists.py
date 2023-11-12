import re
import docx_utils
import config

def insert_bullet_list(p):
    for run in p.runs:
        i = 0
        while i < len(run.text.splitlines()):
            line = run.text.splitlines()[i]
            if re.match(config.RE_BULLETPOINT_LIST_ITEM, line):
                value = re.split(config.RE_BULLETPOINT_LIST_ITEM, line)[2]
                if (
                    docx_utils.concate(run.text.splitlines()[i + 1 :]) != ""
                    or config.LEAVE_EMPTY_PARAGRAPH_AFTER_LIST
                ):
                    new_p = docx_utils.insert_paragraph_after(p, "")
                    runner = new_p.add_run(
                        docx_utils.concate(run.text.splitlines()[i + 1 :])
                    )
                    runner.bold = run.bold
                    runner.italic = run.italic
                    runner.underline = run.underline
                    runner.font.color.rgb = run.font.color.rgb
                    runner.font.name = run.font.name
                    runner.font.size = run.font.size
                p.text = docx_utils.concate(p.text.splitlines()[:i])
                new_p = docx_utils.insert_paragraph_after(p, "", "List Bullet")
                runner = new_p.add_run(value)
                runner.bold = run.bold
                runner.italic = run.italic
                runner.underline = run.underline
                runner.font.color.rgb = run.font.color.rgb
                runner.font.name = run.font.name
                runner.font.size = run.font.size
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