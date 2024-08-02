import io
from datetime import datetime

from fastapi import APIRouter, HTTPException, UploadFile
from googleapiclient.http import MediaIoBaseUpload
from resources.strings import (PHOTO_DELETE_SUCCESS,
                               TICKET_ANALYZE_DOES_NOT_EXIST_ERROR, VIDEO_DELETE_SUCCESS)
from src.database import db_dependency
from src.domain.transaction.tx_ticket_analyze import service
from src.domain.transaction.tx_ticket_analyze.schemas import (
    DeletePhoto, DeleteVideo, FileUrl, MessageResponse, TicketAnalyzeCreate,
    TicketAnalyzeId, TicketAnalyzeUpdate, UploadSuccessResponse)
from starlette import status

# Api Router
router = APIRouter(
    prefix='/action-progress',
    tags=['action-progress'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

# Get Selected TxTicketAnalyze Data
@router.get("/{case_number}/{serial_number}", status_code=status.HTTP_200_OK)
async def get_ticket_analyze_id(db: db_dependency, case_number: str, serial_number: str):
    # Get Selected Data
    ticket_analyze_model = service.get_selected_ticket_analyze(db, case_number, serial_number)

    # If data not found
    if ticket_analyze_model is None:
        raise HTTPException(status_code=404, detail=TICKET_ANALYZE_DOES_NOT_EXIST_ERROR)

    # Helper function to extract file ID from URL
    def extract_id_from_url(url):
        if url:
            return url.split('=')[-1]
        return None

    # Create a list of photo URLs and their IDs
    photos = []
    for photo_attr in ['photo1_url', 'photo2_url', 'photo3_url']:
        photo_url = getattr(ticket_analyze_model, photo_attr)
        photo_id = extract_id_from_url(photo_url)
        photos.append(FileUrl(id=photo_id, url=photo_url))

    # Create a list for videos
    video1_url = ticket_analyze_model.video1_url
    video1_id = extract_id_from_url(video1_url)
    videos = [FileUrl(id=video1_id, url=video1_url)]

    # Construct response data
    response_data = TicketAnalyzeId(
        id=ticket_analyze_model.id,
        photo=photos,
        video=videos
    )

    return response_data


# Save Action Progress
@router.post("/save", status_code=status.HTTP_200_OK)
async def save_action(db: db_dependency, action_request: TicketAnalyzeCreate):
    return service.create_ticket_analyze(db,action_request)


# Upload File Progress
@router.post("/upload-photo/{case_number}/{ticket_analyze_id}", status_code=status.HTTP_200_OK)
async def upload_photo(db:db_dependency, case_number:str, ticket_analyze_id:str, upload_photo: UploadFile):    
    # Read Uploaded File
    file_content = await upload_photo.read()
    # File Path
    media = MediaIoBaseUpload(io.BytesIO(file_content), mimetype=upload_photo.content_type)
    # Upload Photo
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file = service.upload_file(
            file_name= f'{case_number}_{timestamp}',
            file_path=media
        )
            
    # Set file permission to public
    service.set_file_permission(file.get('id'))
            
    # Construct the public URL
    file_url = f"https://drive.google.com/uc?id={file.get('id')}"
    
    # Update TxTicketAnalyze Photo Url
    service.update_photo_url(db, file_url, ticket_analyze_id)
    
    return UploadSuccessResponse(
        url=file_url,
        file_id=file.get('id')
    )
    
    
# Upload Video Progress
@router.post("/upload-video/{case_number}/{ticket_analyze_id}", status_code=status.HTTP_200_OK)
async def upload_video(db: db_dependency, case_number: str, ticket_analyze_id: str, upload_video: UploadFile):    
    # Read Uploaded File
    file_content = await upload_video.read()
    
    # File Path
    media = MediaIoBaseUpload(io.BytesIO(file_content), mimetype=upload_video.content_type)
    
    # Upload Video
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file = service.upload_file(
        file_name=f'{case_number}_video_{timestamp}',
        file_path=media
    )
    
    # Set file permission to public
    service.set_file_permission(file.get('id'))
    
    # Construct the embeddable video URL
    file_id = file.get('id')
    file_url = f"https://drive.google.com/file/d/{file_id}/preview"
    
    # Update TxTicketAnalyze Video Url
    service.update_video_url(db, file_url, ticket_analyze_id)
    
    return UploadSuccessResponse(
        url=file_url,
        file_id=file_id
    )
    
# Delete Uploaded Photo
@router.put("/delete-photo/{ticket_analyze_id}", status_code=status.HTTP_200_OK)
async def delete_photo(db:db_dependency, ticket_analyze_id:int, delete_request:DeletePhoto):  
    # Check Photo 1 address
    photo1_model = service.get_ticket_analyze_by_photo1(db, ticket_analyze_id,delete_request.url)
    if photo1_model is not None:
        photo1_model.photo1_url = None
        db.add(photo1_model)
        db.commit()
        
    # Check Photo 2 address
    photo2_model = service.get_ticket_analyze_by_photo2(db, ticket_analyze_id,delete_request.url)
    if photo2_model is not None:
        photo2_model.photo2_url = None
        db.add(photo2_model)
        db.commit()
        
    # Check Photo 3 address
    photo3_model = service.get_ticket_analyze_by_photo3(db, ticket_analyze_id,delete_request.url)
    if photo3_model is not None:
        photo3_model.photo3_url = None
        db.add(photo3_model)
        db.commit()

    # Delete Photo from Google Drive
    service.delete_file(delete_request.file_id)
    
    return MessageResponse(
        message=PHOTO_DELETE_SUCCESS
    )
    
    
# Delete Uploaded Video
@router.put("/delete-video/{ticket_analyze_id}", status_code=status.HTTP_200_OK)
async def delete_video(db:db_dependency, ticket_analyze_id:int, delete_request:DeleteVideo):  
    
    # Get Selected Data
    ticket_analyze_model = service.get_ticket_analyze_by_id(db, ticket_analyze_id)
    
    # Delete Video1_Url Value in database
    ticket_analyze_model.video1_url = None
    db.add(ticket_analyze_model)
    db.commit()
    
     # Delete Photo from Google Drive
    service.delete_file(delete_request.file_id)
    
    return MessageResponse(
        message=VIDEO_DELETE_SUCCESS
    )
                    

# Edit Action Progress
@router.put("/edit", status_code=status.HTTP_200_OK)
async def edit_action(db: db_dependency, action_request: TicketAnalyzeUpdate, case_number:str):
    return service.update_ticket_analyze(db,action_request,case_number)
