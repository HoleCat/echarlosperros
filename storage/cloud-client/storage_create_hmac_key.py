#!/usr/bin/env python

# Copyright 2019 Google Inc. All Rights Reserved.
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

# [START storage_create_hmac_key]
from google.cloud import storage


def create_key(project_id, service_account_email):
    """
    Create a new HMAC key using the given project and service account.
    """
    # project_id = 'Your Google Cloud project ID'
    # service_account_email = 'Service account used to generate HMAC key'

    storage_client = storage.Client(project=project_id)

    hmac_key, secret = storage_client.create_hmac_key(
        service_account_email=service_account_email, project_id=project_id
    )

    print("The base64 encoded secret is {}".format(secret))
    print("Do not miss that secret, there is no API to recover it.")
    print("The HMAC key metadata is:")
    print("Service Account Email: {}".format(hmac_key.service_account_email))
    print("Key ID: {}".format(hmac_key.id))
    print("Access ID: {}".format(hmac_key.access_id))
    print("Project ID: {}".format(hmac_key.project))
    print("State: {}".format(hmac_key.state))
    print("Created At: {}".format(hmac_key.time_created))
    print("Updated At: {}".format(hmac_key.updated))
    print("Etag: {}".format(hmac_key.etag))
    return hmac_key


# [END storage_create_hmac_key]

if __name__ == "__main__":
    create_key(project_id=sys.argv[1], service_account_email=sys.argv[2])
