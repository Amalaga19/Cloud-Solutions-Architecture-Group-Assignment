import boto3
import json

def handler(event, context):
    # Initialize the Translate client
    translate_client = boto3.client('translate')

    # Extract the text to translate from the event (modify as needed based on input structure)
    text_to_translate = event['text']

    # Perform translation
    result = translate_client.translate_text(
        Text=text_to_translate,
        SourceLanguageCode='auto',
        TargetLanguageCode='en'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'translatedText': result['TranslatedText']
        })
    }
