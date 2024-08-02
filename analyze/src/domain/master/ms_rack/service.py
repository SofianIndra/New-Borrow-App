from fastapi import HTTPException

from resources.strings import (RACK_DELETE_SUCCESS,
                               RACK_DOES_NOT_EXIST_ERROR,
                               RACK_POST_SUCCESS, RACK_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_rack.models import MsRack
from src.domain.master.ms_rack.schemas import (RackCreate,
                                                   RackUpdate,
                                                   MessageResponse)


# Get Rack Data
def get_racks(db: db_dependency):
    return db.query(MsRack).filter(MsRack.active == ACTIVE_DATA).order_by(MsRack.code.asc()).all()


# Get Rack Data LIMIT
def get_rack_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsRack).filter(MsRack.active == ACTIVE_DATA).order_by(MsRack.code.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Rack
def get_selected_rack(db:db_dependency, code: str):
    return db.query(MsRack).filter(
        MsRack.active == ACTIVE_DATA,
        MsRack.code == code
    ).first()
    
    
# Get Selected Rack by location type & ACS WH
def get_rack_by_location_type_and_acswh(db:db_dependency, location_type: str, acs_wh: str):
    return db.query(MsRack).filter(
        MsRack.active == ACTIVE_DATA,
        MsRack.location_type == location_type,
        MsRack.acs_wh == acs_wh,
    ).all()
    

# Update Rack
def update_rack(db:db_dependency, rack_request: RackUpdate, code:str):
    # Get Selected Data
    ms_rack_model = get_selected_rack(db, code)
        
    # When data not found
    if ms_rack_model is None:
        raise HTTPException(
            status_code=404, detail= RACK_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    ms_rack_model.code = rack_request.code,
    ms_rack_model.description = rack_request.description,
    ms_rack_model.location_type = rack_request.location_type,
    ms_rack_model.alias = rack_request.alias,
    ms_rack_model.acs_wh = rack_request.acs_wh,
    ms_rack_model.active = rack_request.active,
        
    # Add data to database
    db.add(ms_rack_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=RACK_UPDATE_SUCCESS)
        
# Create Rack
def create_rack(db:db_dependency, rack_request: RackCreate):
        
    # Post Data request
    ms_rack_model = MsRack(**rack_request.dict())
        
    # Add new data to database
    db.add(ms_rack_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=RACK_POST_SUCCESS)

    
# Remove Rack
def remove_rack(db:db_dependency, ms_rack_model: MsRack):
    db.delete(ms_rack_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=RACK_DELETE_SUCCESS)
        
   
    
    
    
    
    
    