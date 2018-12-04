import PyPDF2
from rake_nltk import Rake
from tkinter import *


def extract_keywords(file_path, length=2):
    r = Rake(min_length=length)
    text = _text_extract(file_path)
    r.extract_keywords_from_text(_process_text(text))
    keywords = r.get_ranked_phrases()
    return _list_to_string(keywords)

def _text_extract(path):
    pdfObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObj)
    resumePage = pdfReader.getPage(0)
    text = resumePage.extractText()
    return text

# nltk.download('stopwords')

def _process_text(string):
    # fileIn = open(file_path, 'r')
    # strList = text_file.readlines()
    newStr = ""
    for i in string:
        i = i.strip()
        if i != '':
            newStr = newStr + i
        else:
            newStr = newStr + " "
    return newStr

def _list_to_string(list):
    string = ""
    for string in list:
        string += "".join(string.split()) + " "
    return string