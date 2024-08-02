from typing import Optional
from pydantic import BaseModel

# Create Asset Body
class AssetCreate(BaseModel):
    parent_id:Optional[int]
    serial_number:Optional[str]
    part_number:Optional[str]
    branch_id:int
    branch:str
    asset_number:str
    category_id:int
    category:str
    
    
# Update Asset Body
class AssetUpdate(BaseModel):
    description:str
    active:str
    
# Message Response
class MessageResponse(BaseModel):
    message:str