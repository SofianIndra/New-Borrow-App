from fastapi import APIRouter, HTTPException
from starlette import status

from src.domain.master.ms_rack import schemas
from resources.strings import RACK_DOES_NOT_EXIST_ERROR
from src.database import db_dependency
from src.domain.master.ms_rack import service

# Api Router
router = APIRouter(
    prefix='/ms-rack',
    tags=['ms-rack'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Get All MsRack Data
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_rack(db: db_dependency,):

    # Get All Data
    ms_rack_model = service.get_racks(db)

    return ms_rack_model


# Get Selected MsRack Data
@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_selected_rack(db: db_dependency, code: str):

    # Get Selected Data 
    ms_rack_model = service.get_selected_rack(db, code)
    
    # When Data Not Found
    if ms_rack_model is not None:
        return ms_rack_model
    raise HTTPException(
        status_code=404, detail=RACK_DOES_NOT_EXIST_ERROR)
    
    
# Get Selected Rack By Location type and ACS WH
@router.get("/{location_type}/{acs_wh}", status_code=status.HTTP_200_OK)
async def get_rack_by_location_type_and_acswh(db: db_dependency, location_type: str, acs_wh:str):

    # Get Selected Data 
    ms_rack_model = service.get_rack_by_location_type_and_acswh(db, location_type,acs_wh)
    
    # When Data Not Found
    if ms_rack_model is not None:
        return ms_rack_model
    raise HTTPException(
        status_code=404, detail=RACK_DOES_NOT_EXIST_ERROR)
    

# Get All MsRack Data with limit
@router.get("/page/{page}", status_code=status.HTTP_200_OK)
async def get_rack_paging(db: db_dependency,page: int):

    # Get Data Limit
    ms_rack_model = service.get_rack_limit(db, page)

    return ms_rack_model
    
    
# Create New MsRack Data
@router.post("/create", status_code= status.HTTP_201_CREATED)
async def create_rack(db: db_dependency, rack: schemas.RackCreate):
    
    # Create Data
    return service.create_rack(db, rack)
    

# Update MsRack Data
@router.put('/update/{code}', status_code= status.HTTP_200_OK)
async def update_rack(db: db_dependency, rack: schemas.RackUpdate, code: str):
    # Update Data
    return service.update_rack(db, rack, code)


# Remove MsRack Data
@router.delete('/delete/{code}', status_code= status.HTTP_200_OK)
async def remove_rack(db:db_dependency, code: str):
    # Get Selected Data
    ms_rack_model = service.get_selected_rack(db, code)
    
    # If data not found
    if ms_rack_model is None:
        raise HTTPException(status_code=404, detail=RACK_DOES_NOT_EXIST_ERROR)
    
    # Remove Data
    return service.remove_rack(db,ms_rack_model)


    
    
