import json
import boto3

s3 = boto3.client('s3')
def lambda_handler(event, context):
    bucket = 'whendeclaremajordata'
    key = 'CourseControlledMajors.csv'
    result = ""
    try:
        coursesDict = {
            "0":"CHEM 110, MATH 140 and 141, MATH 250 or MATH 251, PHYS 211 and 212",
            "1":"CMPSC 132, MATH 140, 141, and 230, PHYS 211 and 212",
            "2":"ENGL 15 or 30, MATH 110 or 140, ECON 102, SCM or STAT 200, MGMT 301, ACCTG 211, MKTG 301, FIN 301",
            "6":"CHEM 110, MATH 140 and 141, MATH 250 or MATH 251, PHYS 211 and 212",
            "7":"CHEM 110, MATH 140 and 141, MATH 250 or MATH 251, PHYS 211 and 212"
        }
        data_obj = s3.get_object(Bucket=bucket, Key=key)
        data = data_obj['Body'].read()
        data = data.decode('utf-8')
        slotList = event['currentIntent']['slots']
        major = slotList["Major"]
        listRequirements = data.split("\r\n")
        resultList = []
        for x in listRequirements:
            temp = x.split(",")
            if(temp[0].lower() == major.lower()):
                result = "GPA:"+ temp[1]+ ", Credit Window:"+ temp[2] + ", Courses: " + coursesDict[temp[3]]
    except:
        result = "Invalid or unsupported input"
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
