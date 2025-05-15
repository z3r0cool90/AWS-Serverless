import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Get task_id from path parameters
    task_id = event['pathParameters'].get('task_id')

    if not task_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'task_id is required'})
        }

    # Delete item from DynamoDB
    try:
        table.delete_item(
            Key={'task_id': task_id}
        )
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'message': f'Task {task_id} deleted'})
    }
