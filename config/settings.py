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
    _database_host: str
    _database_port: str
    _database_db: str
    _database_user: str
    _database_password: str

    def __init__(self):
        for key, value in os.environ.items():
            if key == "CONTACTS_API_KEY":
                self.api_key = value
            if key == "CONTACTS_DATABASE_HOST":
                self._database_host = value
            if key == "CONTACTS_DATABASE_PORT":
                self._database_port = value
            if key == "CONTACTS_DATABASE_DB":
                self._database_db = value
            if key == "CONTACTS_DATABASE_USER":
                self._database_user = value
            if key == "CONTACTS_DATABASE_PASSWORD":
                self._database_password = value
            else:
                with open(SECRETS_FILE, "r", encoding="utf-8") as secrets_file:
                    contents = json.load(secrets_file)
                    self.api_key = contents["contacts_api_key"]
                    self._database_host = contents["contacts_database_host"]
                    self._database_port = contents["contacts_database_port"]
                    self._database_db = contents["contacts_database_db"]
                    self._database_user = contents["contacts_database_user"]
                    self._database_password = contents["contacts_database_password"]

    def get_database_uri(self):
        return f"postgresql+psycopg2://{self._database_user}:{self._database_password}" \
               f"@{self._database_host}:{self._database_port}/{self._database_db}"
