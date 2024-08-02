from fastapi import APIRouter, HTTPException
from starlette import status

from src.domain.master.ms_solution import schemas
from resources.strings import SOLUTION_DOES_NOT_EXIST_ERROR
from src.database import db_dependency
from src.domain.master.ms_solution import service

# Api Router
router = APIRouter(
    prefix='/ms-solution',
    tags=['ms-solution'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Get All MsSolution Data
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_solution(db: db_dependency,):

    # Get All Data
    ms_solution_model = service.get_solution(db)

    return ms_solution_model


# Get Selected MsSolution Data
@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_selected_solution(db: db_dependency, id: int):

    # Get Selected Data 
    ms_solution_model = service.get_selected_solution(db, id)
    
    # When Data Not Found
    if ms_solution_model is not None:
        return ms_solution_model
    raise HTTPException(
        status_code=404, detail=SOLUTION_DOES_NOT_EXIST_ERROR)
    

# Get All MsSolution Data with limit
@router.get("/page/{page}", status_code=status.HTTP_200_OK)
async def get_solution_paging(db: db_dependency,page: int):

    # Get Data Limit
    ms_solution_model = service.get_solution_limit(db, page)

    return ms_solution_model
    
    
# Create New MsSolution Data
@router.post("/create", status_code= status.HTTP_201_CREATED)
async def create_solution(db: db_dependency, solution: schemas.SolutionCreate):
    
    # Create Data
    return service.create_solution(db, solution)
    

# Update MsSolution Data
@router.put('/update/{id}', status_code= status.HTTP_200_OK)
async def update_solution(db: db_dependency, solution: schemas.SolutionUpdate, id: str):
    # Update Data
    return service.update_solution(db, solution, id)


# Remove MsSolution Data
@router.delete('/delete/{id}', status_code= status.HTTP_200_OK)
async def remove_solution(db:db_dependency, id: str):
    # Get Selected Data
    ms_solution_model = service.get_selected_solution(db, id)
    
    # If data not found
    if ms_solution_model is None:
        raise HTTPException(status_code=404, detail=SOLUTION_DOES_NOT_EXIST_ERROR)
    
    # Remove Data
    return service.remove_solution(db,ms_solution_model)


    
    
