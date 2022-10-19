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


current_dir := $(shell pwd)
container_dir := /opt/app
circleci := ${CIRCLECI}

all: archive

clean:
	rm -rf build
	mkdir build

archive: clean
	docker run --rm -ti \
		-v $(current_dir):$(container_dir) \
		--entrypoint "/bin/bash" \
		public.ecr.aws/lambda/python:3.9 \
		 -l -c 'cd $(container_dir) && ./build_lambda.sh'

