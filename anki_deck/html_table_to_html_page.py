# import OS module
import re
import os

fileObject = open("Anki Deck - Case Mix PS (py).html", "r",
                  encoding='utf-8', errors='ignore')
filedata = fileObject.read()

filedata_init = re.sub(
    "^", "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n<title></title>\n<meta name=\"description\" content=\"\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<link rel=\"stylesheet\" href=\"\">\n<style>\nbody{\ncolor: #b3b1ad;\nbackground-color: #0a0e14;\nfont-family: arial;\ntext-align: left;\nfont-size: 16px;\nfont-style: normal;\nfont-weight: normal;\nword-wrap: break-word;\n\nmargin-top: 7%;\nmargin-right: 10%;\nmargin-bottom: auto;\nmargin-left: 10%;\n}\ntable {\nbackground-color: #1b2733;\nborder: 1px solid #273747;\nborder-collapse: collapse;\nborder-spacing: 1%;\ntext-align: left;\nvertical-align: middle;\ntable-layout: fixed;\nwidth: 100%;\nmax-width: 100%;\nheight: auto;\n}\n\nth,\ntfoot {\ncolor: #268bd2;\nbackground-color: #1b2733;\nborder: 1px solid #273747;\nborder-collapse: collapse;\ntext-align: center;\nvertical-align: middle;\npadding: 1%;\n}\n\ntr,\ntd {\ncolor: #839496;\nbackground-color: #1b2733;\nborder: 1px solid #6994bf;\nborder-collapse: collapse;\ntext-align: left;\nvertical-align: middle;\npadding: 1%; \nword-wrap: break-word;\n}\nimg {\nmax-width: 100%;\nmin-width: 50%;\nmax-height: auto;\n\nopacity: 1;\ndisplay: block;\n\nmargin-left: auto;\nmargin-right: auto;\n\ntext-align: center;\n}\n</style></head>\n<body>\n", filedata)
filedata_regex_end = re.sub(
    "$", "<script script src=\"\" async defer></script>\n</body>\n</html>", filedata_init)

with open('index.html', 'w', encoding='utf-8', errors='ignore') as file:
    file.write(filedata_regex_end)
