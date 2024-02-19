def promptTK(label):
    if label.cget("text") == "analysiere...":
        label.config(text="analysiere")
    elif label.cget("text") == "analysiere":
        label.config(text="analysiere.")
    elif label.cget("text") == "analysiere.":
        label.config(text="analysiere..")
    elif label.cget("text") == "analysiere..":
        label.config(text="analysiere...")
