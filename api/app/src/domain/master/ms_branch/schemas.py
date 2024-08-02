from pydantic import BaseModel

# Create Branch Body
class BranchCreate(BaseModel):
    description:str
    
# Update Branch Body
class BranchUpdate(BaseModel):
    description:str
    active:str
    
# Message Response
class MessageResponse(BaseModel):
    message:str