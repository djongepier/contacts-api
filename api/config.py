# Environment configuration

import os
import json
from pathlib import Path

SECRETS_FILE = Path().resolve().parents[0] / ".secrets.json"


class Settings:
    """
    A class holding the secrets for the application.
    """
    database_uri: str
    api_key: str

    def __init__(self):
        for key, value in os.environ.items():
            if key == "CONTACTS_DATABASE_URI":
                self.database_uri = value
            if key == "CONTACTS_API_KEY":
                self.api_key = value
            else:
                with open(SECRETS_FILE, "r", encoding="utf-8") as secrets_file:
                    contents = json.load(secrets_file)
                    self.database_uri = contents["CONTACTS_DATABASE_URI"]
                    self.api_key = contents["CONTACTS_API_KEY"]

