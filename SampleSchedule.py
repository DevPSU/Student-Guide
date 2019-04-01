import json

def lambda_handler(event, context):
    result = ""
    modifiedMajorList = []
    newString = ""
    slotList = event['currentIntent']['slots']
    major = slotList["Major"]
    school = slotList["School"]
    major = major.lower()
    school = school.lower()
    major = major.replace(" ", "-")
    
    if major == "architechural-engineering":
        result = "https://bulletins.psu.edu/undergraduate/colleges/"+school+"/"+major+"-bae/#suggestedacademicplantext"
    
    elif "and" in major:
        li = major.split("-")
        str = ""
        for ele in li:
            if ele == "and":
                ele = ""
                str = str + ele
            else:
                str = str+ele+"-"
        result = "https://bulletins.psu.edu/undergraduate/colleges/"+school+"/"+str+"bs/#suggestedacademicplantext"
    
    else:
        result = "https://bulletins.psu.edu/undergraduate/colleges/"+school+"/"+major+"-bs/#suggestedacademicplantext"
    
    return {"dialogAction": {
    "type": "Close",
    "fulfillmentState": "Fulfilled",
    "message": {
      "contentType": "PlainText",
      "content": result
    }
}
}