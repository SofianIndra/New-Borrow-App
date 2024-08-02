from pydantic import BaseModel

# Create Status Body
class StatusCreate(BaseModel):
    description:str
    
# Update Status Body
class StatusUpdate(BaseModel):
    description:str
    active:str
    
# Message Response
class MessageResponse(BaseModel):
    message:str