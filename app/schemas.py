from pydantic import BaseModel, EmailStr, Field

class PatientCreate(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    phone: str = Field(..., pattern=r"^\+?[0-9]{10,15}$")

class ResponseModel(BaseModel):
    message: str