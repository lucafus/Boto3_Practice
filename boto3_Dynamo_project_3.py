import boto3

def lambda_handler(event, context):
    # Create DynamoDB client
    dynamodb = boto3.client('dynamodb')
    table_name = 'Gem_Games'  

    # Query an item from the table
    item_to_query = 'ItemToQuery' 
    query_response = dynamodb.get_item(
        TableName='Gem_Games',
        Key={
            'PrimaryKey': {'S': item_to_query}
        }
    )
    
    # Retrieve the queried item
    queried_item = query_response.get('Item')
    if queried_item:
        print('Queried item:', queried_item)
    else:
        print('Item not found')

    # Delete an item from the table
    item_to_delete = 'ItemToDelete'  # Replace with the item you want to delete
    delete_response = dynamodb.delete_item(
        TableName=table_name,
        Key={
            'PrimaryKey': {'title': "God of War 1"}
        }
    )

    print('Deletion response:', delete_response)
    
    