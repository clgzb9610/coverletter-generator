from rake_nltk import Rake
import io

def process_text(file_path):                            # did not run without encoding so had to put that in.
    fileIn = io.open(file_path, 'r', encoding="utf-8")  # but now it has weird 'u' in front of every string
    strList = fileIn.readlines()
    newStr = ""
    for i in strList:
        i = i.strip()
        if i != '':
            newStr = newStr + i
        else:
            newStr = newStr + " "
    return newStr

cleaned_string = process_text("jobdesc/job1.txt")

j = Rake(min_length=4)
j.extract_keywords_from_text(cleaned_string)
job_keywords = j.get_ranked_phrases()
print(job_keywords[0:9])