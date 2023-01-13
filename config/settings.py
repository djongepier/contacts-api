"""
Environment configuration
"""

import os
import json
from pathlib import Path

SECRETS_FILE = Path().resolve() / ".secrets.json"


class Settings:
    """
    A class holding the secrets for the application.
    """
    database_uri: str
    api_key: str
    __database_host: str
    __database_port: str
    __database_db: str
    __database_user: str
    __database_password: str

    def __init__(self):
        if "CONTACTS_API_KEY" in os.environ:
            for key, value in os.environ.items():
                if key == "CONTACTS_API_KEY":
                    self.api_key = value
                if key == "CONTACTS_DATABASE_HOST":
                    self.__database_host = value
                if key == "CONTACTS_DATABASE_PORT":
                    self.__database_port = value
                if key == "CONTACTS_DATABASE_DB":
                    self.__database_db = value
                if key == "CONTACTS_DATABASE_USER":
                    self.__database_user = value
                if key == "CONTACTS_DATABASE_PASSWORD":
                    self.__database_password = value
        else:
            with open(SECRETS_FILE, "r", encoding="utf-8") as secrets_file:
                contents = json.load(secrets_file)
                self.api_key = contents["contacts_api_key"]
                self.__database_host = contents["contacts_database_host"]
                self.__database_port = contents["contacts_database_port"]
                self.__database_db = contents["contacts_database_db"]
                self.__database_user = contents["contacts_database_user"]
                self.__database_password = contents["contacts_database_password"]

    def get_database_uri(self):
        return f"postgresql+psycopg2://{self.__database_user}:{self.__database_password}" \
               f"@{self.__database_host}:{self.__database_port}/{self.__database_db}"
