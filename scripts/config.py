from dotenv import load_dotenv
import os

load_dotenv()

SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")

RESOURCE_GROUP_NAME = os.getenv("RESOURCE_GROUP_NAME")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")

ELASTIC_USERNAME = os.getenv("ELASTIC_USERNAME")
ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD")
ELASTIC_ENDPOINT = os.getenv("ELASTIC_ENDPOINT")