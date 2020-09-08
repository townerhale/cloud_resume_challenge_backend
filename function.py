import boto3
import json
import os


def handler(event, context): 

    dynamodb = boto3.resource('dynamodb')
    TABLE_NAME = os.getenv("TABLE_NAME", "Fake_table")
    table = dynamodb.Table(TABLE_NAME) #reference your table methods. 

    databaseResponse = table.update_item(
        Key={
        "id": "visitorCount"  #primary key
        },
        UpdateExpression='ADD visit_count :inc', #attribute visit_count, increment by 1
        ExpressionAttributeValues={
            ':inc': 1
        },   
        ReturnValues= "UPDATED_NEW" #update new attribute
    )

    responseBody = json.dumps({"visitorCount": int(float(databaseResponse["Attributes"]["visit_count"]))})

     # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS" 
        },
    }

    # Return api response object, which holds ResponseBody
    return apiResponse 

