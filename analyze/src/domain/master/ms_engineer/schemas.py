from pydantic import BaseModel

#  Create Engineer Body
class EngineerCreate(BaseModel):
    code: str
    name: str
    
#  Update Engineer Body
class EngineerUpdate(BaseModel):
    code: str
    name: str
    active: str

# Message Response
class MessageResponse(BaseModel):
    message:str