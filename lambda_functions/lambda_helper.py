import os
from aws_cdk import aws_lambda as lambda_
from constructs import Construct

def create_lambda_function(scope: Construct, id: str, handler_directory: str, handler_file: str):
    base_dir = os.path.dirname(os.path.realpath(__file__))  # Gets the directory where lambda_helper.py is located
    handler_path = os.path.join(base_dir, handler_directory)  # Correctly navigate to the lambda_functions directory

    return lambda_.Function(scope, id,
                            runtime=lambda_.Runtime.PYTHON_3_8,
                            handler=f"{handler_file}.handler",
                            code=lambda_.Code.from_asset(handler_path))
