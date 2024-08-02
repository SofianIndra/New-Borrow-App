from datetime import datetime

import pytz
from fastapi import HTTPException
from resources.strings import (TICKET_ANALYZE_START_DELETE_SUCCESS,
                               TICKET_ANALYZE_START_DOES_NOT_EXIST_ERROR,
                               TICKET_ANALYZE_START_POST_SUCCESS,
                               TICKET_ANALYZE_START_UPDATE_SUCCESS)
from src.config import LIMIT
from src.database import db_dependency
from src.domain.transaction.tx_ticket_analyze_start.models import \
    TxTicketAnalyzeStart
from src.domain.transaction.tx_ticket_analyze_start.schemas import (
    MessageResponse, TicketAnalyzeStartCreate, TicketAnalyzeStartUpdate)


# Get TxTicketAnalyzeStart Data
def get_ticket_analyze_start(db: db_dependency):
    return db.query(TxTicketAnalyzeStart).order_by(TxTicketAnalyzeStart.case_number.asc()).all()


# Get TxTicketAnalyzeStart Data LIMIT
def get_ticket_analyze_start_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(TxTicketAnalyzeStart).order_by(TxTicketAnalyzeStart.case_number.asc()).offset(offset).limit(LIMIT).all()


# Get Selected TxTicketAnalyzeStart
def get_selected_ticket_analyze_start(db:db_dependency, case_number: str, serial_number: str):
    return db.query(TxTicketAnalyzeStart).filter(
        TxTicketAnalyzeStart.case_number == case_number,
        TxTicketAnalyzeStart.serial_number == serial_number,
    ).first()
    
    
# Update TxTicketAnalyzeStart
def update_ticket_analyze_start(db:db_dependency, ticket_analyze_start_request: TicketAnalyzeStartUpdate, case_number:str):
    # Current Time in Jakarta
    current_time = datetime.now(pytz.timezone('Asia/Jakarta')).isoformat()
    
    # Serial Number
    serial_number = ticket_analyze_start_request.serial_number
    
    # Get Selected Data
    ticket_analyze_start_model = get_selected_ticket_analyze_start(db, case_number, serial_number)
        
    # When data not found
    if ticket_analyze_start_model is None:
        raise HTTPException(
            status_code=404, detail= TICKET_ANALYZE_START_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    ticket_analyze_start_model.serial_number = ticket_analyze_start_request.serial_number,
    ticket_analyze_start_model.engineer = ticket_analyze_start_request.engineer,
    ticket_analyze_start_model.item_code = ticket_analyze_start_request.item_code,
    ticket_analyze_start_model.item_name = ticket_analyze_start_request.item_name,
    ticket_analyze_start_model.person_name = ticket_analyze_start_request.person_name,
    ticket_analyze_start_model.person_email = ticket_analyze_start_request.person_email,
    ticket_analyze_start_model.person_mobile = ticket_analyze_start_request.person_mobile,
    ticket_analyze_start_model.accessories = ticket_analyze_start_request.accessories,
    ticket_analyze_start_model.problem = ticket_analyze_start_request.problem,
    ticket_analyze_start_model.warranty_status_id = ticket_analyze_start_request.warranty_status_id,
    ticket_analyze_start_model.warranty_status = ticket_analyze_start_request.warranty_status,
    ticket_analyze_start_model.updated_by = ticket_analyze_start_request.updated_by,
    ticket_analyze_start_model.updated_at = current_time,
        
    # Add data to database
    db.add(ticket_analyze_start_model)
    db.commit()
        
    # Update Response
    return MessageResponse(
        case_number=case_number,
        message=TICKET_ANALYZE_START_UPDATE_SUCCESS)


# Create TxTicketAnalyzeStart
def create_ticket_analyze_start(db:db_dependency, ticket_analyze_start_request: TicketAnalyzeStartCreate):
    # Current Time in Jakarta
    current_time = datetime.now(pytz.timezone('Asia/Jakarta')).isoformat()
        
    # Post Data request
    tx_ticket_analyze_start_model = TxTicketAnalyzeStart(**ticket_analyze_start_request.dict())
    tx_ticket_analyze_start_model.revision = 0
    tx_ticket_analyze_start_model.start_date = current_time
    tx_ticket_analyze_start_model.updated_at = current_time
        
    # Add new data to database
    db.add(tx_ticket_analyze_start_model)
    db.commit()
        
    # Post Response
    return MessageResponse(
        case_number=ticket_analyze_start_request.case_number, 
        message=TICKET_ANALYZE_START_POST_SUCCESS)
        
   
# Remove Ticket Analyze Start
def remove_ticket_analyze_start(db:db_dependency, ticket_analyze_start_model: TxTicketAnalyzeStart):
    db.delete(ticket_analyze_start_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=TICKET_ANALYZE_START_DELETE_SUCCESS)
        
   
    
    

    
    