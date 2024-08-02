from sqlalchemy import Column, String

from src.database import Base


class MsEngineer(Base):
    __tablename__ = 'ms_engineer'

    code = Column(String, primary_key=True)
    name = Column(String)
    active = Column(String)
