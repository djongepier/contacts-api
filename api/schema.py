# Pydantic schema

from pydantic import BaseModel


class CreateContact(BaseModel):
    """
    This model is used to create the contact.
    """
    lastname: str
    initials: str
    firstname: str
    street: str
    house_number: str
    postalcode: str
    residence: str


class Contact(CreateContact):
    """
    This defines the base model with all the fields.
    """
    contact_id: int

    class Config:
        orm_mode = True

