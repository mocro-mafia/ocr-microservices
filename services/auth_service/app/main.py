# filepath: /C:/Users/Namous Mohamed/Desktop/ocr-microservices/services/auth_service/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database, auth
from .database import engine, get_db
from .auth import get_current_user

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = auth.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth.create_user(db=db, user=user)

@app.post("/login", response_model=schemas.Token)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, user_credentials.email, user_credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user", response_model=schemas.User)
def get_user_details(current_user: schemas.User = Depends(get_current_user)):
    return current_user

@app.put("/update_profile", response_model=schemas.User)
def update_profile(user: schemas.UserUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db_user = auth.get_user_by_email(db, email=current_user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.email = user.email
    db_user.full_name = user.full_name
    db_user.hashed_password = auth.get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user