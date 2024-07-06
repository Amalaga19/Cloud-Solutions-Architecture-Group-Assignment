#!/usr/bin/env python3
import os

import aws_cdk as cdk

from csa_group_assignment.csa_group import CSAGroupStack


app = cdk.App()
CSAGroupStack(app, "CSAGroupStack",
    
    )

app.synth()
