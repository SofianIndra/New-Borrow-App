from datetime import datetime
import os
import pytz
from fastapi import HTTPException
from resources.strings import (TICKET_ANALYZE_DELETE_SUCCESS,
                               TICKET_ANALYZE_DOES_NOT_EXIST_ERROR,
                               TICKET_ANALYZE_POST_SUCCESS,
                               TICKET_ANALYZE_UPDATE_SUCCESS)
from src.config import LIMIT
from src.database import db_dependency
from src.domain.transaction.tx_ticket_analyze.models import TxTicketAnalyze
from src.domain.transaction.tx_ticket_analyze.schemas import (
    MessageResponse, TicketAnalyzeCreate, TicketAnalyzeId, TicketAnalyzeUpdate,
    )
from googleapiclient.discovery import build
from google.oauth2 import service_account


# Get TxTicketAnalyze Data
def get_ticket_analyze(db: db_dependency):
    return db.query(TxTicketAnalyze).order_by(TxTicketAnalyze.case_number.asc()).all()


# Get TxTicketAnalyze Data LIMIT
def get_ticket_analyze_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(TxTicketAnalyze).order_by(TxTicketAnalyze.case_number.asc()).offset(offset).limit(LIMIT).all()


# Get Selected TxTicketAnalyze
def get_selected_ticket_analyze(db:db_dependency, case_number: str, serial_number: str):
    return db.query(TxTicketAnalyze).filter(
        TxTicketAnalyze.case_number == case_number,
        TxTicketAnalyze.serial_number == serial_number,
    ).first()
    
    
# Get TxTicketAnalyze by id
def get_ticket_analyze_by_id(db:db_dependency, id:int):
    return db.query(TxTicketAnalyze).filter(
        TxTicketAnalyze.id == id,
    ).first()
    
    
# Get TxTicketAnalyze by photo1_url
def get_ticket_analyze_by_photo1(db:db_dependency,id:int, photo1_url:str):
    return db.query(TxTicketAnalyze).filter(
        TxTicketAnalyze.id == id,
        TxTicketAnalyze.photo1_url == photo1_url,
    ).first()
    
    
# Get TxTicketAnalyze by photo2_url
def get_ticket_analyze_by_photo2(db:db_dependency,id:int, photo2_url:str):
    return db.query(TxTicketAnalyze).filter(
        TxTicketAnalyze.id == id,
        TxTicketAnalyze.photo2_url == photo2_url,
    ).first()
    
    
# Get TxTicketAnalyze by photo3_url
def get_ticket_analyze_by_photo3(db:db_dependency,id:int, photo3_url:str):
    return db.query(TxTicketAnalyze).filter(
        TxTicketAnalyze.id == id,
        TxTicketAnalyze.photo3_url == photo3_url,
    ).first()
        
    
