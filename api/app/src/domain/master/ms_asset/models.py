from sqlalchemy import Column, Integer, String

from src.database import Base


class MsAsset(Base):
    __tablename__ = 'ms_asset'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    asset_type = Column(String)
    parent_id = Column(Integer)
    serial_number = Column(String)
    part_number = Column(String)
    branch_id = Column(Integer)
    branch = Column(String)
    asset_number = Column(String)
    category_id = Column(Integer)
    category = Column(String)
    description = Column(String)
    location_id = Column(Integer)
    location = Column(String)
    status_id = Column(Integer)
    status = Column(String)
    borrow_status = Column(String)
    owner_id = Column(Integer)
    owner = Column(String)
    rack = Column(String)
    remark = Column(String)
    active = Column(String)
    created_at = Column(String)
    created_by = Column(String)
    modified_at = Column(String)
    modified_by = Column(String)