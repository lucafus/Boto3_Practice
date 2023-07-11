import boto3

dynamodb = boto3.resource('dynamodb', region_name= 'us-east-2')

def lambda_handler(event, context):
    table = dynamodb.Table('Gem_Games')

    response = table.delete_item(
        Key={
            'title': "God of War 1"
        }
    )
    
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    print(status_code)


print("Deleted Items succeded")
