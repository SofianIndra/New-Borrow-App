from pydantic import BaseModel

# Create Owner Body
class OwnerCreate(BaseModel):
    description:str
    
# Update Owner Body
class OwnerUpdate(BaseModel):
    description:str
    active:str
    
# Message Response
class MessageResponse(BaseModel):
    message:str