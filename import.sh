#!/usr/bin/env bash
: '
This script only needs to be run when INITIALLY importing
an existing Elastic cloud instance into Terraform.
'
envs=("integration")
ENV=$1

if [[ " ${envs[*]} " =~ ${ENV} ]]; then
  cd "environments/${ENV}" || exit
  DEPLOY_ID=$(az elastic monitor show --name "csl-elastic-${ENV}" --resource-group "lpg${ENV}-elastic" --query 'properties.elasticProperties.elasticCloudDeployment.deploymentId' -o tsv)
  terraform init
  terraform import "ec_deployment.csl_course_db_${ENV}" "$DEPLOY_ID"
else
  echo "$ENV is not a valid environment"
  exit
fi
