import random
import resumeProcessor
import jobDescriptionProcessor

"""
This file receives keywords and produces a template accordingly.
"""

# ===========Body Paragraph==================
languageList = ["Python", "Java", "C++", "C#", "C", "Ruby", "Javascript", "HTML", "CSS", "Ionic", "MySQL", "Perl", "React", "Go", "MongoDB", "Express", "Django", "Angular"]


# ===========Keyword Matching==================
# Here's the dictionary used for the matching between keywords and templates.
keyword_template_match = {}

"""A function takes in a keyword string as input and outputs a string of template"""
def get_template(keyword):
    if keyword in keyword_template_match:
        return keyword_template_match.get(keyword)
    else:
        print("Such keyword doesn't exist")
        return keyword

# ==========INTRODUCTION===================
def get_intro(position, company, resource, reason):
    return _input_position(position, company) + " " + _input_resource(resource) + " " + _input_reason(reason) + " " + _ending_sentence(position, company)

#private methods

position_template = ["I am excited to apply for the position of POSITION at COMPANY.",
                     "I am writing to apply for POSITION at COMPANY.",
                     "I am applying for POSITION at COMPANY."]

def _input_position(position, company):
    return random.choice(position_template).replace("POSITION", position).replace("COMPANY", company)

resource_template = ["I learned of this position through RESOURCE.", "I became aware of this position through RESOURCE."]

def _input_resource(resource):
    return random.choice(resource_template).replace("RESOURCE", resource)

def _input_reason(reason):
    return "This particular opportunity appeals to me because " + reason

ending_sentence_template = ["I believe that my past experience in Computer Science make me a well-suited candidate for POSITION position at COMPANY.",
                            "As someone with past experience working in the Computer Science field, I believe I am an excellent candidate for the POSITION position at COMPANY."]

def _ending_sentence(position, company):
    return random.choice(ending_sentence_template).replace("POSITION", position).replace("COMPANY", company)


# ===========CONCLUSION==================
def get_conclusion(passion, phone, email, company):
    return _input_concludingSentence(company) + " " + _input_contactinfo(phone, email) + " " + _input_passion(passion) + " " + _input_ending()

concludingSentence_template = ["I would be proud to contribute to and again be associated with the COMPANY, and I feel that I would be a valuable asset to your organization.",
                              "I trust that my immense skills and previous experience have prepared me for this opportunity to become an asset to COMPANY.",
                              "These experiences and skill sets directly correlate to this position and make me a well-qualified candidate.",
                               "I am confident that my combination of education, experience and skills makes me a competitive candidate and an excellent addition to COMPANY."]

def _input_concludingSentence(company):
    return random.choice(concludingSentence_template).replace("COMPANY", company)

contactIno_template = ["I can be reached at PHONE or via EMAIL."]

def _input_contactinfo(phone, email):
    return contactIno_template[0].replace("PHONE", phone).replace("EMAIL", email)

def _input_passion(passion):
    return passion

ending_template = ["Thank you for your time and consideration. \n\n Sincerely,\n"]
def _input_ending():
    return ending_template[0]