from dotenv import load_dotenv
import os

load_dotenv()

ELASTIC_USERNAME = os.getenv("ELASTIC_USERNAME")
ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD")
ELASTIC_ENDPOINT = os.getenv("ELASTIC_ENDPOINT")
