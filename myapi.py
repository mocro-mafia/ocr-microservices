import pathlib

import PIL.Image
from fastapi import FastAPI, File, UploadFile, HTTPException
from io import BytesIO
from PIL import Image
import pytesseract
import logging
import io
import  uuid
import cv2
import numpy as np
import  os
#put your local path of TESSDATA
os.environ['TESSDATA_PREFIX'] = r"C:\\Program Files\\Tesseract-OCR\\tessdata"
app = FastAPI()
BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"
@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}


@app.post("/ocr/")
async def read_image(file: UploadFile = File(...)):
    bytes_str = io.BytesIO(await file.read())
    # Read the image from the byte string
    np_img = np.frombuffer(bytes_str.getvalue(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "Invalid image format"}

    # Preprocess the image (convert to grayscale, thresholding, and dilation)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Optionally, you can save the image if you want to store it
    fname = pathlib.Path(file.filename)
    fext = fname.suffix
    dest = UPLOAD_DIR / f"{uuid.uuid1()}{fext}"

    # Perform OCR on the processed image
    text = pytesseract.image_to_string(img)

    # Optionally, save the processed image (if you need to debug)
    # cv2.imwrite(str(dest), img)

    return {"text": text}