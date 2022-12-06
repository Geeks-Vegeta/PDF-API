from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes import pdf_route, pdfbsf_route


description = '''

This is pdf api

'''

app = FastAPI(
    title="PDF API",
    description=description,
    version=0.1
)


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ok"}

app.include_router(pdf_route.route)
app.include_router(pdfbsf_route.route)



if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=3000)