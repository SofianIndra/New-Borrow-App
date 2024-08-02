from fastapi import APIRouter, HTTPException
from starlette import status

from src.domain.master.ms_action import schemas
from resources.strings import ACTION_DOES_NOT_EXIST_ERROR
from src.database import db_dependency
from src.domain.master.ms_action import service

# Api Router
router = APIRouter(
    prefix='/ms-action',
    tags=['ms-action'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Get All MsAction Data
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_action(db: db_dependency,):

    # Get All Data
    ms_action_model = service.get_action(db)

    return ms_action_model


# Get Selected MsAction Data
@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_selected_action(db: db_dependency, id: int):

    # Get Selected Data 
    ms_action_model = service.get_selected_action(db, id)
    
    # When Data Not Found
    if ms_action_model is not None:
        return ms_action_model
    raise HTTPException(
        status_code=404, detail=ACTION_DOES_NOT_EXIST_ERROR)
    

# Get All MsAction Data with limit
@router.get("/page/{page}", status_code=status.HTTP_200_OK)
async def get_action_paging(db: db_dependency,page: int):

    # Get Data Limit
    ms_address_model = service.get_action_limit(db, page)

    return ms_address_model
    
    
# Create New MsAction Data
@router.post("/create", status_code= status.HTTP_201_CREATED)
async def create_action(db: db_dependency, action: schemas.ActionCreate):
    
    # Create Data
    return service.create_action(db, action)
    

# Update MsAction Data
@router.put('/update/{code}', status_code= status.HTTP_200_OK)
async def update_action(db: db_dependency, action: schemas.ActionUpdate, code: str):
    
    # Update Data
    return service.update_action(db, action, code)


# Remove MsAction Data
@router.delete('/delete/{code}', status_code= status.HTTP_200_OK)
async def remove_action(db:db_dependency, code: str):
    # Get Selected Data
    ms_action_model = service.get_selected_action(db, code)
    
    # If data not found
    if ms_action_model is None:
        raise HTTPException(status_code=404, detail=ACTION_DOES_NOT_EXIST_ERROR)
    
    # Remove Data
    return service.remove_action(db,ms_action_model)


    
    
