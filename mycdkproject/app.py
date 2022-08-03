#!/usr/bin/env python3

from aws_cdk import core
import aws_cdk as cdk

from mycdkproject.mycdkproject_stack import MycdkprojectStack

app = core.App()
MycdkprojectStack(app, "mycdkproject")

app.synth()