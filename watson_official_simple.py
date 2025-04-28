# Example 2: Adds user input.

from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Create Assistant service object.
authenticator = IAMAuthenticator('N4ROgFLSFheVexFDKTB8aQdyvclGz6QdfJEeXxHqPcAQ') # replace with API key
assistant = AssistantV2(
    version = '2023-04-15',
    authenticator = authenticator
)
assistant.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/8616d148-c668-4225-b8d7-dbde21052795') # replace with service instance URL
assistant_id = 'ae4f08ab-8988-4c06-9617-134169c58ee3' # replace with environment ID

# Initialize with empty value to start the conversation.
message_input = {
    'message_type': 'text',
    'text': ''
    }

context = None

# Main input/output loop
while message_input['text'] != 'quit':

    # Send message to assistant.
    result = assistant.message_stateless(
        assistant_id,
        input = message_input,
        context=context
    ).get_result()
    context = result['context']

    # Print responses from actions, if any. Supports only text responses.
    if result['output']['generic']:
        for response in result['output']['generic']:
            if response['response_type'] == 'text':
                print(response['text'])

    # Prompt for the next round of input unless skip_user_input is True.
    if not result['context']['global']['system'].get('skip_user_input', False):
        user_input = input('>> ')
        message_input = {
            'text': user_input
        }