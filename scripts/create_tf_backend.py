import sys
from client import get_storage_account_client
from config import STORAGE_ACCOUNT_NAME, RESOURCE_GROUP_NAME, CONTAINER_NAME

ALLOWED_ENVS = [
    "integration",
    "staging",
    "perf",
    "prod"
]

backend_file_content = """
storage_account_name = "{storage_account_name}"
container_name = "{container_name}"
resource_group_name = "{resource_group_name}"
key = "{environment}.elastic"
access_key = "{access_key}"
""".strip()


def create_backend_file(environment, arm_access_key):
    filename = f"{sys.path[0]}/../environments/{environment}/backend.conf"
    print(f"Creating terraform backend configuration at {filename}")
    file_content = backend_file_content.format(
        storage_account_name=STORAGE_ACCOUNT_NAME,
        container_name=CONTAINER_NAME,
        resource_group_name=RESOURCE_GROUP_NAME,
        environment=environment,
        access_key=arm_access_key
    )
    with open(filename, "w") as file:
        file.write(file_content)


def get_arm_access_key():
    print("Getting access key for tf state storage account")
    client = get_storage_account_client()
    keys = client.storage_accounts.list_keys(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME)
    return keys.keys[0].value


def run():
    print("Setting up local environment for Terraform")
    arm_access_key = get_arm_access_key()
    for environment in ALLOWED_ENVS:
        print(f"Setting up {environment} environment for terraform")
        create_backend_file(environment, arm_access_key)
    print("Done!")
