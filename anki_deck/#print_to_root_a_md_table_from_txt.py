# import OS module
import re
import os

with open('anki_deck/anki_deck_preprint_template.txt', 'r') as t1:
    tempate = t1.read()

with open('anki_deck.md', 'w', encoding='utf-8', errors='ignore') as t2:
    t2.write(tempate)


fileObject = open("anki_deck/#anki_deck.txt", "r",
                  encoding='utf-8', errors='ignore')
filedata = fileObject.read()

filedata_regex1 = re.sub("^", "||\n---|---\n", filedata)
filedata_regex2 = re.sub("$", "|", filedata_regex1)
filedata_regex3 = re.sub("\t", "|", filedata_regex2)
filedata_regex4 = re.sub("\n", "|\n|", filedata_regex3)

with open('anki_deck.md', 'a', encoding='utf-8', errors='ignore') as f:
    f.write(filedata_regex4)
