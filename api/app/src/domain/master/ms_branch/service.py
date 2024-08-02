from fastapi import HTTPException
from resources.strings import (BRANCH_DELETE_SUCCESS,
                               BRANCH_DOES_NOT_EXIST_ERROR, BRANCH_POST_SUCCESS,
                               BRANCH_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_branch.models import MsBranch
from src.domain.master.ms_branch.schemas import (MessageResponse, BranchCreate,
                                                BranchUpdate)


# Get Branch Data
def get_branch(db: db_dependency):
    return db.query(MsBranch).filter(MsBranch.active == ACTIVE_DATA).order_by(MsBranch.description.asc()).all()


# Get Branch Data LIMIT
def get_branch_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsBranch).filter(MsBranch.active == ACTIVE_DATA).order_by(MsBranch.description.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Branch
def get_selected_branch(db:db_dependency, id: int):
    return db.query(MsBranch).filter(
        MsBranch.active == ACTIVE_DATA,
        MsBranch.id == id
    ).first()
    

# Update Branch
def update_branch(db:db_dependency, branch_request: BranchUpdate, id:int):
    # Get Selected Data
    status_model = get_selected_branch(db, id)
        
    # When data not found
    if status_model is None:
        raise HTTPException(
            status_code=404, detail= BRANCH_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    status_model.description = branch_request.description,
    status_model.active = branch_request.active,
        
    # Add data to database
    db.add(status_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=BRANCH_UPDATE_SUCCESS)
        
# Create Branch
def create_branch(db:db_dependency, branch_request: BranchCreate):
        
    # Post Data request
    status_model = MsBranch(**branch_request.dict())
        
    # Add new data to database
    db.add(status_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=BRANCH_POST_SUCCESS)

    
# Remove Branch
def remove_branch(db:db_dependency, status_model: MsBranch):
    db.delete(status_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=BRANCH_DELETE_SUCCESS)
        
   
    
    
    
    
    
    