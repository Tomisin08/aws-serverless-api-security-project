import json
import boto3
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        claims = (
            event.get('requestContext', {})
                 .get('authorizer', {})
                 .get('jwt', {})
                 .get('claims', {})
        )

        user_id = claims.get('sub')

        if not user_id:
            logger.warning("Unauthorized request - no user ID found in token claims")
            return {
                'statusCode': 401,
                'body': json.dumps({'message': 'Unauthorized'})
            }

        logger.info(f"User accessed orders: {user_id}")

        response = table.scan()
        items = response.get('Items', [])

        user_orders = [
            item for item in items
            if item.get('userId') == user_id
        ]

        logger.info(f"Orders returned for user {user_id}: {len(user_orders)}")

        return {
            'statusCode': 200,
            'body': json.dumps(user_orders)
        }

    except Exception as e:
        logger.error(f"Lambda error in getOrdersFunction: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal Server Error'})
        }