# Puppeteer-Santiago-Rossi 

## Requirements
- **Python 3.10+**
- **PostgreSQL 13+**
- **Docker & Docker Compose**

---

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/santiagorossisosa/Puppeteer.git

# Navigate to the project directory
cd Puppeteer-Santiago-Rossi

# Build and start the Docker containers (use this when Dockerfile or dependencies change)
docker-compose up --build

# Start the Docker containers without rebuilding (use when no changes were made)
# -d background mode
docker-compose up
```

The API will be available at: [http://localhost:8000](http://localhost:8000)

# Connecting to the Database

This document explains how to connect to the PostgreSQL database used by the API. You can use tools like **pgAdmin** for easy database management and interaction.

---

## **Database Configuration**
The database credentials are managed via environment variables stored in the `.env` file. Here are the relevant configurations:

- **Host:** `localhost` (or `db` if accessing from within Docker Compose network)
- **Port:** `5432`
- **Username:** `${POSTGRES_USER}`
- **Password:** `${POSTGRES_PASSWORD}`
- **Database Name:** `${POSTGRES_DB}`

Make sure you have the `.env` file set up with these variables.

---


# API Endpoints Documentation

This document provides a brief overview of the available endpoints for the Patient Management API.

---

## **Endpoints**

### 1. **Register Patient**
- **URL:** `/register`
- **Method:** `POST`
- **Description:** Registers a new patient in the system.
- **Request Format:** `multipart/form-data`
  - **Fields:**
    - `patient_data`: JSON string with patient details (`name`, `email`, `phone`).
    - `document`: File upload (e.g., ID or other document).
- **Response:**
  ```json
  {
      "message": "Patient registered successfully."
  }
  ```
- **Error Responses:**
  - `400`: Invalid input or email already exists.
  - `500`: Server error.

### CURL example (For example, to import into Postman)
```
curl --location 'http://localhost:8000/register' \
--form 'patient_data="{\"name\":\"John Doe\",\"email\":\"john3e@example.com\",\"phone\":\"+1234567890\"}"' \
--form 'document=@"/path/doc.pdf"'
```
---

### 2. **Get All Patients**
The “Get All Patients” endpoint was not included in the original requirements. It has been added as an extra functionality to allow for easy retrieval and verification of registered patients.
- **URL:** `/patients`
- **Method:** `GET`
- **Description:** Retrieves a list of all registered patients in a readable format.
- **Response:**
  ```json
  [
      {
          "ID": 1,
          "Name": "John Doe",
          "Email": "john@example.com",
          "Phone": "+1234567890",
          "Document": "path/to/document.pdf"
      },
      {
          "ID": 2,
          "Name": "Jane Doe",
          "Email": "jane@example.com",
          "Phone": "+0987654321",
          "Document": "path/to/document.pdf"
      }
  ]
  ```
- **Error Responses:**
  - `500`: Server error.

---
