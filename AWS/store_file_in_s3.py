import boto3
import json
import base64

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Retrieve bucket name and file data from the event
    bucket_name = event.get('bucket_name')
    file_name = event.get('file_name')
    file_content_base64 = event.get('file_content')  # Expecting base64-encoded file content
    
    # Validate input
    if not bucket_name or not file_name or not file_content_base64:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input: Provide "bucket_name", "file_name", and "file_content".')
        }
    
    try:
        # Decode the base64 file content
        file_content = base64.b64decode(file_content_base64)
        
        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} uploaded to bucket {bucket_name}.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
