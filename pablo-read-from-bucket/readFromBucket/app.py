import json
import boto3

# import requests
s3 = boto3.client('s3')

def lambda_handler(event, context):


    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket = bucket_name, Key= key)

    content = response['Body']

    print(content.read())




    #return {
    #    "statusCode": 200,
    #    "body": json.dumps({
    #        "message": "hello world",
    #        # "location": ip.text.replace("\n", "")
    #    }),
    #}
