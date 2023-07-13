import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'Gem_Games'  

# Retrieve the queried item
queried_item = query_response.get('God of War 1')
if queried_item:
    print('Queried item:', queried_item)
else:
    print('Item not found')

# Delete an item from the table
item_to_delete = 'God of War 1'  
delete_response = dynamodb.delete_item(
    TableName=table_name,
    Key={
        'PrimaryKey': {'S': "God of War 1"}
        }
    )

print('Deletion response:', delete_response)
    
    