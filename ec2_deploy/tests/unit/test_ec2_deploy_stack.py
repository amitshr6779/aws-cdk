import aws_cdk as core
import aws_cdk.assertions as assertions
from ec2_deploy.ec2_deploy_stack import Ec2DeployStack


def test_sqs_queue_created():
    app = core.App()
    stack = Ec2DeployStack(app, "ec2-deploy")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = Ec2DeployStack(app, "ec2-deploy")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
