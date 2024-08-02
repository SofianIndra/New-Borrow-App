from sqlalchemy import Column, Integer, String

from src.database import Base


class MsAction(Base):
    __tablename__ = 'ms_action'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    active = Column(String)