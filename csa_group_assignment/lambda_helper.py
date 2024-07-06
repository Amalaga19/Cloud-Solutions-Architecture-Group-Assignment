from aws_cdk import aws_lambda as lambda_
from constructs import Construct

def create_lambda_function(scope: Construct, id: str, handler_path: str):
    return lambda_.Function(scope, id,
                            runtime=lambda_.Runtime.PYTHON_3_8,
                            handler="main.handler",
                            code=lambda_.Code.from_asset(handler_path))
