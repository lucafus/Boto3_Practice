import boto3

#Select the required resource

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

#define the table

table = dynamodb.Table('Gem_Games')

# Delete an item from the table

deletion = table.delete_item(
        Key={
            'title': 'God of War 1'
        }
    )
    
  
print('Deletion completed: ' , deletion)   