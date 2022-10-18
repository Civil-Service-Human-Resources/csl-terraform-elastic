from azure.mgmt.storage import StorageManagementClient

import config
import credentials


def get_storage_account_client():
    subscription_id = config.SUBSCRIPTION_ID
    credential = credentials.CLI_CREDENTIALS
    return StorageManagementClient(credential, subscription_id)
