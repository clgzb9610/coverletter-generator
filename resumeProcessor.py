import PyPDF2
from rake_nltk import Rake

def text_extract(path):
    pdfObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObj)
    resumePage = pdfReader.getPage(0)
    text = resumePage.extractText()
    return text

resume = text_extract("resumes/sample4.pdf")
# print(resume)
fh = open("resume.txt","w")
fh.write(resume)
fh.close()

def process_text(file_path):
    fileIn = open(file_path, 'r')
    strList = fileIn.readlines()
    newStr = ""
    for i in strList:
        i = i.decode('utf-8').strip()
        if i != '':
            newStr = newStr + i
        else:
            newStr = newStr + " "
    return newStr

cleaned_string = process_text("resume.txt")
# print(cleaned_string)
# fh = open("resume.txt","w")
# fh.write(cleaned_string)
# fh.close()

r = Rake(min_length=4)
r.extract_keywords_from_text(cleaned_string)
keywords = r.get_ranked_phrases()
print(keywords)