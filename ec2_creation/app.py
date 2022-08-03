#!/usr/bin/env python3
#import os
#from dotenv import load_dotenv

# load our env file
#print ('Loading env file')
#load_dotenv()

import aws_cdk as cdk

from ec2_creation.ec2_creation_stack import Ec2CreationStack

#print ('Creating environment')
#cdk_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

#app = cdk.App()

app = cdk.App()
Ec2CreationStack
(
            app, 
            'Ec2CreationStack'
            #env=cdk_env 
)

# synthesize it
print ('Synthesizing stack')
app.synth()
