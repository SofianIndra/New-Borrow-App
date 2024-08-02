from pydantic import BaseModel


# Create Category Body
class CategoryCreate(BaseModel):
    description:str
    
# Update Category Body
class CategoryUpdate(BaseModel):
    description:str
    active:str
    
# Message Response
class MessageResponse(BaseModel):
    message:str