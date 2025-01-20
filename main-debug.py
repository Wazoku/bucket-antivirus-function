
import os

os.environ['S3_REGION_NAME']='me-central-1'
os.environ['AV_DEFINITION_S3_BUCKET']='virus-definitions'
os.environ['AV_FILE_CONTENTS']='A virus was detected in this file. Contact Wazoku support for further help.'
os.environ['AV_DEFINITION_REGION']='eu-west-1'
from scan import lambda_handler

lambda_handler(event={'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'me-central-1', 'eventTime': '2025-01-17T11:54:30.003Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDA2UU4PPBCPKLPXDBAW'}, 'requestParameters': {'sourceIPAddress': '60.243.92.2'}, 'responseElements': {'x-amz-request-id': 'BNK5AH9DZW0QB5DW', 'x-amz-id-2': 'tpS5PYRPG+DlZHxWGlz1SSLVaDRdiH3hR3d9v3O22IX50/vXm07hqk1XRtIaSCyKaHmJjzrtuslCjrXEdnTSGc0xfnSGgsVy'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '563c5c86-6ad3-4759-968e-849581a67265', 'bucket': {'name': 'wazoku-clients-me', 'ownerIdentity': {'principalId': 'A3UWLTWWKOPJ57'}, 'arn': 'arn:aws:s3:::wazoku-clients-me'}, 'object': {'key': 'bhasker-zaj.wazoku.com/a.txt', 'size': 474, 'eTag': 'c7b6f6dcfff6bd8bba331b4d254c1686', 'sequencer': '00678A44F5CB111BCF'}}}]},
               
context={'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'me-central-1', 'eventTime': '2025-01-17T11:54:30.003Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDA2UU4PPBCPKLPXDBAW'}, 'requestParameters': {'sourceIPAddress': '60.243.92.2'}, 'responseElements': {'x-amz-request-id': 'BNK5AH9DZW0QB5DW', 'x-amz-id-2': 'tpS5PYRPG+DlZHxWGlz1SSLVaDRdiH3hR3d9v3O22IX50/vXm07hqk1XRtIaSCyKaHmJjzrtuslCjrXEdnTSGc0xfnSGgsVy'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '563c5c86-6ad3-4759-968e-849581a67265', 'bucket': {'name': 'wazoku-clients-me', 'ownerIdentity': {'principalId': 'A3UWLTWWKOPJ57'}, 'arn': 'arn:aws:s3:::wazoku-clients-me'}, 'object': {'key': 'bhasker-zaj.wazoku.com/a.txt', 'size': 474, 'eTag': 'c7b6f6dcfff6bd8bba331b4d254c1686', 'sequencer': '00678A44F5CB111BCF'}}}]})
