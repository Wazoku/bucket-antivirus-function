#Sample file which can be used for debugging lambda from linux commandline

import os

os.environ['S3_REGION_NAME']='me-central-1'
os.environ['AV_DEFINITION_S3_BUCKET']='virus-definitions'
os.environ['AV_FILE_CONTENTS']='A virus was detected in this file. Contact Wazoku support for further help.'
os.environ['AV_DEFINITION_REGION']='eu-west-1'
from scan import lambda_handler

lambda_handler(event={'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', ...},
               
context={'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'me-central-1',...}}}]})
