def iterate_run(p, i, new_line, star, arr):
    if i == len(p):
        return
    j = 0
    text = p[i][0]
    while j < len(text):
        if text[i] == "*" and star:
            True
            
        elif new_line and str[i] == "*":
            True
        elif i < len(str) and str[i] == "\n":
            True
        else:
            True
        j += 1
    arr[0].append(p[i])
    iterate_run(p, i+1, new_line, star, arr)



def iterate_paragraph(p):
    arr = [[], "", []]
    iterate_run(p, 0, True, False, arr)
    return arr


test1 = [["**Item"]]

print(iterate_paragraph(test1))

# assert test(test1) == [[],"Item", []]
