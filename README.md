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

### key.sh
This file contains an Env variable definition for `ARM_ACCESS_KEY`. This variable is required to authenticate against the blob storage container for the state storage. Without it, Terraform cannot read/write the state file and any `terraform` commands will fail.

### Terraform commands
#### Import
Importing into the Terraform infrastructure should only be done via the `import.sh` script. It only needs to be performed once - when a new Elasticsearch environment is created.

#### Init
Once the backend is created, `terraform init` can be run against the desired environment (`cd environments/<environment name>`).

This will initialise Terraform with the remote state file in Azure blob storage.

#### Plan/Apply
`terraform plan` and `terraform apply` can then be used in the normal way to plan/apply changes to the infrastructure.

## Python scripts

The various supporting Python scripts are documented below. To run them, `main.py` should be used along with one or more of the following command line arguments:

- `elastic_users`

### Requirements

Required packages for all of the scripts can be found in the `requirements.txt` and installed using `pip install -r requirements.txt`

- Pyhton-dotenv: Reading .env files

### create_elastic_users.py

Requires the following environment variables:
- ELASTIC_USERNAME: The username for the Elastic connection
- ELASTIC_PASSWORD: The password for the Elastic connection
- ELASTIC_ENDPOINT: The Elasticsearch endpoint

Running the script will create any users (along with their roles) that have been specified in the file. Right now only the `learning_catalogue` user is required.

**NOTE**: A random password will be generated for each user. The password will be printed in the shell that is used to run the Python script. The password **cannot** be viewed after it has been created, only changed, so make sure to write it down.
