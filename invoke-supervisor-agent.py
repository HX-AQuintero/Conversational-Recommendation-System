import json
import boto3

def lambda_handler(event, context):
    data = event['body']
    client = boto3.client('bedrock-agent-runtime')

    data_dict = json.loads(data)
    input_text = data_dict['text']
    session_id = data_dict['sessionId']

    try:
        response = client.invoke_agent(
            agentId = 'insert-agent-id',
            agentAliasId = 'insert-agent-alias-id',
            sessionId = session_id,
            inputText = input_text,
            endSession = False
        )

        response_text = ''

        for event in response.get('completion', []):
            if 'chunk' in event and 'bytes' in event['chunk']:
                response_text += event['chunk']['bytes'].decode('utf-8')
        print(response_text)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': response_text
            })
        }
    
    except Exception as e:
        return {
           'statusCode': 500,
           'body': json.dumps({
               'error': str(e)
           }) 
        }

