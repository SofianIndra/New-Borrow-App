from sqlalchemy import Column, Integer, String

from src.database import Base


class MsFailure(Base):
    __tablename__ = 'ms_failure'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    vendor_code = Column(String)
    main_failure = Column(String)
    detail_failure = Column(String)
    active = Column(String)
 