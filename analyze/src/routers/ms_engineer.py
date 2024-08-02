from fastapi import APIRouter, HTTPException
from starlette import status

from src.domain.master.ms_engineer import schemas
from resources.strings import ENGINEER_DOES_NOT_EXIST_ERROR
from src.database import db_dependency
from src.domain.master.ms_engineer import service

# Api Router
router = APIRouter(
    prefix='/ms-engineer',
    tags=['ms-engineer'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Get All MsEngineer Data
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_engineer(db: db_dependency,):

    # Get All Data
    ms_engineer_model = service.get_engineers(db)

    return ms_engineer_model


# Get Selected MsEngineer Data
@router.get("/{code}", status_code=status.HTTP_200_OK)
async def get_selected_engineer(db: db_dependency, code: str):

    # Get Selected Data 
    ms_engineer_model = service.get_selected_engineer(db, code)
    
    # When Data Not Found
    if ms_engineer_model is not None:
        return ms_engineer_model
    raise HTTPException(
        status_code=404, detail=ENGINEER_DOES_NOT_EXIST_ERROR)
    

# Get All MsEngineer Data with limit
@router.get("/page/{page}", status_code=status.HTTP_200_OK)
async def get_engineer_paging(db: db_dependency,page: int):

    # Get Data Limit
    ms_engineer_model = service.get_engineer_limit(db, page)

    return ms_engineer_model
    
    
# Create New MsEngineer Data
@router.post("/create", status_code= status.HTTP_201_CREATED)
async def create_engineer(db: db_dependency, engineer: schemas.EngineerCreate):
    
    # Create Data
    return service.create_engineer(db, engineer)
    

# Update MsEngineer Data
@router.put('/update/{code}', status_code= status.HTTP_200_OK)
async def update_engineer(db: db_dependency, engineer: schemas.EngineerUpdate, code: str):
    # Update Data
    return service.update_engineer(db, engineer, code)


# Remove MsEngineer Data
@router.delete('/delete/{code}', status_code= status.HTTP_200_OK)
async def remove_engineer(db:db_dependency, code: str):
    # Get Selected Data
    ms_engineer_model = service.get_selected_engineer(db, code)
    
    # If data not found
    if ms_engineer_model is None:
        raise HTTPException(status_code=404, detail=ENGINEER_DOES_NOT_EXIST_ERROR)
    
    # Remove Data
    return service.remove_engineer(db,ms_engineer_model)


    
    
