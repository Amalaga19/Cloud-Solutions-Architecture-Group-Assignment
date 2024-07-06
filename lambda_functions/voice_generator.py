import boto3
import json

def handler(event, context):
    # Initialize the Polly client
    polly_client = boto3.client('polly')

    # Extract the translated text from the event
    text_to_speak = event['translatedText']

    # Request speech synthesis
    response = polly_client.synthesize_speech(
        Text=text_to_speak,
        OutputFormat='mp3',
        VoiceId='Joanna'  # or any other voice ID
    )

    # Save the audio stream returned by Polly to S3 (not shown here)
    # You'd typically write the stream to an S3 object

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Speech synthesis completed successfully'})
    }
