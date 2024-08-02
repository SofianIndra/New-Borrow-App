from pydantic import BaseModel

#  Create Solution Body
class SolutionCreate(BaseModel):
    main_solution: str
    detail_solution: str
    
#  Update Solution Body
class SolutionUpdate(BaseModel):
    main_solution: str
    detail_solution: str
    active: str

# Message Response
class MessageResponse(BaseModel):
    message:str