from pydantic import BaseModel

# Create Action Body
class ActionCreate(BaseModel):
    name: str
    active:str
    
# Update Action Body
class ActionUpdate(BaseModel):
    name: str
    active:str
    
# Message Response
class MessageResponse(BaseModel):
    message:str