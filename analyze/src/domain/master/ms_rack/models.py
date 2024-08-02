from sqlalchemy import Column, String

from src.database import Base


class MsRack(Base):
    __tablename__ = 'ms_rack'

    code = Column(String, primary_key=True)
    description = Column(String)
    location_type = Column(String)
    alias = Column(String)
    acs_wh = Column(String)
    active = Column(String)
