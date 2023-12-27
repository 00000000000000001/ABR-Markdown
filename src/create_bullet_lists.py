import utils
from docx_tools import rm, mv
import copy


def run(document):
    edited = False
    l = 0
    while l < len(document.paragraphs):
        p = document.paragraphs[l]
        p_last = p
        is_new_line = True
        could_be_a_list_item = False
        moved = False
        i = 0
        while i < len(p.text):
            if p.text[i] == "\n":
                is_new_line = True
                i += 1
                continue
            if is_new_line and p.text[i] == "*":
                could_be_a_list_item = True
                is_new_line = False
                moved = False
                i += 1
                continue
            if could_be_a_list_item and p.text[i] == "*":
                edited = True
                if i > 1:
                    rm(i - 2, i, p)
                    i -= 2
                else:
                    rm(i - 1, i, p)
                    i -= 1
                line = ""
                k = i

                # remove leading whitespaces
                while 0 < len(p.text) and p.text[i] == " ":
                    rm(i, i, p)

                while k < len(p.text) and p.text[k] != "\n":
                    line += p.text[k]
                    k += 1
                p_new = utils.insert_paragraph_after(p_last, "", "List Bullet")
                mv(i, k - 1, p, p_new)
                if p.text == "":
                    utils.delete_paragraph(p)
                    break
                p_last = p_new
                moved = True
                continue
            if moved and p.text[i] != "*":
                p_new = copy.deepcopy(p)
                p_new._p.clear()
                p_last._p.addnext(p_new._p)
                mv(i, len(p.text) - 1, p, p_new)
                if p.text[len(p.text) - 1] == "\n":
                    rm(len(p.text) - 1, len(p.text) - 1, p)
                    if p.text == "":
                        utils.delete_paragraph(p)
                        break
                p_last = p_new
                moved = False
                i += 1
                continue
            i += 1
        l += 1
    return edited
