from pydantic import BaseModel

#  Create Failure Body
class FailureCreate(BaseModel):
    vendor_code: str
    main_failure: str
    detail_failure: str
    
#  Update Failure Body
class FailureUpdate(BaseModel):
    vendor_code: str
    main_failure: str
    detail_failure: str
    active: str

# Message Response
class MessageResponse(BaseModel):
    message:str