
# Boto3 is the name of the Python SDK for AW
import boto3

# Call the resources from AWS
dynamodb = boto3.resource('dynamodb', region_name= 'us-east-2')

table = dynamodb.create_table( 
    
    TableName= 'Gem_Games',
    
    AttributeDefinitions=[ 
            
            {
            
            'AttributeName': 'title', # Specify the name of the title attribute
            'AttributeType' : 'S'     # Specify that the title attribute is a string
            
            }
         ],
   
    KeySchema=[ 
            
            {   
            
            'AttributeName': 'title', # Specify that the title attribute will be used as the partition key
            'KeyType' : 'HASH'        # Specify that the title attribute will be used as the hash key
                        
            }
         ],
                      
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits' : 1
          
            }        
)

print(table)

