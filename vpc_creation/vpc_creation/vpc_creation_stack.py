from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ec2,
)


class VpcCreationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.vpc = aws_ec2.Vpc(self, 'demovpc',
            cidr = '192.168.50.0/24',
            max_azs = 2,
            enable_dns_hostnames = True,
            enable_dns_support = True, 
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    name = 'Public-Subent',
                    subnet_type = aws_ec2.SubnetType.PUBLIC,
                    cidr_mask = 26
                ),
                aws_ec2.SubnetConfiguration(
                    name = 'Private-Subnet',
                    #subnet_type = aws_ec2.SubnetType.PRIVATE_ISOLATED,
                    subnet_type = aws_ec2.SubnetType.PRIVATE_WITH_NAT,
                    cidr_mask = 26
                )
            ],
            nat_gateways = 1,

        )
