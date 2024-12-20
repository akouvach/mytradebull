# Import the Secret Manager client library.
from google.cloud import secretmanager

# GCP project in which to store secrets in Secret Manager.
project_id = "conectun-b4c7d"

# ID of the secret to create.
secret_id = "ak_bull_api"

version_id = "1"

# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()

# # Build the parent name from the project.
# parent = f"projects/{project_id}"

# # Create the parent secret.
# secret = client.create_secret(
#     request={
#         "parent": parent,
#         "secret_id": secret_id,
#         "secret": {"replication": {"automatic": {}}},
#     }
# )

# # Add the secret version.
# version = client.add_secret_version(
#     request={"parent": secret.name, "payload": {"data": b"hello world!"}}
# )
# Construct the resource name of the secret version
name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

# Access the secret version.
response = client.access_secret_version(request={"name": name})

# Print the secret payload.
#
# WARNING: Do not print the secret in a production environment - this
# snippet is showing how to access the secret material.
payload = response.payload.data.decode("UTF-8")
print(f"Plaintext: {payload}")



