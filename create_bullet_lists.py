import re
import docx_utils
import config

def insert_bullet_list(p):
    i = 0
    while i < len(p.text.splitlines()):
        line = p.text.splitlines()[i]
        if re.match(config.RE_BULLETPOINT_LIST_ITEM, line):
            value = re.split(config.RE_BULLETPOINT_LIST_ITEM, line)[2]
            docx_utils.insert_paragraph_after(p, docx_utils.concate(p.text.splitlines()[i+1:]))
            p.text = docx_utils.concate(p.text.splitlines()[:i])
            docx_utils.insert_paragraph_after(p, value, 'List Bullet')
        i += 1
        if p.text == '':
            docx_utils.delete_paragraph(p)
            break

def run(document):
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        insert_bullet_list(p)
        j += 1