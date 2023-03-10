"""
Author: Daniel W. Jongepier
Purpose: Store contact information in a Postgresql database.
"""
from fastapi import FastAPI, Security, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from starlette.status import HTTP_403_FORBIDDEN

from db.postgres import SessionLocal, engine
from models.contact import ContactModel, Base
from schema.contacts import Contact, CreateContact
from config.settings import Settings


# Instantiate the settings
settings = Settings()

# Print the used settings to console:
# print(f"Database URI: {settings.database_uri} \n"
#       f"API-Key: {settings.api_key}")

# Set the access token en key name.
API_KEY = settings.api_key
API_KEY_NAME = "access_token"

# Define the APIKeyHeader to check for.
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Create the metadata and bind to database engine.
Base.metadata.create_all(bind=engine)

# Instantiate the application based on FastAPI.
app = FastAPI()


# Function to open and close the database connection on use.
def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


# Function to check if the ApiKey provided matches the key expected.
def key_auth(api_key_header: str = Security(api_key_header)):

    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


# Define the CRUDRouter.
router = SQLAlchemyCRUDRouter(
    schema=Contact,
    create_schema=CreateContact,
    db_model=ContactModel,
    db=get_db,
    prefix='contact',
    delete_all_route=False,
    dependencies=[Depends(key_auth)]
)

# Update the already instantiated FastAPI instance with the CRUDRouter.
app.include_router(router)
