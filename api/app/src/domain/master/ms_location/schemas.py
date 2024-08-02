from pydantic import BaseModel


# Create Location Body
class LocationCreate(BaseModel):
    description:str
    
# Update Location Body
class LocationUpdate(BaseModel):
    description:str
    active:str
    
# Message Response
class MessageResponse(BaseModel):
    message:str