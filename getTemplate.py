"""
This file receives keywords and produces a template accordingly.
"""


# Here's the dictionary used for the matching between keywords and templates.
keyword_template_match = {}

"""A function takes in a keyword string as input and outputs a string of template"""
def get_template(keyword):
    if keyword in keyword_template_match:
        return keyword_template_match.get(keyword)
    else:
        print("Such keyword doesn't exist")
        return ""


"""A function that returns an introduction part for the cover letter"""
def get_introduction():
    return ""
