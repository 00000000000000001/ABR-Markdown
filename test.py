text = "{123}\nasd{123}"

i = 0
while i < len(text):
    if text[i] == "{":
        while text[i] != "}":
            text = text[:i] + text[i+1:]
        text = text[:i] + text[i+1:]
        # consume spaces
        while i < len(text)and text[i] == "\n":
            text = text[:i] + text[i+1:]
    i += 1
print(text)