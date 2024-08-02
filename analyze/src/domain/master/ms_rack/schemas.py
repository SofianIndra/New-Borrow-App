from pydantic import BaseModel

#  Create Rack Body
class RackCreate(BaseModel):
    code: str
    description: str
    location_type: str
    alias: str
    acs_wh: str
    
    
#  Update Rack Body
class RackUpdate(BaseModel):
    code: str
    description: str
    location_type: str
    alias: str
    acs_wh: str
    active: str

# Message Response
class MessageResponse(BaseModel):
    message:str