"""
Contact database model.

"""

from sqlalchemy import Column, Integer, String, Sequence

from db import Base


class ContactModel(Base):
    """
    Model defines the database structure.
    """
    __tablename__ = "contacts"

    contact_id = Column(Integer, Sequence("contact_id", start=1), primary_key=True, index=True)
    lastname = Column(String(254))
    initials = Column(String(20))
    firstname = Column(String(254))
    street = Column(String(254))
    house_number = Column(String(254))
    postalcode = Column(String(254))
    residence = Column(String(254))
