#!/usr/bin/env python3

from aws_cdk import core
from ec2_cloudwatch.ec2_cloudwatch_stack import Ec2CloudwatchStack

app = core.App()

# Replace the accoount and region with your information
env_CN = core.Environment(account="You account information", region="cn-northwest-1")
Ec2CloudwatchStack(app, "ec2-cloudwatch", env=env_CN)

app.synth()
