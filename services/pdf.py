from fastapi import Response
from starlette.background import BackgroundTask
from fastapi.responses import FileResponse
from PyPDF2 import PdfReader, PdfWriter
import io
import base64
import os




def remove_file(path: str) -> None:
    os.remove(path)



def pdfroatation(file, angle_of_rotation:int, page_number:int):
    try:

        document = io.BytesIO(file)
        pdf_reader = PdfReader(document)
        pdf_page_numbers = len(pdf_reader.pages)
        page_number = int(page_number)
        angle_of_rotation = int(angle_of_rotation)
        file_name = f"abx.pdf"


        if angle_of_rotation not in [90,180,270]:
            return {"message":"Angle of Rotation degree must be one of these 90, 180, 270"}

        if page_number not in range(1, pdf_page_numbers+1):
            return {"message":f"input page number does not exists because this pdf only contain {pdf_page_numbers} pages"}

        writer = PdfWriter()
        return_data = io.BytesIO()

        for idxnum, page in enumerate(pdf_reader.pages):
            if idxnum == page_number-1:
                page.rotate_clockwise(angle_of_rotation)
            writer.add_page(page)


        with open(file_name, "wb") as pdf_out:
            writer.write(pdf_out)


        with open(file_name, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)  


        headers = {'Content-Disposition': 'inline; filename="don.pdf"'}
        return Response(return_data.getvalue(), headers=headers,media_type="application/octet-stream", background=BackgroundTask(remove_file, file_name))

 
    except Exception as e:
      print(e)
      return {"message":"Only pdf file are allowed"},400
    



def pdfbsfrotation(file, angle_of_rotation:int, page_number:int):

    try:

        document = io.BytesIO(file)
        pdf_reader = PdfReader(document)
        pdf_page_numbers = len(pdf_reader.pages)
        page_number = int(page_number)
        angle_of_rotation = int(angle_of_rotation)


        if angle_of_rotation not in [90,180,270]:
            return {"message":"Angle of Rotation degree must be one of these 90, 180, 270"}

        if page_number not in range(1, pdf_page_numbers+1):
            return {"message":f"input page number does not exists because this pdf only contain {pdf_page_numbers} pages"}


        writer = PdfWriter()
        return_data = io.BytesIO()
        write_data = io.BytesIO()


        for idxnum, page in enumerate(pdf_reader.pages):
            if idxnum == page_number-1:
                page.rotate_clockwise(angle_of_rotation)
            writer.add_page(page)

        writer.write(return_data)
        write_data.write(b"data:application/pdf;base64,")
        write_data.write(base64.b64encode(return_data.getvalue()))
        write_data.seek(0)


        return Response(write_data.getvalue(), media_type="application/pdf")

 
    except Exception as e:
      print(e)
      return {"message":"Only pdf file are allowed"},400