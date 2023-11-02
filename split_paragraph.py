import re
import docx_utils
import config


def split_paragraph(p, document):
    text = p.text
    text = re.sub(r"\n\s*\n", "\n>>>\n", text)
    for j in range(len(text.splitlines())):
        line = text.splitlines()[j]
        if re.match(config.RE_LINE_BREAK, line):
            docx_utils.insert_paragraph_after(
                p,
                docx_utils.concate(text.splitlines()[j + 1 :]),
                document.styles["Normal"],
            )
            p.text = docx_utils.concate(text.splitlines()[0:j])
            break


def run(document):
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        split_paragraph(p, document)
        j += 1
