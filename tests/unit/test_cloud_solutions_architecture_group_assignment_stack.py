import aws_cdk as core
import aws_cdk.assertions as assertions

from csa_group_assignment.csa_group import CloudSolutionsArchitectureGroupAssignmentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cloud_solutions_architecture_group_assignment/cloud_solutions_architecture_group_assignment_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CloudSolutionsArchitectureGroupAssignmentStack(app, "cloud-solutions-architecture-group-assignment")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
