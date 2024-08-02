from fastapi import HTTPException
from resources.strings import (LOCATION_DELETE_SUCCESS,
                               LOCATION_DOES_NOT_EXIST_ERROR,
                               LOCATION_POST_SUCCESS, LOCATION_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_location.models import MsLocation
from src.domain.master.ms_location.schemas import (LocationCreate,
                                                   LocationUpdate,
                                                   MessageResponse)


# Get Location Data
def get_locations(db: db_dependency):
    return db.query(MsLocation).filter(MsLocation.active == ACTIVE_DATA).order_by(MsLocation.description.asc()).all()


# Get Location Data LIMIT
def get_location_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsLocation).filter(MsLocation.active == ACTIVE_DATA).order_by(MsLocation.description.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Location
def get_selected_location(db:db_dependency, id: int):
    return db.query(MsLocation).filter(
        MsLocation.active == ACTIVE_DATA,
        MsLocation.id == id
    ).first()
    

# Update Location
def update_location(db:db_dependency, location_request: LocationUpdate, id:int):
    # Get Selected Data
    location_model = get_selected_location(db, id)
        
    # When data not found
    if location_model is None:
        raise HTTPException(
            status_code=404, detail= LOCATION_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    location_model.description = location_request.description,
    location_model.active = location_request.active,
        
    # Add data to database
    db.add(location_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=LOCATION_UPDATE_SUCCESS)
        
# Create Location
def create_location(db:db_dependency, location_request: LocationCreate):
        
    # Post Data request
    location_model = MsLocation(**location_request.dict())
        
    # Add new data to database
    db.add(location_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=LOCATION_POST_SUCCESS)

    
# Remove Location
def remove_location(db:db_dependency, location_model: MsLocation):
    db.delete(location_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=LOCATION_DELETE_SUCCESS)
        
   
    
    
    
    
    
    