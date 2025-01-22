import os
import uuid
from fastapi import UploadFile, HTTPException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

UPLOAD_DIRECTORY = os.getenv("UPLOAD_DIRECTORY", "uploaded_documents")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_FILE_EXTENSIONS", "pdf,png,jpg").split(",")

def save_file(file: UploadFile) -> str:
    """
    Saves an uploaded file to the file system.

    Args:
        file (UploadFile): The uploaded file.
    
    Returns:
        str: The full path of the saved file.
    
    Raises:
        HTTPException: If the file has an invalid extension.
    """
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

    # Validate file extension
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file extension: {file_extension}. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    # Save file with a unique name
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path