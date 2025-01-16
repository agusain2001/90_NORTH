import json

def lambda_handler(event, context):
    # Retrieve numbers from the event
    number1 = event.get('number1')
    number2 = event.get('number2')

    # Validate input
    if number1 is None or number2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input: Provide both "number1" and "number2".')
        }
    
    # Perform addition
    result = number1 + number2

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
