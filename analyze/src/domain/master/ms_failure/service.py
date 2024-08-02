from fastapi import HTTPException

from resources.strings import (FAILURE_DELETE_SUCCESS,
                               FAILURE_DOES_NOT_EXIST_ERROR,
                               FAILURE_POST_SUCCESS, FAILURE_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_failure.models import MsFailure
from src.domain.master.ms_failure.schemas import (FailureCreate,
                                                   FailureUpdate,
                                                   MessageResponse)


# Get Failure Data
def get_failure(db: db_dependency):
    return db.query(MsFailure).filter(MsFailure.active == ACTIVE_DATA).order_by(MsFailure.id.asc()).all()


# Get Failure Data LIMIT
def get_failure_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsFailure).filter(MsFailure.active == ACTIVE_DATA).order_by(MsFailure.id.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Failure
def get_selected_failure(db:db_dependency, id: int):
    return db.query(MsFailure).filter(
        MsFailure.active == ACTIVE_DATA,
        MsFailure.id == id
    ).first()
    
    
# Get Selected Failure by vendor code
def get_failure_by_vendor_code(db:db_dependency, vendor_code: str):
    return db.query(MsFailure).filter(
        MsFailure.active == ACTIVE_DATA,
        MsFailure.vendor_code == vendor_code
    ).all()
    

# Update Failure
def update_failure(db:db_dependency, failure_request: FailureUpdate, id:int):
    # Get Selected Data
    ms_failure_model = get_selected_failure(db, id)
        
    # When data not found
    if ms_failure_model is None:
        raise HTTPException(
            status_code=404, detail= FAILURE_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    ms_failure_model.vendor_code = failure_request.vendor_code,
    ms_failure_model.main_failure = failure_request.main_failure,
    ms_failure_model.detail_failure = failure_request.detail_failure,
    ms_failure_model.active = failure_request.active,
    
    
    # Add data to database
    db.add(ms_failure_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=FAILURE_UPDATE_SUCCESS)
        
# Create Failure
def create_failure(db:db_dependency, failure_request: FailureCreate):
        
    # Post Data request
    ms_failure_model = MsFailure(**failure_request.dict())
        
    # Add new data to database
    db.add(ms_failure_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=FAILURE_POST_SUCCESS)

    
# Remove Failure
def remove_failure(db:db_dependency, ms_failure_model: MsFailure):
    db.delete(ms_failure_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=FAILURE_DELETE_SUCCESS)
        
   
    
    
    
    
    
    