from fastapi import HTTPException
from resources.strings import (STATUS_DELETE_SUCCESS,
                               STATUS_DOES_NOT_EXIST_ERROR, STATUS_POST_SUCCESS,
                               STATUS_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_status.models import MsStatus
from src.domain.master.ms_status.schemas import (MessageResponse, StatusCreate,
                                                StatusUpdate)


# Get Status Data
def get_status(db: db_dependency):
    return db.query(MsStatus).filter(MsStatus.active == ACTIVE_DATA).order_by(MsStatus.description.asc()).all()


# Get Status Data LIMIT
def get_status_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsStatus).filter(MsStatus.active == ACTIVE_DATA).order_by(MsStatus.description.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Status
def get_selected_status(db:db_dependency, id: int):
    return db.query(MsStatus).filter(
        MsStatus.active == ACTIVE_DATA,
        MsStatus.id == id
    ).first()
    

# Update Status
def update_status(db:db_dependency, status_request: StatusUpdate, id:int):
    # Get Selected Data
    status_model = get_selected_status(db, id)
        
    # When data not found
    if status_model is None:
        raise HTTPException(
            status_code=404, detail= STATUS_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    status_model.description = status_request.description,
    status_model.active = status_request.active,
        
    # Add data to database
    db.add(status_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=STATUS_UPDATE_SUCCESS)
        
# Create Status
def create_status(db:db_dependency, status_request: StatusCreate):
        
    # Post Data request
    status_model = MsStatus(**status_request.dict())
        
    # Add new data to database
    db.add(status_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=STATUS_POST_SUCCESS)

    
# Remove Status
def remove_status(db:db_dependency, status_model: MsStatus):
    db.delete(status_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=STATUS_DELETE_SUCCESS)
        
   
    
    
    
    
    
    