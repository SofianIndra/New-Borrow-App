from sqlalchemy import Column, Integer, String

from src.database import Base


class MsSolution(Base):
    __tablename__ = 'ms_solution'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    main_solution = Column(String)
    detail_solution = Column(String)
    active = Column(String)
 