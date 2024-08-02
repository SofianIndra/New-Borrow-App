from sqlalchemy import Column, Integer, String

from src.database import Base


class MsOwner(Base):
    __tablename__ = 'ms_owner'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)
    active = Column(String)
    created_at = Column(String)
    created_by = Column(String)
    modified_at = Column(String)
    modified_by = Column(String)