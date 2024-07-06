from aws_cdk import App
from csa_group_assignment.csa_group import MyCdkStack
#from csa_group_assignment.s3_bucket_stack import S3BucketStack

app = App()
MyCdkStack(app, "MyCdkStack")
#S3BucketStack(app, "S3BucketStack")
app.synth()
