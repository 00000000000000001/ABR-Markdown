import re
import docx_utils
import config

def delete_paragraph(paragraph):
    p = paragraph._element
    if p.getparent() is not None:
        p.getparent().remove(p)
        p._p = p._element = None

def split_paragraph(p, document):
    for j in range(len(p.runs)):
        p.runs[j].text = re.sub(r"\n\s*\n", "\n>>>\n", p.runs[j].text)
        if re.search(r"\n>>>\n", p.runs[j].text):
            arr = re.split(r"\n>>>\n", p.runs[j].text)
            for str in reversed(arr):
                new_p = docx_utils.insert_paragraph_after(p, "")
                # adopt style
                runner = new_p.add_run(str)
                runner.bold = p.runs[j].bold
                runner.italic = p.runs[j].italic
                runner.underline = p.runs[j].underline
                runner.font.color.rgb = p.runs[j].font.color.rgb
                runner.font.name = p.runs[j].font.name
                runner.font.size = p.runs[j].font.size
            delete_paragraph(p)

def run(document):
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        split_paragraph(p, document)
        j += 1
