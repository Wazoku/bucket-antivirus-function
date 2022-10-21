#!/usr/bin/env bash

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


set -e

yum update -y
yum install -y cpio zip git json-c
pip install --no-cache-dir virtualenv
virtualenv /tmp/env
. /tmp/env/bin/activate
pip install --no-cache-dir -r requirements.txt

git config --global --add safe.directory /opt/app
lambda_output_file=/opt/app/build/lambda_$(git rev-parse --short HEAD).zip

pushd /tmp
yum install -y clamav-server \
    clamav-data \
    clamav-update \
    clamav-filesystem \
    clamav \
    clamav-devel \
    clamav-lib
popd
mkdir -p /tmp/bin
cp /usr/bin/clamscan /usr/bin/freshclam /tmp/bin/.
cp  -v /usr/lib64/libssl3.so  /tmp/bin/
ldd /usr/bin/clamscan /usr/bin/freshclam | grep "\/.*\.so[^ ]*" -o | grep -v -e crypto -e libssl\. -e keyutils -e libpcre -e libc.so -e libresolv -e libstdc++ -e libm.so -e libicu -e ld-linux -e gcc  -e libdl  -e selinux -e krb5 -e com_err   | xargs -I{} cp {} /tmp/bin/.
echo "DatabaseMirror database.clamav.net" > /tmp/bin/freshclam.conf

zip -r9 $lambda_output_file *.py
cd /tmp/
zip -r9 $lambda_output_file bin
cd /tmp/env/lib/python3.9/site-packages
zip -r9 $lambda_output_file *
