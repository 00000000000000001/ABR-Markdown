import docx_utils


def copy_to_new_paragraph(p, text, run, style=None):
    new_p = docx_utils.insert_paragraph_after(p, "", style)
    runner = new_p.add_run(text)
    runner.bold = run.bold
    runner.italic = run.italic
    runner.underline = run.underline
    runner.font.color.rgb = run.font.color.rgb
    runner.font.name = run.font.name
    runner.font.size = run.font.size
    return new_p


def delete_paragraph(paragraph):
    p = paragraph._element
    if p.getparent() is not None:
        p.getparent().remove(p)


def parse_next(str):
    arr = []
    i = 0
    new_line = True
    star = False
    while i < len(str):
        if str[i] == "*" and star:
            if str[i - 2] == "\n":
                arr.append(str[: i - 2])
            else:
                arr.append(str[: i - 1])
            i += 1
            value = ""
            while i < len(str) and str[i] != "\n":
                value += str[i]
                str = str[:i] + str[i + 1 :]
            arr.append(value)
            arr.append(str[i + 1 :])
            return arr
        elif new_line and str[i] == "*":
            star = True
            i += 1
            continue
        elif i < len(str) and str[i] == "\n":
            new_line = True
        else:
            new_line = False
        star = False
        i += 1
    return arr


def insert_bullet_list(p):
    edited = False
    for run in p.runs:
        arr = parse_next(run.text)
        if len(arr) == 3:
            if arr[0] != "":
                prev_p = copy_to_new_paragraph(p, arr[0], run)
            else:
                prev_p = p
            list_p = copy_to_new_paragraph(prev_p, arr[1], run, "List Bullet")
            if arr[2] != "":
                copy_to_new_paragraph(list_p, arr[2], run)
            delete_paragraph(p)
            edited = True
            return edited
    return edited


def run(document):
    edited = False
    j = 0
    while j < len(document.paragraphs):
        p = document.paragraphs[j]
        edited |= insert_bullet_list(p)
        j += 1
    return edited
