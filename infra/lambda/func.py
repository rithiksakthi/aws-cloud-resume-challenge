import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rithik-resume')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id':'0'
    })
    views = response['Item']['views']
    views = views + 1
    
    response = table.put_item(Item={
            'id':'0',
            'views': views
    })

    return views