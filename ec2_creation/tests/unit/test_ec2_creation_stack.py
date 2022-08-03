import aws_cdk as core
import aws_cdk.assertions as assertions

from ec2_creation.ec2_creation_stack import Ec2CreationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ec2_creation/ec2_creation_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Ec2CreationStack(app, "ec2-creation")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
