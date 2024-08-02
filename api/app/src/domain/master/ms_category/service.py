from fastapi import HTTPException
from resources.strings import (CATEGORY_DELETE_SUCCESS,
                               CATEGORY_DOES_NOT_EXIST_ERROR,
                               CATEGORY_POST_SUCCESS, CATEGORY_UPDATE_SUCCESS)
from src.config import ACTIVE_DATA, LIMIT
from src.database import db_dependency
from src.domain.master.ms_category.models import MsCategory
from src.domain.master.ms_category.schemas import (CategoryCreate,
                                                   CategoryUpdate,
                                                   MessageResponse)


# Get Category Data
def get_categories(db: db_dependency):
    return db.query(MsCategory).filter(MsCategory.active == ACTIVE_DATA).order_by(MsCategory.description.asc()).all()


# Get Category Data LIMIT
def get_category_limit(db: db_dependency, page: int):
    offset = (page - 1) * LIMIT
    
    return db.query(MsCategory).filter(MsCategory.active == ACTIVE_DATA).order_by(MsCategory.description.asc()).offset(offset).limit(LIMIT).all()


# Get Selected Category
def get_selected_category(db:db_dependency, id: int):
    return db.query(MsCategory).filter(
        MsCategory.active == ACTIVE_DATA,
        MsCategory.id == id
    ).first()
    

# Update Category
def update_category(db:db_dependency, category_request: CategoryUpdate, id:int):
    # Get Selected Data
    category_model = get_selected_category(db, id)
        
    # When data not found
    if category_model is None:
        raise HTTPException(
            status_code=404, detail= CATEGORY_DOES_NOT_EXIST_ERROR)
        
    # Variable that want to update
    category_model.description = category_request.description,
    category_model.active = category_request.active,
        
    # Add data to database
    db.add(category_model)
    db.commit()
        
    # Update Response
    return MessageResponse(message=CATEGORY_UPDATE_SUCCESS)
        
# Create Category
def create_category(db:db_dependency, category_request: CategoryCreate):
        
    # Post Data request
    category_model = MsCategory(**category_request.dict())
        
    # Add new data to database
    db.add(category_model)
    db.commit()
        
    # Post Response
    return MessageResponse(message=CATEGORY_POST_SUCCESS)

    
# Remove Category
def remove_category(db:db_dependency, category_model: MsCategory):
    db.delete(category_model)
    db.commit()
        
    # Delete Response
    return MessageResponse(message=CATEGORY_DELETE_SUCCESS)
        
   
    
    
    
    
    
    