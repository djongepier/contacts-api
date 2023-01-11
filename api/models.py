# Contact Model

from sqlalchemy import Column, Integer, String, Sequence

from api.db import Base


class Contact(Base):
    """
    Model defines the database structure.
    """
    __tablename__ = "contacts"

    contact_id = Column(Integer, Sequence("contact_id", start=1), primary_key=True, index=True)
    lastname = Column(String(254))
    initials = Column(String(20))
    firstname = Column(String(254))


