"""
Author: Daniel W. Jongepier
Purpose: Store contact information in a database.
"""

from db import SessionLocal, engine
from models import ContactModel, Base
from schema import Contact, CreateContact
from config import Settings

from fastapi import FastAPI, Security, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from starlette.status import HTTP_403_FORBIDDEN

# Instantiate the settings
settings = Settings()

# Print the used settings to console:
print(f"Database URI: {settings.database_uri} \n"
      f"API-Key: {settings.api_key}")

API_KEY = settings.api_key
API_KEY_NAME = "access_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def key_auth(api_key_header: str = Security(api_key_header)):

    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


router = SQLAlchemyCRUDRouter(
    schema=Contact,
    create_schema=CreateContact,
    db_model=ContactModel,
    db=get_db,
    prefix='contact',
    delete_all_route=False,
    dependencies=[Depends(key_auth)]
)

app.include_router(router)
