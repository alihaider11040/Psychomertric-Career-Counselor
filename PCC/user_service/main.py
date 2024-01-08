from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from pydantic import BaseModel
from typing import List
from passlib.context import CryptContext  # for password hashing

# SQLite Database URL
DATABASE_URL = "sqlite:///./USER.db"

# SQLAlchemy Models
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    hashed_password = Column(String)  # Store hashed password
    user_type = Column(String)

# Create SQLite engine
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Enable CORS
origins = ["*"]  # You can replace "*" with the specific origins you want to allow



# Dependency to get the database session
def get_db():
    db = Session(autocommit=False, autoflush=False, bind=engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Pydantic User model for request and response
class User(BaseModel):
    username: str
    email: str
    password: str  # New password field
    user_type: str

class LoginResponse(BaseModel):
   
    email: str
    username: str
    user_type: str  # Adjust this based on your UserDB model
# Password hashing
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class LoginRequest(BaseModel):
    email: str
    password: str
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# CRUD operations
# Create a new user
@app.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    # Hash the password before storing it in the database
    hashed_password = password_context.hash(user.password)
    
    db_user = UserDB(username=user.username, email=user.email, hashed_password=hashed_password, user_type=user.user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

# Function to verify the provided password against the stored hashed password
def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)
# Read all users
@app.get("/users/", response_model=List[User])
def read_users(db: Session = Depends(get_db)):
    return db.query(UserDB).all()

# Read a specific user by username
@app.post("/login/", response_model=LoginResponse)
async def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.email == login_request.email).first()
    
    if user and verify_password(login_request.password, user.hashed_password):
        return LoginResponse( username=user.username,email=user.email, user_type=user.user_type)
    
    raise HTTPException(status_code=401, detail="Invalid credentials")
# Update a specific user by username
@app.put("/users/{username}", response_model=User)
def update_user(username: str, updated_user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.username == username).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Update fields if provided
    if updated_user.email:
        db_user.email = updated_user.email
    if updated_user.user_type:
        db_user.user_type = updated_user.user_type
    if updated_user.password:
        db_user.hashed_password = password_context.hash(updated_user.password)

    db.commit()
    db.refresh(db_user)
    return updated_user

# Delete a specific user by username
@app.delete("/users/{username}", response_model=User)
def delete_user(username: str, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return User(username=user.username, email=user.email, user_type=user.user_type)
