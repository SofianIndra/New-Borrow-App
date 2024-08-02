from fastapi import APIRouter
from starlette import status

from src.domain.transaction.tx_ticket_analyze_start.schemas import TicketAnalyzeStartCreate, TicketAnalyzeStartUpdate
from src.database import db_dependency
from src.domain.transaction.tx_ticket_analyze_start import service

# Api Router
router = APIRouter(
    prefix='/analyze',
    tags=['analyze'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

# Start Analyze
@router.post("/start", status_code=status.HTTP_200_OK)
async def start_analyze(db: db_dependency, analyze_request: TicketAnalyzeStartCreate):
    return service.create_ticket_analyze_start(db,analyze_request)



    
    
