import config
import glob
import fcntl
import sys
import os
import docx
from gui import fenster, updateProgress
from threading import *
from converterFunctions import checkAndConvert


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


def threading():
    t1 = Thread(target=work)
    t1.start()


def saveDivide(dividend, divisor):
    if divisor == 0:
        return dividend
    else:
        return dividend / divisor


def work():
    file_input = config.TOMEDO_CACHE_PROXY

    briefe = glob.glob(file_input + "*.docx")

    number = len(briefe)
    step = saveDivide(100, number)

    for brief in briefe:
        doc = docx.Document(brief)
        if checkAndConvert(doc) != None:
            doc.save(brief)
        updateProgress(step)

    fenster.after(555, lambda: fenster.quit())


threading()

fenster.mainloop()


# Am Ende den Lock freigeben
fcntl.flock(lock_file, fcntl.LOCK_UN)
lock_file.close()
