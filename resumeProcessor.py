import PyPDF2
from rake_nltk import Rake
from tkinter import *

# sample resume from https://www.albany.edu/
sampleResume1 = {"Name":"Test Tester",
                 "College":"Macalester College",
                 "Major":"Computer Science",
                 "Minor":"Mathematics",
                 "Language":["C++", "C#", "HTML", "Java", "Perl", "Python"],
                 "Operating Systems":["UNIX", "Windows", "Linux"],
                 "Database":["Oracle", "SQL MS Access"],
                 "Experience":[
                    {"Title":"Software Developer Intern",
                     "Company":"EDS Corporation",
                     "Description":["Participated in development of Windows-based Financial software packages for local businesses",
                                    "Instituted training program for interns regarding the software development process",
                                    "Used C++ and Java in business setting",
                                    "Conducted regression testing on Unix-based software packages"]},
                     {"Title":"Student Assistant Consultant",
                      "Company":"Macalester College Computer Center",
                      "Description":["Supported more than 300 student users of the residence hall LAN",
                                     "Analyzed and serviced hardware, software and networking issues",
                                     "Designed web pages for University administrative and academic sites using Dreamweaver and HTML"]},
                     {"Title":"Sales Associate",
                      "Company":"Old Navy",
                      "Description":["Excelled in customer service, assisting in search for appropriate sizes",
                                     "Executed accurate financial transactions involving, cash, credit and checks",
                                     "Trained new sales associates in store procedures and philosophy of customer service"]}
                 ]}

# resume from https://www.calpoly.edu/
sampleResume2 = {
    'Name': 'Test Tester',
    'College':'Macalester College',
    'Experience':[
        {'Job Title':'Software Engineer Intern',
         'Company':'Google',
         'Description':["Developed Google Assistant with Android Studio",
                        "Designed and implemented new service with Java, C++, Javascript, CSS, HTML, protocol buffers, and RPCs",
                        "Implemented firebase dynamic linking and URL resolution"]},
        {'Job Title':'Engineering Practicum Intern',
         'Company':'Google',
         'Description':["Developed tool in C++ and Javascript to expose relevant logging data to ads development team",
                        "Integrated 2 existing internal tools using Python"]},
        {'Job Title':'WLAN Systems Engineer Intern',
         'Company':'Broadcom',
         'Description':["Developed embedded graphics display library and UI for streaming audio devices",
                        "Generated power management, state of charge, and battery conditioning software and associated API’s",
                        "Created various API’s for WICED software development kit related to status and system state",
                        "Enhanced I2C libraries for specialized hardware support working with ASIC team",
                        "Utilized modern software development tools including: GIT, Gerrit, JIRA, Jenkins, and Confluence"]},
        {'Job Title':'Software Tester',
         'Company':'Tapestry Solutions',
         'Description':["Wrote and executed Test Cases for company software, discovered and documented steps to produce bugs",
                        "Collaborated with Tapestry Solutions and Software Quality Assurance team at Miro Technologies"]}],
    'Project':[
        {'Project Title':"Checkers Game",
         "Language":"Python",
         "Description":["Teamed with 2 students to create a checkers game; Coded entirely in Python with networking and a database backend",
                        "Players interact through GUI’s on their respective machines",
                        "Leaderboard generated with MMR rankings is displayed at the end of each game",
                        "Players have the option to review each move made in the game"]}],
    'Language':["Java", "Python", "C++", "MySQL", "C", "Javascript"],
    'Skills':["quality assurance practice", "testing", 'Mocking', 'Robotics', "embedded work"]
}

def extract_keywords_dict(dict):
    finalList = []
    r = Rake(max_length=1)
    for exp in dict["Experience"]:
        keywordDict = {}
        keywordList = []
        for eachDisc in exp["Description"]:
            r.extract_keywords_from_text(eachDisc)
            keywords = r.get_ranked_phrases()
            keywordList.append(keywords)
        keywordDict["Title"] = exp["Title"]
        keywordDict["Keywords"] = keywordList
        finalList.append(keywordDict)
    return finalList

print(extract_keywords_dict(sampleResume1))

def extract_keywords(file_path, length=4):
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
    return_string = ""
    for string in list:
        return_string += "_".join(string.split())+ " "
    return return_string