from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime

# FastAPI app
app = FastAPI()

# MySQL connection settings
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/id_cards_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model for ID cards
class IDCard(Base):
    __tablename__ = "id_cards"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to store ID card data
@app.post("/store")
def store_id_data(data: dict, db: Session = Depends(get_db)):
    if "name" not in data:
        raise HTTPException(status_code=400, detail="Missing 'name' field")
    
    id_card = IDCard(name=data["name"], description=data.get("description", ""))
    db.add(id_card)
    db.commit()
    db.refresh(id_card)
    return {"id": id_card.id}

# Endpoint to retrieve ID card data
@app.get("/retrieve/{id}")
def get_id_data(id: int, db: Session = Depends(get_db)):
    id_card = db.query(IDCard).filter(IDCard.id == id).first()
    if not id_card:
        raise HTTPException(status_code=404, detail="ID card data not found")
    
    return {
        "id": id_card.id,
        "name": id_card.name,
        "description": id_card.description,
        "created_at": id_card.created_at
    }
