from fastapi import HTTPException
from resources.strings import (OWNER_DELETE_SUCCESS,
                               OWNER_DOES_NOT_EXIST_ERROR, OWNER_POST_SUCCESS,
                               OWNER_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_owner.models import MsOwner
from src.domain.master.ms_owner.schemas import (MessageResponse, OwnerCreate,
                                                OwnerUpdate)


# Get Owner Data
def get_owners(db: db_dependency):
    return db.query(MsOwner).filter(MsOwner.active == ACTIVE_DATA).order_by(MsOwner.description.asc()).all()


# Get Owner Data LIMIT
def get_owner_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsOwner).filter(MsOwner.active == ACTIVE_DATA).order_by(MsOwner.description.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Owner
def get_selected_owner(db:db_dependency, id: int):
    return db.query(MsOwner).filter(
        MsOwner.active == ACTIVE_DATA,
        MsOwner.id == id
    ).first()
    

# Update Owner
def update_owner(db:db_dependency, owner_request: OwnerUpdate, id:int):
    # Get Selected Data
    owner_model = get_selected_owner(db, id)
        
    # When data not found
    if owner_model is None:
        raise HTTPException(
            status_code=404, detail= OWNER_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    owner_model.description = owner_request.description,
    owner_model.active = owner_request.active,
        
    # Add data to database
    db.add(owner_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=OWNER_UPDATE_SUCCESS)
        
# Create Owner
def create_owner(db:db_dependency, owner_request: OwnerCreate):
        
    # Post Data request
    owner_model = MsOwner(**owner_request.dict())
        
    # Add new data to database
    db.add(owner_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=OWNER_POST_SUCCESS)

    
# Remove Owner
def remove_owner(db:db_dependency, owner_model: MsOwner):
    db.delete(owner_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=OWNER_DELETE_SUCCESS)
        
   
    
    
    
    
    
    