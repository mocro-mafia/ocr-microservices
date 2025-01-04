from sqlalchemy import Column, String, Date
from .database import Base

class MoroccanID(Base):
    __tablename__ = "moroccan_ids"

    id_number = Column(String(50), primary_key=True, index=True)
    full_name_latin = Column(String(100), index=True)
    full_name_arabic = Column(String(100), index=True)
    birth_date = Column(Date)
    birth_place = Column(String(100))
    expiry_date = Column(Date)
    document_number = Column(String(50), index=True)