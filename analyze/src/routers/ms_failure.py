from fastapi import APIRouter, HTTPException
from starlette import status

from src.domain.master.ms_failure import schemas
from resources.strings import FAILURE_DOES_NOT_EXIST_ERROR
from src.database import db_dependency
from src.domain.master.ms_failure import service

# Api Router
router = APIRouter(
    prefix='/ms-failure',
    tags=['ms-failure'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Get All MsFailure Data
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_failure(db: db_dependency,):

    # Get All Data
    ms_failure_model = service.get_failure(db)
    
    print(ms_failure_model)

    return ms_failure_model


# Get Selected MsFailure Data
@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_selected_failure(db: db_dependency, id: int):

    # Get Selected Data 
    ms_failure_model = service.get_selected_failure(db, id)
    
    # When Data Not Found
    if ms_failure_model is not None:
        return ms_failure_model
    raise HTTPException(
        status_code=404, detail=FAILURE_DOES_NOT_EXIST_ERROR)
    
    
# Get Selected MsFailure Data by vendor code
@router.get("/vendor/{vendor_code}", status_code=status.HTTP_200_OK)
async def get_failure_by_vendor_code(db: db_dependency, vendor_code: str):

    # Get Selected Data 
    ms_failure_model = service.get_failure_by_vendor_code(db, vendor_code)
    
    # When Data Not Found
    if ms_failure_model is not None:
        return ms_failure_model
    raise HTTPException(
        status_code=404, detail=FAILURE_DOES_NOT_EXIST_ERROR)
    

# Get All MsFailure Data with limit
@router.get("/page/{page}", status_code=status.HTTP_200_OK)
async def get_failure_paging(db: db_dependency,page: int):

    # Get Data Limit
    ms_failure_model = service.get_failure_limit(db, page)

    return ms_failure_model
    
    
# Create New MsFailure Data
@router.post("/create", status_code= status.HTTP_201_CREATED)
async def create_failure(db: db_dependency, failure: schemas.FailureCreate):
    
    # Create Data
    return service.create_failure(db, failure)
    

# Update MsFailure Data
@router.put('/update/{id}', status_code= status.HTTP_200_OK)
async def update_failure(db: db_dependency, failure: schemas.FailureUpdate, id: int):
    # Update Data
    return service.update_failure(db, failure, id)


# Remove MsFailure Data
@router.delete('/delete/{id}', status_code= status.HTTP_200_OK)
async def remove_failure(db:db_dependency, id: int):
    # Get Selected Data
    ms_failure_model = service.get_selected_failure(db, id)
    
    # If data not found
    if ms_failure_model is None:
        raise HTTPException(status_code=404, detail=FAILURE_DOES_NOT_EXIST_ERROR)
    
    # Remove Data
    return service.remove_failure(db,ms_failure_model)


    
    
