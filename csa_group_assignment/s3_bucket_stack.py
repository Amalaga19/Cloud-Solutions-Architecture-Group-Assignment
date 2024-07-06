from aws_cdk import aws_s3 as s3
from constructs import Construct

def create_s3_bucket(scope: Construct, id: str):
    bucket = s3.Bucket(scope, id,
                        versioned=True,
                        block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
    return bucket
