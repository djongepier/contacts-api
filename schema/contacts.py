"""
Pydantic schema.
"""
from typing import Optional
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
    phone_number: Optional[str]


class Contact(CreateContact):
    """
    The contact model.
    """
    contact_id: int

    class Config:
        orm_mode = True

