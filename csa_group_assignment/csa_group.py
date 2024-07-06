from aws_cdk import Stack
from constructs import Construct 
from .s3_bucket_stack import create_s3_bucket
from lambda_functions.lambda_helper import create_lambda_function
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets

class MyCdkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)


        self.bucket = create_s3_bucket(self, "Translations")
        self.transcriber_lambda = create_lambda_function(
        self, "TranscriberFunction", "../lambda_functions", "transcriber")
        self.translator_lambda = create_lambda_function(
        self, "TranslatorFunction", "../lambda_functions", "translator")
        self.voice_generator_lambda = create_lambda_function(
        self, "VoiceGeneratorFunction", "../lambda_functions", "voice_generator")
           # Define the Step Functions workflow
        self.state_machine = self.create_step_function()

    def create_step_function(self):
            start_state = tasks.LambdaInvoke(self, "StartTranscription",
                                            lambda_function=self.transcriber_lambda,
                                            output_path="$.Payload")

            translation_state = tasks.LambdaInvoke(self, "TranslateText",
                                                lambda_function=self.translator_lambda,
                                                input_path="$.Payload",
                                                output_path="$.Payload")

            voice_generation_state = tasks.LambdaInvoke(self, "GenerateVoice",
                                                        lambda_function=self.voice_generator_lambda,
                                                        input_path="$.Payload",
                                                        output_path="$.Payload")

            definition = start_state.next(translation_state).next(voice_generation_state)
            return sfn.StateMachine(self, "TranslationStateMachine", definition=definition)
    def create_event_rule(scope: Construct, state_machine):
        return events.Rule(scope, "TriggerRule",
                       event_pattern={
                           "source": ["aws.s3"],
                           "detail": {
                               "eventName": ["PutObject"],
                               "requestParameters": {
                                   "bucketName": ["Translations"],
                                   "key": [{
                                       "prefix": "!",
                                       "anything-but": "translations/"
                                   }]
                               }
                           }
                       },
                       targets=[targets.SfnStateMachine(state_machine)])