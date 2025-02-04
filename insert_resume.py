import boto3
import json

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Load JSON resume data
try:
    with open('resume.json') as f:
        resume_data = json.load(f)
    print("Loaded JSON data:", resume_data)
except Exception as e:
    print(f"Error loading JSON file: {e}")
    exit()

# Insert data into DynamoDB
try:
    item = {
        'id': {'S': resume_data['id']},
        'name': {'S': resume_data['name']},
        'skills': {'SS': resume_data['skills']},
        'experience': {'S': json.dumps(resume_data['experience'])},
        'education': {'S': json.dumps(resume_data['education'])}
    }
    print("Inserting item:", item)

    dynamodb.put_item(
        TableName='Resumes',
        Item=item
    )
    print("Resume data inserted successfully!")
except Exception as e:
    print(f"Error inserting data: {e}")