import config
import os
import glob
import re
import utils
import remove_comments
import split_paragraph
import create_bullet_lists
import docx

def open_file(filename):
    return open(filename, "rb")

def convert_file(file):
    doc = docx.Document(file.name)
    edited = (
        # remove_comments.run(doc)
        split_paragraph.run(doc)
        # | create_bullet_lists.run(doc)
    )
    if edited:
        doc.save(file.name)
        return open_file(file.name)
        # True
    else:
        return None

# walk files in tomedo cache
file_input = config.TOMEDO_CACHE_PROXY
briefe = glob.glob(file_input + "*.docx")

msg = ""
for brief in briefe:  # contains hash accounting and file conversion
    try:
        file = open_file(brief)
        hash = utils.get_hash(file)
        if utils.is_registered(hash):
            continue
        file_converted = convert_file(file)
        if file_converted == None:
            utils.register_hash(hash)
            file.close()
            continue
        else:
            hash_converted = utils.get_hash(file_converted)
            utils.register_hash(hash_converted)
            file.close()
            file_converted.close()
            msg += "✅" + re.split(r"(.*)/((.+).docx)", brief)[2] + "\n"

    except Exception as error:
        print("An exception occurred:", error)
        continue


if msg == "":
    msg = """ℹ️ Es wurden keine unfertigen Briefe gefunden. Falls Sie etwas anderes erwartet haben, öffnen Sie bitte Sie den Arztbrief, der erstellt werden soll und versuchen Sie es erneut."""

os.system('osascript -e \'tell app "Tomedo" to display dialog "' + msg + "\"'")
