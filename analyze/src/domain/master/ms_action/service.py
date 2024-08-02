from fastapi import HTTPException

from resources.strings import (ACTION_DELETE_SUCCESS,
                               ACTION_DOES_NOT_EXIST_ERROR,
                               ACTION_POST_SUCCESS, ACTION_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_action.models import MsAction
from src.domain.master.ms_action.schemas import (ActionCreate, ActionUpdate,
                                                 MessageResponse)


# Get Action Data
def get_action(db: db_dependency):
    return db.query(MsAction).filter(MsAction.active == ACTIVE_DATA).order_by(MsAction.name.asc()).all()


# Get Action Data LIMIT
def get_action_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsAction).filter(MsAction.active == ACTIVE_DATA).order_by(MsAction.name.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Action
def get_selected_action(db:db_dependency, id: int):
    return db.query(MsAction).filter(
        MsAction.id == id,
        MsAction.active == ACTIVE_DATA,
    ).first()
    

# Update Action
def update_action(db:db_dependency, action_request: ActionUpdate, id:int):
    # Get Selected Data
    ms_action_model = get_selected_action(db, id)
        
    # When data not found
    if ms_action_model is None:
        raise HTTPException(
            status_id=404, detail= ACTION_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    ms_action_model.name = action_request.name,
    ms_action_model.active = action_request.active,
        
    # Add data to database
    db.add(ms_action_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=ACTION_UPDATE_SUCCESS)
        
# Create Action
def create_action(db:db_dependency, action_request: ActionCreate):
        
    # Post Data request
    ms_action_model = MsAction(**action_request.dict())
        
    # Add new data to database
    db.add(ms_action_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=ACTION_POST_SUCCESS)
    
    
# Remove Action
def remove_action(db:db_dependency, ms_action_model: MsAction):
    db.delete(ms_action_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=ACTION_DELETE_SUCCESS)
        
   
    
    
    
    
    
    