from fastapi import APIRouter, UploadFile, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from app.utils.file_upload import save_file
from app.utils.notifications.notification_factory import get_notification_service
from app.schemas import PatientCreate, ResponseModel
from app.models import Patient
from app.db import SessionLocal
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=ResponseModel)
async def register_patient(
    patient_data: str = Form(...),
    document: UploadFile = None,
    db: Session = Depends(get_db),
):
    """
    Endpoint to register patients.

    Args:
        patient_data (str): JSON string with patient data.
        document (UploadFile): Document uploaded by the patient.
        db (Session): Database session.

    Returns:
        dict: Success message.
    """
    # Parse and validate patient_data
    try:
        parsed_data = json.loads(patient_data)
        patient_obj = PatientCreate(**parsed_data)  # Validate with Pydantic
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")

    # Check if the email already exists
    existing_patient = db.query(Patient).filter(Patient.email == patient_obj.email).first()
    if existing_patient:
        raise HTTPException(status_code=400, detail="Email already exists. Please use a different email.")

    if not document:
        raise HTTPException(status_code=400, detail="Document is required.")

    # Save the document
    try:
        document_path = save_file(document)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

    # Save the patient in the database
    try:
        new_patient = Patient(
            name=patient_obj.name,
            email=patient_obj.email,
            phone=patient_obj.phone,
            document_path=document_path
        )
        db.add(new_patient)
        db.commit()

     # Use NotificationFactory to send an email
        notification_service = get_notification_service("email")
        await notification_service.send_notification(
            recipient=new_patient.email,
            subject="Registration Confirmation",
            body=f"Hello {new_patient.name},\n\nThank you for registering. Your account has been successfully created."
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving patient to database: {str(e)}")

    return {"message": "Patient registered successfully."}

@router.get("/patients", response_model=list)
async def get_patients(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve the list of registered patients.

    Args:
        db (Session): Database session.

    Returns:
        list: List of patients.
    """
    try:
        patients = db.query(Patient).all()
        return [
            {
                "id": patient.id,
                "name": patient.name,
                "email": patient.email,
                "phone": patient.phone,
                "document_path": patient.document_path,
            }
            for patient in patients
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving patients: {str(e)}")
