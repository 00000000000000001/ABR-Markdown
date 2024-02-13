import sys

sys.path.append("../src")
sys.path.append("./src")

from docx import Document
from comments import removeComments
from docxTools import delete_paragraph



import random

def generate_random_string():
    characters = []
    possible_characters = ['A','{', '}']
    
    for n in range(len(possible_characters) * 10):
        for _ in range(random.randint(0,1)): 
            characters.append(random.choice(possible_characters))
    
    return ''.join(characters)


doc = Document()

shortest = 9999
shortestString = ""

for _ in range(100):
    p = doc.add_paragraph(generate_random_string())

    if len(p.text) < shortest:
        shortest = len(p.text)
        shortestString = p.text

    print("Vorher: " + p.text, end='')
    removeComments(doc)
    print(", Nachher: " + p.text)

    delete_paragraph(p)

print("shortest " + str(shortest) + ": " + shortestString)