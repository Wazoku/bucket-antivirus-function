# Upside Travel, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import errno
import os

import boto3

AV_DEFINITION_S3_BUCKET = os.getenv("AV_DEFINITION_S3_BUCKET")
AV_DEFINITION_S3_PREFIX = os.getenv("AV_DEFINITION_S3_PREFIX", "clamav_defs")
AV_DEFINITION_PATH = os.getenv("AV_DEFINITION_PATH", "/tmp/clamav_defs")
AV_SCAN_START_SNS_ARN = os.getenv("AV_SCAN_START_SNS_ARN")
AV_SCAN_START_METADATA = os.getenv("AV_SCAN_START_METADATA", "av-scan-start")
AV_STATUS_CLEAN = os.getenv("AV_STATUS_CLEAN", "CLEAN")
AV_STATUS_INFECTED = os.getenv("AV_STATUS_INFECTED", "INFECTED")
AV_STATUS_METADATA = os.getenv("AV_STATUS_METADATA", "av-status")
AV_STATUS_SNS_ARN = os.getenv("AV_STATUS_SNS_ARN")
AV_TIMESTAMP_METADATA = os.getenv("AV_TIMESTAMP_METADATA", "av-timestamp")
CLAMAVLIB_PATH = os.getenv("CLAMAVLIB_PATH", "./bin")
CLAMSCAN_PATH = os.getenv("CLAMSCAN_PATH", "./bin/clamscan")
FRESHCLAM_PATH = os.getenv("FRESHCLAM_PATH", "./bin/freshclam")
S3_REGION_NAME = os.getenv("S3_REGION_NAME")
AV_DEFINITION_REGION = os.getenv("AV_DEFINITION_REGION","eu-west-1")
AV_PROCESS_ORIGINAL_VERSION_ONLY = os.getenv("AV_PROCESS_ORIGINAL_VERSION_ONLY", "False")

AV_FILE_CONTENTS = os.getenv("AV_FILE_CONTENTS", "Virus detected. Contact Wazoku support.")  # noqa
AV_DEFINITION_FILENAMES = ["main.cvd", "daily.cvd", "main.cld", "bytecode.cvd"]  # noqa

s3 = boto3.resource('s3',region_name=S3_REGION_NAME)
s3_client = boto3.client('s3',region_name=S3_REGION_NAME)
s3_client_eu = boto3.client('s3',region_name=AV_DEFINITION_REGION)

def create_dir(path):
    if not os.path.exists(path):
        try:
            print("Attempting to create directiory %s.\n" % path)
            os.makedirs(path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
