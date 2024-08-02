from fastapi import HTTPException

from resources.strings import (ENGINEER_DELETE_SUCCESS,
                               ENGINEER_DOES_NOT_EXIST_ERROR,
                               ENGINEER_POST_SUCCESS, ENGINEER_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_engineer.models import MsEngineer
from src.domain.master.ms_engineer.schemas import (EngineerCreate,
                                                   EngineerUpdate,
                                                   MessageResponse)


# Get Engineer Data
def get_engineers(db: db_dependency):
    return db.query(MsEngineer).filter(MsEngineer.active == ACTIVE_DATA).order_by(MsEngineer.name.asc()).all()


# Get Engineer Data LIMIT
def get_engineer_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsEngineer).filter(MsEngineer.active == ACTIVE_DATA).order_by(MsEngineer.name.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Engineer
def get_selected_engineer(db:db_dependency, code: str):
    return db.query(MsEngineer).filter(
        MsEngineer.active == ACTIVE_DATA,
        MsEngineer.code == code
    ).first()
    

# Update Engineer
def update_engineer(db:db_dependency, engineer_request: EngineerUpdate, code:str):
    # Get Selected Data
    ms_engineer_model = get_selected_engineer(db, code)
        
    # When data not found
    if ms_engineer_model is None:
        raise HTTPException(
            status_code=404, detail= ENGINEER_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    ms_engineer_model.code = engineer_request.code,
    ms_engineer_model.name = engineer_request.name,
    ms_engineer_model.active = engineer_request.active,
        
    # Add data to database
    db.add(ms_engineer_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=ENGINEER_UPDATE_SUCCESS)
        
# Create Engineer
def create_engineer(db:db_dependency, engineer_request: EngineerCreate):
        
    # Post Data request
    ms_engineer_model = MsEngineer(**engineer_request.dict())
        
    # Add new data to database
    db.add(ms_engineer_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=ENGINEER_POST_SUCCESS)

    
# Remove Engineer
def remove_engineer(db:db_dependency, ms_engineer_model: MsEngineer):
    db.delete(ms_engineer_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=ENGINEER_DELETE_SUCCESS)
        
   
    
    
    
    
    
    