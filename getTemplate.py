import random

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
        return keyword

def get_intro(position, resource, reason):
    return _input_position(position) + " " + _input_resource(resource) + " " + reason


#private methods

position_template = ["I am excited to apply for the position of POSITION.",
                     "I am writing to apply for POSITION.",
                     "I am applying for POSITION."]

def _input_position(position):
    return random.choice(position_template).replace("POSITION", position)

resource_template = ["I learned of this position through RESOURCE.", "I became aware of this position through RESOURCE."]

def _input_resource(resource):
    return random.choice(resource_template).replace("RESOURCE", resource)