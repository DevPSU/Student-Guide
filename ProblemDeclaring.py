import json
import boto3

s3 = boto3.client('s3')
def lambda_handler(event, context):
    bucket = 'whendeclaremajordata'
    key = 'CourseControlledMajors.csv'
    result = ""
    try:
        courseList = ["aerospace engineering","architectural engineering","biomedical engineering","chemical engineering","civil engineering","computer engineering","computer science","industrial engineering","mechanical engineering","nuclear engineering","accounting","corporate innovation and entrepreneurship","finance","management","management information systems","marketing","risk management","supply chain and information systems","cybersecurity","ist","sra"]
        data_obj = s3.get_object(Bucket=bucket, Key=key)
        data = data_obj['Body'].read()
        data = data.decode('utf-8')
        listRequirements = data.split("\r\n")
        slotList = event['currentIntent']['slots']
        major = slotList["Major"]
        sem = int(slotList["numCredits"])
        gpa = float(slotList["GPA"])
        spot = courseList.index(major.lower())
        temp = listRequirements[spot].split(',')
        if major.lower() in courseList:
            if (sem < 4):
                message = "You must wait until your Sophmore year to declare a major."
            elif (gpa < float(temp[1])):
                message = "You do not meet the minimum GPA requirement."
            else:
                message = "You may be missing the required courses."
        else:
            message = "This course has no requirements."
    except Exception as e:
        print(e)
        message = "Invalid or unsupported input"
    return {
            "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
            "contentType": "PlainText",
            "content": message
            }
        }
    }
