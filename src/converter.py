import config
import glob
import re
import docx
import fcntl
import sys
import os
from docxTools import docText
import comments, paragraph, bulletList


def hasBriefkommando(string):
    return re.search(r"\$\[.+\]\$", string)


def hasMDSyntax(string):
    return (
        re.search(r"\{.+\}", string)
        or re.search(r"[\r\n]{2,}", string)
        or re.search(r"\*\*.*", string)
    )


def convert_file(doc):
    wasEdited = False
    try:
        wasEdited |= comments.removeComments(doc)
        wasEdited |= paragraph.subdivide(doc)
        wasEdited |= bulletList.substitute(doc)
    except:
        print("Error when converting docx")
    return wasEdited


def showMessage(text):
    os.system(
        'osascript -e \'tell app "Tomedo" to display dialog "'
        + text
        + '" buttons {"OK"} default button "OK"\''
    )


lock_file_path = "/tmp/my_script.lock"

# Versuchen, einen exklusiven Lock auf der Datei zu setzen
try:
    lock_file = open(lock_file_path, "w")
    fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    print("Das Skript wird bereits ausgeführt. Beende.")
    sys.exit(1)


# Hier folgt der eigentliche Code des Skripts

from gui import fenster, updateProgress
from threading import *


def threading():
    t1 = Thread(target=work)
    t1.start()


def work():
    file_input = config.TOMEDO_CACHE_PROXY

    briefe = glob.glob(file_input + "*.docx")

    number = len(briefe)
    step = 100 / number

    for brief in briefe:

        doc = docx.Document(brief)
        text = docText(doc)
        if hasBriefkommando(text) or not hasMDSyntax(text):
            updateProgress(step)
            continue

        if convert_file(doc):
            doc.save(brief)

        updateProgress(step)

    fenster.after(555, lambda: fenster.quit())


threading()

fenster.mainloop()


# Am Ende den Lock freigeben
fcntl.flock(lock_file, fcntl.LOCK_UN)
lock_file.close()
