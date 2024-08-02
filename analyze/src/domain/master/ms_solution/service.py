from fastapi import HTTPException

from resources.strings import (SOLUTION_DELETE_SUCCESS,
                               SOLUTION_DOES_NOT_EXIST_ERROR,
                               SOLUTION_POST_SUCCESS, SOLUTION_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_solution.models import MsSolution
from src.domain.master.ms_solution.schemas import (SolutionCreate,
                                                   SolutionUpdate,
                                                   MessageResponse)


# Get Solution Data
def get_solution(db: db_dependency):
    return db.query(MsSolution).filter(MsSolution.active == ACTIVE_DATA).order_by(MsSolution.id.asc()).all()


# Get Solution Data LIMIT
def get_solution_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsSolution).filter(MsSolution.active == ACTIVE_DATA).order_by(MsSolution.id.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Solution
def get_selected_solution(db:db_dependency, id: int):
    return db.query(MsSolution).filter(
        MsSolution.active == ACTIVE_DATA,
        MsSolution.id == id
    ).first()
    

# Update Solution
def update_solution(db:db_dependency, solution_request: SolutionUpdate, id:int):
    # Get Selected Data
    ms_solution_model = get_selected_solution(db, id)
        
    # When data not found
    if ms_solution_model is None:
        raise HTTPException(
            status_code=404, detail= SOLUTION_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    ms_solution_model.main_solution = solution_request.main_solution,
    ms_solution_model.detail_solution = solution_request.detail_solution,
    ms_solution_model.active = solution_request.active,
        
    # Add data to database
    db.add(ms_solution_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=SOLUTION_UPDATE_SUCCESS)
        
# Create Solution
def create_solution(db:db_dependency, solution_request: SolutionCreate):
        
    # Post Data request
    ms_solution_model = MsSolution(**solution_request.dict())
        
    # Add new data to database
    db.add(ms_solution_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=SOLUTION_POST_SUCCESS)

    
# Remove Solution
def remove_solution(db:db_dependency, ms_solution_model: MsSolution):
    db.delete(ms_solution_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=SOLUTION_DELETE_SUCCESS)
        
   
    
    
    
    
    
    