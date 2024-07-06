import boto3
import json

def handler(event, context):
    # Initialize the Transcribe client
    transcribe_client = boto3.client('transcribe')
    
    # Assuming the event contains the S3 bucket and object key
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Set up the transcription job parameters
    job_name = f"Transcription-{context.aws_request_id}"
    job_uri = f"s3://{bucket_name}/{file_key}"

    # Start transcription job
    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',  # or the format of your audio file
        LanguageCode='auto',  # or set a specific language code
        OutputBucketName=bucket_name
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
