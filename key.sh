# TODO: Migrate this to a keyvault when TF changes are made
ACCOUNT_KEY=$(az storage account keys list --resource-group lpgterraform --account-name lpgterraformsecure --query '[0].value' -o tsv)
export ARM_ACCESS_KEY=$ACCOUNT_KEY