# Update TxTicketAnalyze
def update_ticket_analyze(db:db_dependency, ticket_analyze_request: TicketAnalyzeUpdate, case_number:str):
    # Current Time in Jakarta
    current_time = datetime.now(pytz.timezone('Asia/Jakarta')).isoformat()
    
    # Serial Number
    serial_number = ticket_analyze_request.serial_number
    
    # Get Selected Data
    ticket_analyze_model = get_selected_ticket_analyze(db, case_number, serial_number)
        
    # When data not found
    if ticket_analyze_model is None:
        raise HTTPException(
            status_code=404, detail= TICKET_ANALYZE_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    ticket_analyze_model.serial_number = ticket_analyze_request.serial_number,
    ticket_analyze_model.action_date = ticket_analyze_request.action_date,
    ticket_analyze_model.rack = ticket_analyze_request.rack,
    ticket_analyze_model.engineer = ticket_analyze_request.engineer,
    ticket_analyze_model.service_action = ticket_analyze_request.service_action,
    ticket_analyze_model.warranty_status_id = ticket_analyze_request.warranty_status_id,
    ticket_analyze_model.warranty_status = ticket_analyze_request.warranty_status,
    ticket_analyze_model.failure = ticket_analyze_request.failure,
    ticket_analyze_model.solution = ticket_analyze_request.solution,
    ticket_analyze_model.other_solution = ticket_analyze_request.other_solution,
    ticket_analyze_model.photo1_url = ticket_analyze_request.photo1_url,
    ticket_analyze_model.photo2_url = ticket_analyze_request.photo2_url,
    ticket_analyze_model.photo3_url = ticket_analyze_request.photo3_url,
    ticket_analyze_model.video1_url = ticket_analyze_request.video1_url,
    ticket_analyze_model.remark = ticket_analyze_request.remark,
    ticket_analyze_model.is_cancel = ticket_analyze_request.is_cancel,
    ticket_analyze_model.updated_by = ticket_analyze_request.updated_by,
    ticket_analyze_model.updated_at = current_time
        
    # Add data to database
    db.add(ticket_analyze_model)
    db.commit()
        
    # Update Response
    return MessageResponse(
        message=TICKET_ANALYZE_UPDATE_SUCCESS)


# Create TxTicketAnalyze
def create_ticket_analyze(db:db_dependency, ticket_analyze_request: TicketAnalyzeCreate):
    # Current Time in Jakarta
    current_time = datetime.now(pytz.timezone('Asia/Jakarta')).isoformat()
    
    # Post Data request
    tx_ticket_analyze = TxTicketAnalyze(**ticket_analyze_request.dict())
    tx_ticket_analyze.action_date = current_time,
    tx_ticket_analyze.updated_at = current_time,
    tx_ticket_analyze.revision = 0
        
    # Add new data to database
    db.add(tx_ticket_analyze)
    db.commit()
        
    # Post Response
    return TicketAnalyzeId(
        id=tx_ticket_analyze.id
    )
    
    
# Update Photo Url
def update_photo_url(db:db_dependency, photo_url:str, ticket_analyze_id:int):
    # Get Ticket Analyze Data
    ticket_analyze_model = get_ticket_analyze_by_id(db,ticket_analyze_id)
    
    # When data not found
    if ticket_analyze_model is None:
        raise HTTPException(
            status_code=404, detail= TICKET_ANALYZE_DOES_NOT_EXIST_ERROR)
    
    # Update Photo Url
    if ticket_analyze_model.photo1_url == None:
        ticket_analyze_model.photo1_url = photo_url
    elif ticket_analyze_model.photo2_url == None:
        ticket_analyze_model.photo2_url = photo_url
    else:
        ticket_analyze_model.photo3_url = photo_url
        
    # Add new data to database
    db.add(ticket_analyze_model)
    db.commit()
        
    # Update Response
    return MessageResponse(
        message=TICKET_ANALYZE_UPDATE_SUCCESS)
    
    
# Update Video Url
def update_video_url(db:db_dependency, video_url:str, ticket_analyze_id:int):
    # Get Ticket Analyze Data
    ticket_analyze_model = get_ticket_analyze_by_id(db,ticket_analyze_id)
    
    # When data not found
    if ticket_analyze_model is None:
        raise HTTPException(
            status_code=404, detail= TICKET_ANALYZE_DOES_NOT_EXIST_ERROR)
    
    # Update Video Url
    ticket_analyze_model.video1_url = video_url
        
    # Add new data to database
    db.add(ticket_analyze_model)
    db.commit()
        
    # Update Response
    return MessageResponse(
        message=TICKET_ANALYZE_UPDATE_SUCCESS)
        
   
# Remove Ticket Analyze 
def remove_ticket_analyze(db:db_dependency, ticket_analyze_model: TxTicketAnalyze):
    db.delete(ticket_analyze_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=TICKET_ANALYZE_DELETE_SUCCESS)
        
file_name = 'service_account.json'
absolute_path = os.path.abspath(file_name)

# Google API
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = absolute_path
PARENT_FOLDER_ID = '10eDesEoxd-k5w0IEPsBg-NdGBWbn4B0D'

# Google Authenticate
def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
    return creds


# Function to set permissions for a file
def set_file_permission(file_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    permission = {
        'type': 'anyone',
        'role': 'reader',
    }
    service.permissions().create(fileId=file_id, body=permission).execute()


# Upload Image or Video
def upload_file(file_name:str, file_path:str):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {
        'name':file_name,
        'parents':[PARENT_FOLDER_ID]
    }
    
    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
    
    return file
   
   
# Delete Image or video
def delete_file(file_id:str):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    try:
        # Delete the file from Google Drive
        service.files().delete(fileId=file_id).execute()
        return {"message": "File deleted successfully"}
    except Exception as e:
        # Handle exceptions such as file not found
        raise HTTPException(status_code=404, detail=f"Error deleting file: {str(e)}")
    

    
    