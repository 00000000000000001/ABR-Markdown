def parse_next(str):
    arr = []
    i = 0
    new_line = True
    star = False
    while i < len(str):
        if str[i] == "*" and star:
            if str[i-2] == "\n":
                arr.append(str[:i-2])
            else:
                arr.append(str[:i-1])
            i += 1
            value = ""
            while i < len(str) and str[i] != "\n":
                value += str[i]
                str = str[:i] + str[i+1:]
            arr.append(value)
            arr.append(str[i+1:])
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

test0 = "asd"
test1 = "**Item"
test2 = "w\n**Item"
test3 = "w\n**Item\nw"
test4 = "**Item1\n**Item2"
test5 = "**Item\nqwertz\nasd"
test6 = "\nasd\n**Item"
test7= "\nasd\nfds"
test8 = "\na\nb\nc**Item1"
test9 = "\na\nb\nc**Item1\n**Item2\nasd"
test10 = "**Item1**Item2"
test11 = "**Item1\n*Item2"

# print(parse_next_item(test2))

assert parse_next(test0) == []
assert parse_next(test1) == ["", "Item", ""]
assert parse_next(test2) == ["w", "Item", ""]
assert parse_next(test3) == ["w", "Item", "w"]
assert parse_next(test4) == ["", "Item1", "**Item2"]
assert parse_next(test5) == ["", "Item", "qwertz\nasd"]
assert parse_next(test6) == ["\nasd", "Item", ""]
assert parse_next(test7) == []
assert parse_next(test8) == []
assert parse_next(test9) == ["\na\nb\nc**Item1", "Item2", "asd"]
assert parse_next(test10) == ["", "Item1**Item2", ""]
assert parse_next(test11) == ["", "Item1", "*Item2"]