from fastapi import APIRouter, status, File, UploadFile
from typing import List, Union
from services.pdf import pdfroatation
from enum import Enum

# class Angles(int, Enum):
#     "90" = 90
#     "180" = 180
#     "270" = 270

route = APIRouter(
    tags=["pdf rotation"],
)



@route.post("/pdf",responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Return the pdf of comics.",
        }
    }, 
    summary="Basic Pdf Rotation",
    response_description="pdf created"
    )
async def pdf(*,file: bytes = File(), angle_of_rotation:int,  page_number:int):
    """
    This api will rotate single page in pdf file and resend pdf as it is:

    - **file**: Make sure it's a pdf file
    - **angle_of_rotation**: an angel of rotation should be with in [90, 180, 270]
    - **page_number**: required
    """
    # return {"filename": len(file)}

    return pdfroatation(file, angle_of_rotation, page_number)