# CSL Terraform Elastic
This repository contains Terraform code used to manage the CSL Cloud Elastisearch instance, as well as some Python scripts to aid with setting up elasticsearch.

## Requirements
- Terraform 0.13.0
- Azure CLI
- Python 3

## Setup
### Elastic API key
Before running any of the Terraform/Python commands within this repo, you'll need to generate an Elasticsearch API key. Instructions on how to do this can be found here: https://www.elastic.co/guide/en/cloud/current/ec-api-authentication.html

The scripts in this repo rely on the key being assigned to the environment variable `EC_API_KEY`.

### Backend
The script `scripts/create_tf_backend.py` must first be used to set up the Azure Terraform backend.

This script will create a `backend.conf` file within the various environment sub-directories. The backend configuration file contains the properties required to store/access the state file securely within Azure Blob storage. This should **NOT** be committed as it contains sensitive information.

### Terraform commands
#### Import
Importing into the Terraform infrastructure should only be done via the `import.sh` script. It only needs to be performed once - when a new Elasticsearch environment is created.

#### Init
Once the backend is created, `terraform init -backend-config=backend.conf` can be run against the desired environment (`cd environments/<environment name>`).

This will initialise Terraform using the newly created backend configuration file, which will use the remote state file in Azure blob storage.

#### Plan/Apply
`terraform plan` and `terraform apply` can then be used in the normal way to plan/apply changes to the infrastructure.

## Python scripts

The various supporting Python scripts are documented below. To run them, `main.py` should be used along with one or more of the following command line arguments:

- `tf_backend`
- `elastic_users`

### Requirements

Required packages for all of the scripts can be found in the `requirements.txt` and installed using `pip install -r requirements.txt`

- Azure mgmt storage: SDK for interacting with storage accounts in Azure
- Azure identity: SDK used to authenticate with Azure (CLI auth is used)
- Pyhton-dotenv: Reading .env files

### create_tf_backend.py

Requires the following environment variables:
- SUBSCRIPTION_ID: The subscription ID for the blob storage container
- RESOURCE_GROUP_NAME: The resource group for the blob storage container
- STORAGE_ACCOUNT_NAME: Blob storage account name
- CONTAINER_NAME: The blob storage container which has the elastic Terraform state files

The script will fetch the account key for the blob storage account and create the Terraform backend file using the other parameters.

The name of the state file will be inferred from the environment.

### create_elastic_users.py

Requires the following environment variables:
- ELASTIC_USERNAME: The username for the Elastic connection
- ELASTIC_PASSWORD: The password for the Elastic connection
- ELASTIC_ENDPOINT: The Elasticsearch endpoint

Running the script will create any users (along with their roles) that have been specified in the file. Right now only the `learning_catalogue` user is required.

**NOTE**: A random password will be generated for each user. The password will be printed in the shell that is used to run the Python script. The password **cannot** be viewed after it has been created, only changed, so make sure to write it down.