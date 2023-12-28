import config
import os
import glob
import re
import utils
import remove_comments
import split_paragraph
import create_bullet_lists
import docx
import fcntl
import sys

# Markdown ist eine Singleton-Klasse

class Markdown(object):
    _instance = None

    account_hashes = True
    show_dialog = True

    def __new__(cls):
        if cls._instance is None:
            print("Creating the object")
            cls._instance = super(Markdown, cls).__new__(cls)
            # Put any initialization here.
            cls.init(cls)
        return cls._instance

    def init(self):
        # walk files in tomedo cache
        file_input = config.TOMEDO_CACHE_PROXY
        briefe = glob.glob(file_input + "*.docx")

        msg = ""
        for brief in briefe:  # contains hash accounting and file conversion
            try:
                print("untersuche: " + brief)
                file = self.open_file(brief)
                hash = utils.get_hash(file)
                if self.account_hashes and utils.is_registered(hash):
                    continue
                file_converted = self.convert_file(self, file)
                if file_converted == None:
                    utils.register_hash(hash)
                    file.close()
                    continue
                else:
                    hash_converted = utils.get_hash(file_converted)
                    utils.register_hash(hash_converted)
                    file.close()
                    file_converted.close()
                    msg += "[✅]" + re.split(r"(.*)/((.+).docx)", brief)[2] + "\n"
            except Exception as error:
                print("An exception occurred:", error)
                continue

        print("done.")
        if msg == "":
            msg = """ℹ️ Es wurden keine unfertigen Briefe gefunden. Falls Sie etwas anderes erwartet haben, öffnen Sie bitte Sie den Arztbrief, der erstellt werden soll und versuchen Sie es erneut."""

        if self.show_dialog:
            os.system(
                'osascript -e \'tell app "Tomedo" to display dialog "'
                + msg
                + '" buttons {"OK"} default button "OK"\''
            )
            # os.system(
            #     f"osascript -e 'tell app \"Tomedo\" to display notification \"{msg}\"'"
            # )

    def open_file(filename):
        return open(filename, "rb")

    def convert_file(self, file):
        doc = docx.Document(file.name)
        edited = (
            remove_comments.run(doc)
            | split_paragraph.run(doc)
            | create_bullet_lists.run(doc)
        )
        if edited:
            doc.save(file.name)
            return self.open_file(file.name)
        else:
            return None


lock_file_path = "/tmp/my_script.lock"

# Versuchen, einen exklusiven Lock auf der Datei zu setzen
try:
    lock_file = open(lock_file_path, "w")
    fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    print("Das Skript wird bereits ausgeführt. Beende.")
    sys.exit(1)

# Hier folgt der eigentliche Code des Skripts
Markdown()

# Am Ende den Lock freigeben
fcntl.flock(lock_file, fcntl.LOCK_UN)
lock_file.close()
