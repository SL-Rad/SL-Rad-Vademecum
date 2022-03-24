# import OS module
import re
import os

fileObject = open("Anki Deck - Case Mix PS.txt", "r",
                  encoding='utf-8', errors='ignore')
filedata = fileObject.read()

filedata_regex1 = re.sub("^", "||\n---|---\n", filedata)
filedata_regex2 = re.sub("$", "|", filedata_regex1)
filedata_regex3 = re.sub("\t", "|", filedata_regex2)
filedata_regex4 = re.sub("\n", "|\n|", filedata_regex3)

with open('Anki Deck - Case Mix PS (py).md', 'w', encoding='utf-8', errors='ignore') as file:
    file.write(filedata_regex4)
