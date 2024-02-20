import tkinter as tk
from tkinter import ttk

fenster = tk.Tk()
fenster.columnconfigure(0, weight=1)
fenster.resizable(False, False)
fenster.title("Markdown")

labelInfo = tk.Label(fenster, text="-", justify="left", anchor="w", width=35)
labelInfo.grid(column=0, row=0, columnspan=2, rowspan=1, sticky="w")

labelFortschritt = tk.Label(fenster, text="Gesamtfortschritt: ", justify="left", anchor="w")
labelFortschritt.grid(column=0, row=1, columnspan=1, rowspan=1, sticky="w")

progress = ttk.Progressbar(fenster, orient="horizontal", length=200, maximum=100)
progress.grid(column=1, row=1, columnspan=1, rowspan=1, sticky="w")

def showMsg(string):
    labelInfo.config(text=string)
    print(string)

def updateProgress(step):
    progress["value"] += step
    # if progress["value"] >= progress["maximum"]:
    #     fenster.after(555, lambda: fenster.quit())