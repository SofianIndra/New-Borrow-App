from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel


# Create Ticket Analyze Body
class TicketAnalyzeCreate(BaseModel):
    case_number:str
    serial_number:str
    ordinal:int
    rack:str
    engineer:str
    service_action:str
    warranty_status_id:int
    warranty_status:str
    failure:str
    solution:str
    other_solution:Optional[str]
    remark:Optional[str]
    is_cancel:int
    updated_by:str
    
    
# Update Ticket Analyze Body
class TicketAnalyzeUpdate(BaseModel):
    serial_number:str
    action_date:str
    rack:str
    engineer:str
    service_action:str
    warranty_status_id:int
    warranty_status:str
    failure:str
    solution:str
    other_solution:str
    photo1_url:str
    photo2_url:str
    photo3_url:str
    video1_url:str
    remark:str
    is_cancel:int
    updated_by:str
    updated_at:str


# Delete Photo Body
class DeletePhoto(BaseModel):
    file_id:str
    url:str
    
    
# Delete Video Body
class DeleteVideo(BaseModel):
    file_id:str


# Photo Url
class FileUrl(BaseModel):
    id:Optional[str]
    url:Optional[str]


# Ticket Analyze Id Response
class TicketAnalyzeId(BaseModel):
    id: int
    photo: list[FileUrl]
    video: list[FileUrl]
    

# Upload File Success Response
class UploadSuccessResponse(BaseModel):
    url:str
    file_id:str

# Message Response
class MessageResponse(BaseModel):
    message:str
    