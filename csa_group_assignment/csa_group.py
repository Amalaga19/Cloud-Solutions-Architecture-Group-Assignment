from aws_cdk import Stack
# Import necessary CDK libraries for AWS services used
from constructs import Construct 
from .s3_bucket_stack import create_s3_bucket


class MyCdkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Your stack setup goes here

        self.bucket = create_s3_bucket(self, "Translations")
