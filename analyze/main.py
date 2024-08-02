from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from src.routers.handlers.http_error import http_error_handler

from src.database import Base, SessionLocal, engine

from src.routers.api import router as router_api


###
# Main application file
###

def get_application() -> FastAPI:
    ''' Configure, start and return the application '''
    
    ## Start FastApi App 
    application = FastAPI()

    ## Generate database tables
    Base.metadata.create_all(bind=engine)

    ## Mapping api routes
    application.include_router(router_api)

    ## Add exception handlers
    application.add_exception_handler(HTTPException, http_error_handler)


    # adding cors urls
    origins = [
        "http://localhost",
        "http://localhost:3000",
    ]
    
    ## Allow cors
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )   

  
    
    return application


app = get_application()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    '''
    The middleware we'll add (just a function) will create
    a new SQLAlchemy SessionLocal for each request, add it to
    the request and then close it once the request is finished.
    '''
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response