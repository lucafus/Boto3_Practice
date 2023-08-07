import boto3

#Select the required resource

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

#Select the table

dynamodb.delete_table(TableName='Gem_Games')