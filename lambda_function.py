import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Fetch resume data from DynamoDB
    response = dynamodb.get_item(
        TableName='Resumes',
        Key={'id': {'S': '1'}}
    )

    # Check if the item exists
    if 'Item' in response:
        # Convert DynamoDB item to JSON
        resume_data = {
            'id': response['Item']['id']['S'],
            'name': response['Item']['name']['S'],
            'skills': response['Item']['skills']['SS'],
            'experience': json.loads(response['Item']['experience']['S']),
            'education': json.loads(response['Item']['education']['S'])
        }

        # Return the resume data
        return {
            'statusCode': 200,
            'body': json.dumps(resume_data, indent=2)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Resume not found'})
        }