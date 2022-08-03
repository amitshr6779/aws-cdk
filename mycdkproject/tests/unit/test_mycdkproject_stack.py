import aws_cdk as core
import aws_cdk.assertions as assertions

from mycdkproject.mycdkproject_stack import MycdkprojectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in mycdkproject/mycdkproject_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MycdkprojectStack(app, "mycdkproject")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
