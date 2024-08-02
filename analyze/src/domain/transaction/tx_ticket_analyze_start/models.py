from sqlalchemy import Column, Integer, String

from src.database import Base

# Create TxTicketAnalyzeStart Table
class TxTicketAnalyzeStart(Base):
    __tablename__ = 'tx_ticket_analyze_start'
    
    id = Column(Integer,primary_key=True, index=True, autoincrement=True)
    case_number = Column(String)
    revision = Column(Integer)
    engineer  = Column(String)
    start_date = Column(String)
    ordinal = Column(Integer)
    serial_number = Column(String)
    item_code = Column(String)
    item_name = Column(String)
    person_name = Column(String)
    person_email = Column(String)
    person_mobile = Column(String)
    accessories = Column(String)
    problem = Column(String)
    warranty_status_id = Column(Integer)
    warranty_status = Column(String)
    updated_by = Column(String)
    updated_at = Column(String)
    
    

    
   
