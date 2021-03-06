#!/usr/bin/env python

# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# [START storage_copy_file_archived_generation]
from google.cloud import storage


def copy_file_archived_generation(
        bucket_name, blob_name, destination_bucket_name, destination_blob_name, generation
):
    """Copies a blob from one bucket to another with a new name with the same generation."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"
    # generation = 1579287380533984

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name, source_generation=generation
    )

    print(
        "Generation {} of the blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.generation,
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


# [END storage_copy_file_archived_generation]

if __name__ == "__main__":
    copy_file_archived_generation(
        bucket_name=sys.argv[1],
        blob_name=sys.argv[2],
        destination_bucket_name=sys.argv[3],
        destination_blob_name=sys.argv[4],
        generation=sys.argv[5]
    )
