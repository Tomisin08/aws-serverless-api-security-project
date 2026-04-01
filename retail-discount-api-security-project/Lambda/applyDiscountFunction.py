import json
import boto3

ssm = boto3.client('ssm')

def get_api_key():
    response = ssm.get_parameter(
        Name='/myapp/api_key',
        WithDecryption=True
    )
    return response['Parameter']['Value']


def lambda_handler(event, context):
    
    # 👉 Get secret from Parameter Store
    api_key = get_api_key()
    print(f"API Key from Parameter Store: {api_key}")

    # 👉 Existing logic (your Step 11 code)
    code = event['queryStringParameters']['code']

    if not code.isalnum() or len(code) > 10:
        return {
            'statusCode': 400,
            'body': 'Invalid code'
        }

    return {
        'statusCode': 200,
        'body': f'Discount applied: {code}'
    }