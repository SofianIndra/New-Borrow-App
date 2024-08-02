from typing import List

from pydantic import BaseModel, Field


# Create Ticket Analyze Start
class TicketAnalyzeStartCreate(BaseModel):
    case_number: str 
    engineer : str 
    ordinal : int 
    serial_number: str
    item_code: str 
    item_name: str 
    person_name: str 
    person_email: str 
    person_mobile: str 
    accessories: str 
    problem: str 
    warranty_status_id: int 
    warranty_status: str 
    updated_by: str 
    
    
# Update Ticket Analyze Start 
class TicketAnalyzeStartUpdate(BaseModel):
    engineer : str 
    serial_number: str
    item_code: str 
    item_name: str 
    person_name: str 
    person_email: str 
    person_mobile: str 
    accessories: str 
    problem: str 
    warranty_status_id: int 
    warranty_status: str 
    updated_by: str 


# Message Response
class MessageResponse(BaseModel):
    case_number:str
    message:str