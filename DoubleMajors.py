import json

def lambda_handler(event, context):
    result = ""
    controlledMajors = ["Architectural Engineering",
                "Biomedical Engineering",
                "Chemical Engineering",
                "Civil Engineering",
                "Computer Engineering",
                "Computer Science",
                "Industrial Engineering",
                "Mechanical Engineering",
                "Nuclear Engineering",
                "Accounting",
                "Corporate Innovation and Entrepreneurship",
                "Finance",
                "Management",
                "Management Information Systems",
                "Marketing",
                "Risk Management",
                "Supply Chain and Information Systems",
                "Cybersecurity Analytics and Operations",
                "Information Sciences and Technology",
                "Security and Risk Analysis"]
    engMajors = ["Agricultural Engineering",
    "Architectural Engineering",
    "Aerospace Engineering",
    "Biological Engineering",
    "Biomedical Engineering",
    "Chemical Engineering",
    "Civil Engineering",
    "Computer Science",
    "Electrical Engineering",
    "Engineering Science",
    "Environmental Engineering",
    "Industrial Engineering",
    "Industrial and Management Systems",
    "Mechanical Engineering",
    "Nuclear Engineering"]
    mechanicalAndNuclear = ["Mechanical Engineering", "Nuclear Engineering"]
    doubleMajor = ["Spanish", "French", "German"]
    surveyingAndCivil = ["Surveying Engineering", "Civil Engineering"]
    mechanicalAndBiomedical = ["Biomedical Engineering", "Mechanical Engineering"]
    notAllowedOne = ["Electrical Engineering", "General Science"]
    notAllowedTwo = ["Computer Engineering", "Computer Science", "Mathematics Computational Option"]
    slotDict = event["currentIntent"]["slots"]
    if event["currentIntent"]["slots"]["MajorOne"] == event["currentIntent"]["slots"]["MajorTwo"]:
        result = "You have entered the same major twice."
    elif event["currentIntent"]["slots"]["MajorOne"] in mechanicalAndNuclear and event["currentIntent"]["slots"]["MajorTwo"] in mechanicalAndNuclear:
        result = "You are able to double major in these subjects.  You must first be admitted to the Mechanical Engineering program and add Nuclear Engineering as a second major."
    elif event["currentIntent"]["slots"]["MajorOne"] in mechanicalAndBiomedical and event["currentIntent"]["slots"]["MajorTwo"] in mechanicalAndBiomedical:
        result = "You are able to double major in these subjects.  You must first be admitted to the Biomedical Engineering program and add Mechanical Engineering as a second major."
    elif event["currentIntent"]["slots"]["MajorOne"] in surveyingAndCivil and event["currentIntent"]["slots"]["MajorTwo"] in surveyingAndCivil:
        result = "You are able to double major in these subjects. However, you must be enrolled in the Surveying Engineering at the Wilkes-Barre campus."
    elif event["currentIntent"]["slots"]["MajorOne"] in controlledMajors and event["currentIntent"]["slots"]["MajorTwo"] in controlledMajors:
        result = "You are unable to double major in these subjects."
    elif event["currentIntent"]["slots"]["MajorOne"] in notAllowedOne and event["currentIntent"]["slots"]["MajorTwo"] in notAllowedOne:
        result = "You are unable to double major in these subjects."
    elif event["currentIntent"]["slots"]["MajorOne"] in notAllowedTwo and event["currentIntent"]["slots"]["MajorTwo"] in notAllowedTwo:
        result = "You are unable to double major in these subjects."
    elif (event["currentIntent"]["slots"]["MajorOne"] in engMajors and event["currentIntent"]["slots"]["MajorTwo"] == "Liberal Arts") or (event["currentIntent"]["slots"]["MajorOne"] == "Liberal Arts" and event["currentIntent"]["slots"]["MajorTwo"] in engMajors):
        result = "You are able double major in these subjects, but some of the engineering majors may not be available."
    elif (event["currentIntent"]["slots"]["MajorOne"] in engMajors or event["currentIntent"]["slots"]["MajorTwo"] in engMajors) and (event["currentIntent"]["slots"]["MajorOne"] in doubleMajor or event["currentIntent"]["slots"]["MajorTwo"] in doubleMajor):
        result = "You are able double major in these subjects."
    else:
        result = "You may or may not be able to double major in these subjects.  You should make an appointment with your advisor to discuss this further."
    return {
            "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
            "contentType": "PlainText",
            "content": result
            }
        }
    }