from fastapi import FastAPI, UploadFile, File, HTTPException
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
from PIL import Image
import io
import re
from datetime import datetime
from .models import MoroccanID

app = FastAPI()

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

def extract_id_info(text: str) -> MoroccanID:
    # Regex patterns for Moroccan ID fields
    patterns = {
        'id_number': r'[A-Z][0-9]{7}',
        'birth_date': r'\d{2}/\d{2}/\d{4}',
        'expiry_date': r'Valable jusqu\'au \d{2}/\d{2}/\d{4}',
        'name_latin': r'[A-Z\s]+(?=\s*\d)',  # Captures Latin name before numbers
    }
    
    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted[key] = match.group(0)
    
    return MoroccanID(
        id_number=extracted.get('id_number'),
        full_name_latin=extracted.get('name_latin'),
        full_name_arabic="",  # Needs Arabic OCR model
        birth_date=datetime.strptime(extracted.get('birth_date'), '%d/%m/%Y').date(),
        birth_place=extracted.get('birth_place', ""),
        expiry_date=datetime.strptime(extracted.get('expiry_date').replace('Valable jusqu\'au ', ''), '%d/%m/%Y').date(),
        document_number=extracted.get('id_number')
    )

@app.post("/process")
async def process_id(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "File must be an image")
    
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    pixel_values = processor(image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    id_data = extract_id_info(generated_text)
    # Store data in storage service
    await store_id_data(id_data)
    return id_data