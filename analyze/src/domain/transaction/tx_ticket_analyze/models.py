from sqlalchemy import Column, Integer, String

from src.database import Base


# Create TxTicketAnalyze Table
class TxTicketAnalyze(Base):
    __tablename__ = 'tx_ticket_analyze'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    case_number = Column(String, primary_key=True)
    serial_number = Column(String)
    revision = Column(Integer)
    ordinal = Column(Integer)
    action_date = Column(String)
    rack = Column(String)
    engineer = Column(String)
    service_action = Column(String)
    warranty_status_id = Column(Integer)
    warranty_status = Column(String)
    failure = Column(String)
    solution = Column(String)
    other_solution = Column(String)
    photo1_url = Column(String)
    photo2_url = Column(String)
    photo3_url = Column(String)
    video1_url = Column(String)
    remark = Column(String)
    is_cancel = Column(Integer)
    updated_by = Column(String)
    updated_at = Column(String)
    
    
    
    

