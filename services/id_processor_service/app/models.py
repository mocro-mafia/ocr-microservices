from pydantic import BaseModel
from datetime import date

class MoroccanID(BaseModel):
    id_number: str
    full_name_latin: str
    full_name_arabic: str
    birth_date: date
    birth_place: str
    expiry_date: date
    document_number: str