from fastapi import APIRouter
from src.routers import (action_progress, analyze, ms_action, ms_engineer,
                         ms_failure, ms_rack, ms_solution)

router = APIRouter()

def include_api_routes():
    ''' Include to router all api rest routes with version prefix '''
    router.include_router(ms_action.router)
    router.include_router(ms_engineer.router)
    router.include_router(ms_failure.router)
    router.include_router(ms_rack.router)
    router.include_router(ms_solution.router)
    router.include_router(analyze.router)
    router.include_router(action_progress.router)
    
include_api_routes()