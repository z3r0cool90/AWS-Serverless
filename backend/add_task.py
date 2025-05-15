import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Parse the incoming POST request body
    body = json.loads(event.get('body', '{}'))
    task_description = body.get('task')

    if not task_description:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Task description is required'})
        }
    
    # Generate unique ID for the task
    task_id = str(uuid.uuid4())

    # Create the item to save
    item = {
        'task_id': task_id,
        'task': task_description
    }

    # Put the item into DynamoDB
    table.put_item(Item=item)

    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'message': 'Task added', 'task_id': task_id})
    }
