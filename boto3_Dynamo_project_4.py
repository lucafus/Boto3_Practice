import boto3

#Select the required resource

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

#define the table

table = dynamodb.Table('Gem_Games')

response = table.delete()

print("Table deleted succesfully")