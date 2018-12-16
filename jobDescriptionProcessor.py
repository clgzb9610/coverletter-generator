from rake_nltk import Rake
import io

# https://www.linkedin.com/jobs/view/summer-college-intern-software-engineer-windlogics-at-nextera-energy-999940117/
sampleJobDescription1 = {
    'Company' : "WindLogics",
    'Job Position':'Software Engineer',
    'Description':'This internship on the New Product Engineering team will include developing software and tools to help solve renewable energy analytics problems. The candidate can expect to employ modern software engineering methods and technologies to enable solutions in domain areas that may include load forecasting, wind power forecasting, smart grid analytics, distributed energy management, and customer service analytics. The candidate will achieve successful results by effectively participating in the WindLogics software development process, helping to build robust software solutions and articulating results to other business units.',
    'Job Function': ['Building software to acquire, process and visualize large datasets','Software testing','Participating in the WindLogics Scrum software development process.','Developing solutions for a cloud based environment','Evaluating cloud based tools and development frameworks'],
    'Qualification':['Proficiency in JavaScript, Scala, Python or R','Knowledge of both relational (SQL) and non-relational (NoSQL) data storage technologies and modeling','Familiarity writing software to utilize a cluster-computing framework (e.g., Spark)', 'Experience creating software intended to run in an elastic computing environment (e.g., Amazon Web Services)', 'Excellent analytical, interpersonal, communication and organizational skills']
}

def extract_keyword_from_job(dict):
    keywordDict = {}
    r = Rake()
    r.extract_keywords_from_text(dict["Description"])
    keywordDict["Description"] = r.get_ranked_phrases()
    functionList = []
    for eachFunction in dict['Job Function']:
        r.extract_keywords_from_text(eachFunction)
        functionList.append(r.get_ranked_phrases())
    keywordDict["Job Function"] = functionList
    qualificationList = []
    for eachQualification in dict['Qualification']:
        r.extract_keywords_from_text(eachQualification)
        qualificationList.append(r.get_ranked_phrases())
    keywordDict["Qualification"] = qualificationList
    return keywordDict

print(extract_keyword_from_job(sampleJobDescription1))



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